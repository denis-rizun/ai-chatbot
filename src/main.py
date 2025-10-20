from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import config

app = FastAPI(root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)
