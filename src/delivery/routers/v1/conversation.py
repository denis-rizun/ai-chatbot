from fastapi import APIRouter

from src.delivery.helper import APIHelper
from src.domain.entities.pipelines.inference import Inference
from src.infrastructure.di.container import container
from src.infrastructure.di.dependencies import ConversationPipelineDI
from src.infrastructure.dto.conversation import ConversationDTO, ConversationQueryDTO
from src.infrastructure.dto.response import ResponseDTO

router = APIRouter(prefix="/conversations", tags=["conversation"])


@router.post(path="", response_model=ResponseDTO[ConversationDTO])
async def ask(body: ConversationQueryDTO, pipeline: ConversationPipelineDI) -> ResponseDTO:
    entity = Inference.build(body.model_dump())
    response = await pipeline.run(entity)
    response = ConversationDTO.build(response)
    return APIHelper.unified_response(response)
