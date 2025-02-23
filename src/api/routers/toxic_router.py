from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post(
    "/",
    description="Đăng kí một đối tượng vào cơ sở dữ liệu Vector",
    status_code=201,
    response_model=object,
)
async def create_identity(req: object):
    resp = await object.create_identity(req=req)
    if not resp.get("success"):
        raise HTTPException(status_code=422, detail=resp.get("detail"))
    return resp.get("data")
