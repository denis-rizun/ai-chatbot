from functools import cached_property
from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config(BaseSettings):
    PROJECT_NAME: str = "AI-Chatbot"
    VERSION: str = "1.0.0"
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    ENABLE_LOGGER: bool = True
    COMPOSE_PROJECT_NAME: str

    API_INNER_PORT: int
    API_OUTER_PORT: int
    API_WORKERS_AMOUNT: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    INNER_POSTGRES_PORT: int
    OUTER_POSTGRES_PORT: int

    REDIS_HOST: str
    INNER_REDIS_PORT: int
    OUTER_REDIS_PORT: int

    CHATGPT_API_KEY: str

    model_config = ConfigDict(env_file=BASE_DIR / ".env")

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
