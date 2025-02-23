#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -a
source .env
set +a

# Ensure required environment variables are set
if [[ -z "$ENVIRONMENT" || -z "$PORT" || -z "$HOST" ]]; then
  echo "Error: Required environment variables ENVIRONMENT, PORT, or HOST are not set."
  exit 1
fi

# Execute the FastAPI application
exec fastapi "$ENVIRONMENT" app/main.py --port "$PORT" --host "$HOST" --reload