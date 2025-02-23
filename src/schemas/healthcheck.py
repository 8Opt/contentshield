from pydantic import BaseModel, Field

from src.common.utils.utils import datetime_now


class HealtcheckInfo(BaseModel):
    ip: str
    created_at: int = Field(..., default_factory=datetime_now)
