from src.services.base import BaseSerivce


class ToxicDetectService(BaseSerivce):
    async def inference(self, sentences):
        return super().inference(sentences)
