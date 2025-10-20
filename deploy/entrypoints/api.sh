#!/bin/sh

set -e
cd /app

if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

exec uvicorn src.main:app \
    --host 0.0.0.0 \
    --port "${API_INNER_PORT}" \
    --workers "${API_WORKERS_AMOUNT}"
