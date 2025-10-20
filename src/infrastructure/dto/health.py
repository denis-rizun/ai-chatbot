from src.infrastructure.dto.base import BaseSchema


class HealthCheckSchema(BaseSchema):
    status: int = 200
    message: str = 'ok'
