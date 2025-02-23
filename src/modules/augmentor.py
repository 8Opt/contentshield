import torch

from src.modules.searching import beam_search


class Augmentor:
    def __init__(self, language_model, classifier, mode: int, device: str = "auto"):
        self.classifier = classifier
        self.language_model = language_model
        if device == "auto":
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        self.mode = mode

    def __call__(self, prompt: str):
        return self.generate(prompt)

    def generate(self, prompt: str):
        if self.mode == "neutral":
            flag = 0
        else:
            flag = 1
        return beam_search(
            prompt, self.language_model, self.classifier, flag, self.device
        )
