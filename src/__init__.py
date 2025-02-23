from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from src.api import api_routers
from src.core.config import settings
from src.core.setup_lifespan import lifespan


description_md = Path(__file__).parent / "README.md"

app = FastAPI(
    docs_url="/",
    lifespan=lifespan,
    openapi_url="/openapi.json",
    title=settings.APP,
    version="0.1.0",
    description=description_md.read_text(encoding="utf-8")
    if description_md.exists()
    else "",
)

app.include_router(api_routers)


@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    return FileResponse("openapi.yaml", media_type="text/yaml")
