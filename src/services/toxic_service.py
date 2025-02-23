from src.services.base import BaseSerivce


class ToxicDetectService(BaseSerivce):
    async def inference(self, sentence):
        return super().inference(sentence)
