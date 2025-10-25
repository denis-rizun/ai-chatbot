from src.domain.enums.response import ResponseStatusEnum
from src.infrastructure.dto.base import BaseDTO
from src.infrastructure.dto.context import ContextDTO
from src.infrastructure.dto.conversation import ConversationDTO


class ResponseDTO(BaseDTO):
    status_code: int
    status: ResponseStatusEnum
    message: str | None
    response: ContextDTO | ConversationDTO | None

