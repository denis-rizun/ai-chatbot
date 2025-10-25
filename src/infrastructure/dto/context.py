from typing import Self

from src.domain.entities.pipelines.context import Context
from src.infrastructure.dto.base import BaseDTO


class ContextRequestDTO(BaseDTO):
    source_id: int
    content: str


class ContextDTO(BaseDTO):
    source_id: int

    @classmethod
    def build(cls, data: Context) -> Self:
        return cls(source_id=data.source_id)
