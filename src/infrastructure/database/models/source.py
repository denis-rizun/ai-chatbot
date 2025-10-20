from sqlalchemy.orm import Mapped

from src.infrastructure.database.models.base import BaseModel


class SourceModel(BaseModel):
    __tablename__ = "sources"

    url: Mapped[str]
