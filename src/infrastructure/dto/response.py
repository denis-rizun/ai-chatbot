from typing import Generic

from src.domain.enums.response import ResponseStatusEnum
from src.domain.types import DTOType
from src.infrastructure.dto.base import BaseDTO


class ResponseDTO(BaseDTO, Generic[DTOType]):
    status_code: int
    status: ResponseStatusEnum
    message: str | None
    response: DTOType | None
