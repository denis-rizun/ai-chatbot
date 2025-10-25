from fastapi import APIRouter

from src.delivery.helper import APIHelper
from src.domain.entities.pipelines.context import Context
from src.infrastructure.di.dependencies import ContextPipelineDI
from src.infrastructure.dto.context import ContextRequestDTO, ContextDTO
from src.infrastructure.dto.response import ResponseDTO

router = APIRouter(prefix="/contexts", tags=["context"])


@router.post(path="", response_model=ResponseDTO[ContextDTO])
async def add_context(body: ContextRequestDTO, pipeline: ContextPipelineDI) -> ResponseDTO:
    entity = Context.build(body.model_dump())
    response = await pipeline.run(entity)
    response = ContextDTO.build(response)
    return APIHelper.unified_response(response, code=201)
