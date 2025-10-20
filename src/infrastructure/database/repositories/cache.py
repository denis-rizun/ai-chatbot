from typing import Any

from redis.asyncio import Redis

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
