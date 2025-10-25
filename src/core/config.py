from functools import cached_property
from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config(BaseSettings):
    model_config = ConfigDict(env_file=BASE_DIR / ".env")

    PROJECT_NAME: str = "AI-Chatbot"
    VERSION: str = "1.0.0"
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    ENABLE_LOGGER: bool = True
    COMPOSE_PROJECT_NAME: str = "ai-chatbot"

    API_INNER_PORT: int = 8000
    API_OUTER_PORT: int = 8000
    API_WORKERS_AMOUNT: int = 1

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ai-chatbot"
    POSTGRES_HOST: str = "database"
    INNER_POSTGRES_PORT: int = 5432
    OUTER_POSTGRES_PORT: int = 5432

    REDIS_HOST: str = "cache"
    INNER_REDIS_PORT: int = 6379
    OUTER_REDIS_PORT: int = 6379
    REDIS_USER: str = "redis"
    REDIS_PASSWORD: str = "redis"

    CHATGPT_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    @cached_property
    def postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.INNER_POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    @cached_property
    def alembic_postgres_url(self) -> str:
        return (
            f"postgresql://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.INNER_POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )


config = Config()
