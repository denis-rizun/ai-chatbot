from dataclasses import dataclass
from typing import Any, Self


@dataclass
class ContextInternal:
    chunks: list[str] | None = None
    embeddings: list[float] | None = None


@dataclass
class Context:
    source_id: int
    content: str

    internal: ContextInternal

    @classmethod
    def build(cls, data: dict[str, Any]) -> Self:
        return cls(
            source_id=data["source_id"],
            content=data["content"],
            internal=ContextInternal()
        )
