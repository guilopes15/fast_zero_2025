#!/bin/sh

poetry run alembic upgrade head

poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero_2025.app:app

# chmod +x entrypoint.sh