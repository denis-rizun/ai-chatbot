from typing import Any

import numpy as np
from redis.asyncio import Redis
from redis.commands.search.query import Query

from src.domain.interfaces.repositories.cache import ICacheRepository


class CacheRepository(ICacheRepository):
    def __init__(self, client: Redis) -> None:
        self.client = client

    async def get(self, key: str) -> Any | None:
        return await self.client.get(key)

    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        await self.client.set(key, value, ex=ttl)

    async def delete(self, key: str) -> None:
        await self.client.delete(key)

    async def exists(self, key: str) -> bool:
        return await self.client.exists(key) > 0

    async def set_hashed(self, key: str, data: dict[str, Any]) -> None:
        vector = data["embedding"]
        data["embedding"] = np.array(vector, dtype=np.float32).tobytes()
        await self.client.hset(name=key, mapping=data)

    async def get_similar_vectors(
        self,
        vector: list[float],
        top_k: int,
        score_threshold: int
    ) -> dict | None:
        vec_bytes = np.array(vector, dtype=np.float32).tobytes()

        query = (
            Query(f"*=>[KNN {top_k} @embedding $vec AS score]")
            .sort_by("score")
            .return_fields("q", "answer", "score")
            .paging(0, top_k)
            .dialect(2)
        )

        res = await self.client.ft("qa_vectors").search(query, query_params={"vec": vec_bytes})
        if res.total > 0:
            score = float(res.docs[0].score)
            if score <= score_threshold:
                doc = res.docs[0]
                return {
                    "id": doc.id,
                    "q": doc.q if hasattr(doc, "q") else None,
                    "answer": doc.answer if hasattr(doc, "answer") else None,
                    "score": score
                }

        return None
