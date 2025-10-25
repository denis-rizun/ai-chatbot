from typing import Self

from src.domain.entities.pipelines.inference import Inference
from src.infrastructure.dto.base import BaseDTO


class ConversationQueryDTO(BaseDTO):
    source_id: int
    question: str


class ConversationDTO(BaseDTO):
    source_id: int
    question: str

    answer: str

    @classmethod
    def build(cls, data: Inference) -> Self:
        return cls(
            question=data.question,
            source_id=data.source_id,
            answer=data.answer,
        )
