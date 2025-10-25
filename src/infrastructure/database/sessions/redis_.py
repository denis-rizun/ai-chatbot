from redis.asyncio import Redis, ConnectionPool
from src.core.config import config


class RedisSession:
    client: Redis | None = None

    @classmethod
    def init(cls) -> Redis:
        if cls.client is None:
            pool = ConnectionPool(
                host=config.REDIS_HOST,
                port=config.INNER_REDIS_PORT,
                decode_responses=True,
                max_connections=20
            )
            cls.client = Redis(connection_pool=pool, password="redis123")

        return cls.client
