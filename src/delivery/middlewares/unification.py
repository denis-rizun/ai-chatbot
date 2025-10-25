from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from src.domain.enums.response import ResponseStatusEnum
from src.infrastructure.dto.response import ResponseDTO


class UnifiedResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)

        if hasattr(response, "body"):
            try:
                body = await response.body()

            except TypeError:
                body = response.body
        else:
            body = None

        status_code = response.status_code
        unified_body = ResponseDTO(
            status_code=status_code,
            status=ResponseStatusEnum.SUCCESS,
            response=body,
            message=None
        )

        return JSONResponse(
            content=unified_body.model_dump(),
            status_code=unified_body.status_code
        )
