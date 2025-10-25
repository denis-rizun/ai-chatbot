from src.infrastructure.dto.base import BaseDTO


class HealthCheckDTO(BaseDTO):
    message: str = "I am alive!"
