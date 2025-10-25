from typing import Annotated

from fastapi import Depends

from src.application.pipelines.pipeline import Pipeline
from src.infrastructure.di.factory import Factory

ContextPipelineDI = Annotated[Pipeline, Depends(Factory.get_context_pipeline)]
ConversationPipelineDI = Annotated[Pipeline, Depends(Factory.get_conversation_pipeline)]
