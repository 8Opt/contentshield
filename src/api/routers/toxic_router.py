from fastapi import APIRouter, HTTPException

from src.services.toxic_service import ToxicDetectService
from src.schemas.toxic_schema import ToxicRequest, ToxicResponse

router = APIRouter()
toxic_detect_service = ToxicDetectService()

@router.post(
    "/",
    description="Detecting Toxicity of a Sentence",
    status_code=200,
    response_model=ToxicResponse,
)
async def toxicity_detect(req: ToxicRequest):
    resp = await toxic_detect_service.inference(sentences=req.sentences)
    if not resp.get("success"):
        raise HTTPException(status_code=422, detail=resp.get("detail"))
    return resp.get("data")


@router.get(
    '/info', 
    description="Healthcheck", 
    status_code=200,
    response_description="An IP address of the running service"
)
async def get_info(): 
    resp = await toxic_detect_service.info()
    if not resp.get("success"):
        raise HTTPException(status_code=422, detail=resp.get("detail"))
    return resp.get("data")
