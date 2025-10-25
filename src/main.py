from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import config
from src.delivery.exception_handlers import ExceptionHandler
from src.delivery.routers.health import router as health
from src.delivery.routers.v1.context import router as context
from src.delivery.routers.v1.conversation import router as conversation

app = FastAPI(root_path="/api", title=config.PROJECT_NAME, version=config.VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)

app.include_router(health)
app.include_router(context)
app.include_router(conversation)

ExceptionHandler.register(app)
