from fastapi import APIRouter

from src.infrastructure.dto.health import HealthCheckSchema

router = APIRouter(tags=["health"])


@router.get(path="/", response_model=HealthCheckSchema)
async def health() -> HealthCheckSchema:
    return HealthCheckSchema()
