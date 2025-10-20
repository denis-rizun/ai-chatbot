from sqlalchemy.orm import DeclarativeBase

from src.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class BaseModel(DeclarativeBase, IDMixin, TimestampMixin):

    def to_dict(self) -> dict:
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            result[column.name] = value

        return result
