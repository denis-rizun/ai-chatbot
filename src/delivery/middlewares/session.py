from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.infrastructure.database.repositories.manager import RepositoryManager
from src.infrastructure.database.sessions import PostgresSession, RedisSession


class DBSessionMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        session = PostgresSession.initialize()
        async with session() as conn:
            request.state.repository = RepositoryManager.get_repository(
                session=conn,
                client=RedisSession.init()
            )
            return await call_next(request)
