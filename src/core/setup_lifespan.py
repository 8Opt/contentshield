import os
from contextlib import asynccontextmanager

import tomli
import yaml
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def get_project_metadata():
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomli.load(f)  # Use tomllib.load(f) for Python >= 3.11
            project = data["project"]
            return {
                "title": project["name"].replace("-", " ").title().upper(),
                "version": project["version"],
                "description": project["description"],
            }
    except (FileNotFoundError, KeyError):
        return {
            "title": "metadata-poc",
            "version": "0.1.0",
            "description": "A microservice for building POC of Oryza Metadata",
        }


def write_openapi_yaml(schema: dict):
    with open("openapi.yaml", "w", encoding="utf-8") as f:
        yaml.dump(schema, f, sort_keys=False, allow_unicode=True)


metadata = get_project_metadata()


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Generate OpenAPI Schema
    openapi_schema = get_openapi(
        title=metadata["title"],
        version=metadata["version"],
        description=metadata["description"],
        routes=app.routes,
    )

    # Write OpenAPI YAML file
    write_openapi_yaml(openapi_schema)

    yield

    print("Shutting down the server")
