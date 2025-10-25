from src.infrastructure.dto.base import BaseDTO


class ContextRequestDTO(BaseDTO):
    source_id: int
    context: str


class ContextDTO(BaseDTO):
    source_id: int
