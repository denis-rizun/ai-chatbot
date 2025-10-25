from openai import AsyncOpenAI

from src.core.config import config
from src.core.constants import AI_QUERY_PROMPT
from src.domain.interfaces.services.ai import IAIModel


class GroqModel(IAIModel):
    _BASE_URL = "https://api.groq.com/openai/v1"
    _MODEL_NAME = "llama-3.1-8b-instant"
    _MAX_TOKENS = 1000

    def __init__(self) -> None:
        self._client = AsyncOpenAI(api_key=config.GROQ_API_KEY, base_url=self._BASE_URL)

    async def ask(self, q: str, context: str) -> str:
        return "all good"

    async def embed(self, text: str) -> list[float]:
        pass

    @staticmethod
    def _prepare_messages(q: str, context: str) -> list[dict[str, str]]:
        system_content = f"{AI_QUERY_PROMPT}:{context}"
        return [
            {"role": "user", "content": q},
            {"role": "system", "content": system_content}
        ]
