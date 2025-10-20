from src.domain.enums.common import StatusEnum
from src.infrastructure.dto.base import BaseDTO


class HealthCheckDTO(BaseDTO):
    status: int = 200
    message: StatusEnum = StatusEnum.OK
