import uvicorn

from src.core.config import settings

if __name__ == "__main__":
    match settings.ENVIRONMENT:
        case "dev":
            uvicorn.run(
                app="app:app", port=settings.PORT, reload=True, host=settings.HOST
            )
        case "prod":
            uvicorn.run(
                app="app:app", port=settings.PORT, reload=False, host=settings.HOST
            )
