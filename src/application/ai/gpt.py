from typing import Any

from openai import AsyncOpenAI

from src.core.config import config
from src.domain.interfaces.services.ai import IAIModel


class GPTModel(IAIModel):
    _EMBEDDING_MODEL = "text-embedding-ada-002"

    def __init__(self) -> None:
        self._client = AsyncOpenAI(api_key=config.CHATGPT_API_KEY)

    async def ask(self, q: str) -> str:
        pass

    async def embed(self, text: str) -> Any:
        response = await self._client.embeddings.create(
            input=text,
            model=self._EMBEDDING_MODEL
        )

        return response.data[0].embedding
