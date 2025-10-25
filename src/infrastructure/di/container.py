from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Resource, Factory

from src.application.ai.gpt import GPTModel
from src.application.ai.groq import GroqModel
from src.application.ai.mini_lm import MiniLMModel
from src.application.embedding import EmbeddingService
from src.application.pipelines.add_context.embedding import GenerateEmbeddingStep
from src.application.pipelines.add_context.split import SplitTextStep
from src.application.pipelines.inference.ask import AskStep
from src.application.pipelines.inference.cache_reader import CacheReadStep
from src.application.pipelines.inference.cache_writer import CacheWriteStep
from src.application.pipelines.inference.search import SearchContextStep
from src.infrastructure.database.repositories.manager import RepositoryManager
from src.infrastructure.database.sessions import RedisSession, PostgresSession


class Container(DeclarativeContainer):
    postgres_session_factory = Resource(PostgresSession.initialize)
    postgres_session = Resource(
        lambda session_factory: session_factory(),
        session_factory=postgres_session_factory
    )
    redis_client = Resource(RedisSession.init)

    repo = Factory(RepositoryManager, session=postgres_session, client=redis_client)

    mini_lm_model = Factory(MiniLMModel)
    groq_model = Factory(GroqModel)
    gpt_model = Factory(GPTModel)

    embed_service = Factory(EmbeddingService, repository=repo, ai_model=mini_lm_model)

    split_text_step = Factory(SplitTextStep)
    generate_embedding_step = Factory(GenerateEmbeddingStep, embedding_service=embed_service)
    cache_read_step = Factory(CacheReadStep, repository=repo, ai_model=mini_lm_model)
    search_context_step = Factory(SearchContextStep, repository=repo)
    ask_step = Factory(AskStep, ai_model=groq_model)
    cache_write_step = Factory(CacheWriteStep, repository=repo)


container = Container()
