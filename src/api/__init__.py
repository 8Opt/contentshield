from fastapi import APIRouter

from src.api.routers import toxic_router

api_routers = APIRouter(prefix="/api/v1")

api_routers.include_router(toxic_router, prefix="toxic", tags=["TOXIC_DETECT"])
