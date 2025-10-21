from fastapi import APIRouter, Request

from src.application.ai.mini_lm import MiniLMModel
from src.application.embedding import EmbeddingService
from src.application.pipelines.add_context.embedding import GenerateEmbeddingStep
from src.application.pipelines.add_context.split import SplitTextStep
from src.application.pipelines.pipeline import Pipeline
from src.infrastructure.dto.context import ContextRequestDTO, ContextResponseDTO

router = APIRouter(prefix="/context", tags=["context"])


@router.post(path="", response_model=ContextResponseDTO)
async def add_context(request: Request, ctx: ContextRequestDTO) -> ContextResponseDTO:
    steps = [
        SplitTextStep(),
        GenerateEmbeddingStep(EmbeddingService(request.state.repository, ai_model=MiniLMModel())),
    ]
    pipeline = Pipeline(steps)
    res = await pipeline.run(ctx.model_dump())
    return ContextResponseDTO(source_id=res["source_id"])
