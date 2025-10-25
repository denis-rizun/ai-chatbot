from fastapi import APIRouter, Request

from src.application.ai.mini_lm import MiniLMModel
from src.application.embedding import EmbeddingService
from src.application.pipelines.add_context.embedding import GenerateEmbeddingStep
from src.application.pipelines.add_context.split import SplitTextStep
from src.application.pipelines.pipeline import Pipeline
from src.delivery.helper import APIHelper
from src.infrastructure.dto.context import ContextRequestDTO, ContextDTO
from src.infrastructure.dto.response import ResponseDTO

router = APIRouter(prefix="/contexts", tags=["context"])


@router.post(path="", response_model=ResponseDTO[ContextDTO])
async def add_context(request: Request, body: ContextRequestDTO) -> ResponseDTO:
    steps = [
        SplitTextStep(),
        GenerateEmbeddingStep(EmbeddingService(request.state.repository, ai_model=MiniLMModel())),
    ]
    pipeline = Pipeline(steps)
    res = await pipeline.run(body.model_dump())
    return APIHelper.unified_response(ContextDTO(source_id=res["source_id"]), code=201)
