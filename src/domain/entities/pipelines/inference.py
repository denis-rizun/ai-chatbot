from dataclasses import dataclass
from typing import Self, Any


@dataclass
class InferenceMeta:
    is_finished: bool = False
    is_cached: bool = False


@dataclass
class InferenceInternal:
    embeddings: list[float] | None = None
    similar: str | None = None


@dataclass
class Inference:
    question: str
    source_id: int

    answer: str | None
    metadata: InferenceMeta
    internal: InferenceInternal

    message: str | None

    @classmethod
    def build(cls, data: dict[str, Any]) -> Self:
        return cls(
            question=data["question"],
            source_id=data["source_id"],
            answer=None,
            metadata=InferenceMeta(),
            internal=InferenceInternal(),
            message=None,
        )
