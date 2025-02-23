from pydantic import BaseModel, Field

from src.common.utils.utils import datetime_now



class ToxicRequest(BaseModel):
    sentence: str
    model: str
    toxicity_rate: float = Field(default=0.75, description="Set by client")
    created_at: int = Field(..., default_factory=datetime_now)


class ToxicResponse(BaseModel): 
    sentence: str
    model: str
    is_toxic: bool
    toxicity_rate: float = Field(description="Return by Model")
    created_at: int = Field(..., default_factory=datetime_now)
    elapsed_time: int