from abc import ABC, abstractmethod

from src.core.config import settings
from src.schemas.healthcheck import HealtcheckInfo


class BaseSerivce(ABC):
    @abstractmethod
    async def inference(self, sentence: str | list[str]) -> str:
        raise NotImplementedError

    async def info(self) -> HealtcheckInfo:
        return HealtcheckInfo(ip=settings.HOST)
