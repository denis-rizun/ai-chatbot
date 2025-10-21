import asyncio

import torch
from sentence_transformers import SentenceTransformer

from src.domain.interfaces.services.ai import IAIModel


class MiniLMModel(IAIModel):
    _EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    def __init__(self) -> None:
        self._model = SentenceTransformer(self._EMBEDDING_MODEL)
        if torch.cuda.is_available():
            self._model = self._model.to("cuda")

    async def ask(self, q: str) -> str:
        pass

    async def embed(self, text: str | list[str]) -> list[float]:
        embedding = await asyncio.to_thread(self._model.encode, text, convert_to_tensor=False)
        return embedding.tolist() if hasattr(embedding, "tolist") else embedding
