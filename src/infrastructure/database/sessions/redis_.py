from redis.asyncio import Redis, ConnectionPool
from src.core.config import config


class RedisSession:
    MAX_CONNECTION_AMOUNT = 20
    CLIENT: Redis | None = None

    @classmethod
    def init(cls) -> Redis:
        if cls.CLIENT is None:
            pool = ConnectionPool(
                host=config.REDIS_HOST,
                port=config.INNER_REDIS_PORT,
                username=config.REDIS_USER,
                password=config.REDIS_PASSWORD,
                decode_responses=True,
                max_connections=cls.MAX_CONNECTION_AMOUNT
            )
            cls.CLIENT = Redis(connection_pool=pool)

        return cls.CLIENT
