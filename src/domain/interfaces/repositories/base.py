from abc import ABC, abstractmethod
from typing import Generic, Any, Literal

from src.domain.enums.common import FindByEnum
from src.domain.types import ModelType


class IBaseRepository(ABC, Generic[ModelType]):
    MODEL: type[ModelType]

    @abstractmethod
    async def get_by_extended(
        self,
        filters: dict[FindByEnum, Any],
        many: bool = False,
        order_by: FindByEnum | None = None,
        order_by_type: Literal["asc", "desc"] | None = None,
        limit: int | None = None,
        unique: bool = False,
        options: list[Any] | None = None
    ) -> ModelType | list[ModelType] | None:
        pass

    @abstractmethod
    async def create(self, is_flush: bool = False, **data) -> ModelType | None:
        pass
