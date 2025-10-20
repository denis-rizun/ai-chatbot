FROM python:3.13-slim

RUN useradd -m -s /bin/bash chat-bot

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY src/ /app/src/
COPY .env /app/.env
COPY .dockerignore /app/.dockerignore

USER chat-bot

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8001"]
