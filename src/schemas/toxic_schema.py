from src.schemas.base import BaseIO


class ToxicRequest(BaseIO):
    model: str
    toxicity_rate: float = 0.75
    do_augment: bool = True
