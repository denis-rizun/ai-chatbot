from openai import AsyncOpenAI

from src.core.config import config
from src.core.constants import AI_QUERY_PROMPT
from src.domain.interfaces.services.ai import IAIModel


class GPTModel(IAIModel):
    _EMBEDDING_MODEL = "text-embedding-ada-002"
    _MODEL_NAME = "gpt-5"
    _MAX_TOKENS = 1000

    def __init__(self) -> None:
        self._client = AsyncOpenAI(api_key=config.CHATGPT_API_KEY)

    async def ask(self, q: str, context: str) -> str:
        response = await self._client.chat.completions.create(
            model=self._MODEL_NAME,
            messages=self._prepare_messages(q, context),
            max_tokens=self._MAX_TOKENS
        )
        return response.choices[0].message.content

    async def embed(self, text: str) -> list[float]:
        response = await self._client.embeddings.create(
            input=text,
            model=self._EMBEDDING_MODEL
        )

        return response.data[0].embedding

    @staticmethod
    def _prepare_messages(q: str, context: str) -> list[dict[str, str]]:
        system_content = f"{AI_QUERY_PROMPT}:{context}"
        return [
            {"role": "user", "content": q},
            {"role": "system", "content": system_content}
        ]
