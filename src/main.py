from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import config
from src.delivery.middlewares.session import DBSessionMiddleware
from src.delivery.routers.health import router as health

app = FastAPI(root_path="/api", title=config.PROJECT_NAME, version=config.VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)
app.add_middleware(DBSessionMiddleware)

app.include_router(health)