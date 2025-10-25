from starlette.responses import JSONResponse

from src.domain.enums.response import ResponseStatusEnum
from src.infrastructure.dto.base import BaseDTO
from src.infrastructure.dto.response import ResponseDTO


class APIHelper:

    @staticmethod
    def unified_response(data: BaseDTO, code: int = 200) -> ResponseDTO:
        unified_body = ResponseDTO(
            status_code=code,
            status=ResponseStatusEnum.SUCCESS,
            response=data,
            message=None
        )

        return JSONResponse(
            content=unified_body.model_dump(),
            status_code=code
        )
