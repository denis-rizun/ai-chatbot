from fastapi import FastAPI
from fastapi.requests import Request
from starlette.responses import JSONResponse

from src.core.exceptions import CustomException
from src.domain.enums.response import ResponseStatusEnum
from src.infrastructure.dto.response import ResponseDTO


class ExceptionHandler:
    FAILED_STATUS = ResponseStatusEnum.FAILURE

    @classmethod
    def register(cls, app: FastAPI) -> None:

        @app.exception_handler(CustomException)
        async def custom_exception_handler(request: Request, exc: CustomException) -> None:  # noqa
            body = cls._unified_body(exc)
            return JSONResponse(content=body.model_dump(), status_code=exc.status_code)

    @classmethod
    def _unified_body(cls, exc: CustomException) -> ResponseDTO:
        return ResponseDTO(
            status_code=exc.status_code,
            status=cls.FAILED_STATUS,
            response=None,
            message=str(exc.message)
        )
