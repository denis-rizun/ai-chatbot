from fastapi import APIRouter
from starlette.requests import Request

from src.application.ai.groq import GroqModel
from src.application.ai.mini_lm import MiniLMModel
from src.application.pipelines.pipeline import Pipeline
from src.application.pipelines.inference.ask import AskStep
from src.application.pipelines.inference.cache_reader import CacheReadStep
from src.application.pipelines.inference.cache_writer import CacheWriteStep
from src.application.pipelines.inference.search import SearchContextStep
from src.delivery.helper import APIHelper
from src.domain.entities.pipelines.inference import Inference
from src.infrastructure.dto.conversation import ConversationDTO, ConversationQueryDTO
from src.infrastructure.dto.response import ResponseDTO

router = APIRouter(prefix="/conversations", tags=["conversation"])


@router.post(path="", response_model=ResponseDTO[ConversationDTO])
async def ask(request: Request, body: ConversationQueryDTO) -> ResponseDTO:
    repo = request.state.repository
    model = MiniLMModel()
    steps = [
        CacheReadStep(repo, model),
        SearchContextStep(repo),
        AskStep(GroqModel()),
        CacheWriteStep(repo)
    ]
    pipeline = Pipeline(steps)
    response = await pipeline.run(Inference.build(body.model_dump()))
    return APIHelper.unified_response(ConversationDTO.build(response))
