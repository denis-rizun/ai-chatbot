from fastapi import APIRouter

from src.infrastructure.dto.health import HealthCheckDTO

router = APIRouter(tags=["health"])


@router.get(path="/", response_model=HealthCheckDTO)
async def health() -> HealthCheckDTO:
    return HealthCheckDTO()
