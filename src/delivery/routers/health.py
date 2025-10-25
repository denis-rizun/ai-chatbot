from fastapi import APIRouter

from src.delivery.helper import APIHelper
from src.infrastructure.dto.health import HealthCheckDTO
from src.infrastructure.dto.response import ResponseDTO

router = APIRouter(tags=["health"])


@router.get(path="/", response_model=ResponseDTO[HealthCheckDTO])
async def health() -> ResponseDTO:
    return APIHelper.unified_response(HealthCheckDTO())
