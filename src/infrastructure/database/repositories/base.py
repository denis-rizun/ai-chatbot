from typing import Generic, Any, Literal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.enums.common import FindByEnum
from src.domain.interfaces.repositories.base import IBaseRepository
from src.domain.types import ModelType


class BaseRepository(IBaseRepository, Generic[ModelType]):
    MODEL: type[ModelType]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

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
        stmt = select(self.MODEL)

        if options:
            for opt in options:
                stmt = stmt.options(opt)

        for field, value in filters.items():
            column = getattr(self.MODEL, field.value)
            if isinstance(value, (list, tuple, set)):
                stmt = stmt.where(column.in_(value))
            else:
                stmt = stmt.where(column == value)

        if order_by:
            column = getattr(
                self.MODEL,
                order_by.value if hasattr(order_by, "value") else order_by
            )
            if order_by_type == "desc":
                stmt = stmt.order_by(column.desc())
            else:
                stmt = stmt.order_by(column.asc())

        if limit is not None:
            stmt = stmt.limit(limit)

        result = await self.session.execute(stmt)
        scalars = result.unique().scalars() if unique else result.scalars()
        return scalars.all() if many else scalars.first()

    async def create(self, is_flush: bool = False, **data) -> ModelType | None:
        model = self.MODEL(**data)
        self.session.add(model)
        if is_flush:
            await self.session.flush()
            return model

        return None
