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
    description="Service Health Status", 
    status_code=200,
    response_description="Service health status and basic information"
)
async def get_health_status(): 
    resp = await toxic_detect_service.info()
    if not resp.get("success"):
        raise HTTPException(status_code=422, detail=resp.get("detail"))
    
    # Only return minimal necessary info
    safe_data = {
        "status": "healthy" if resp.get("data") else "unhealthy",
        "version": resp.get("data", {}).get("version", "unknown")
    }
    return safe_data
