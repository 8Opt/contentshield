from .._search import beam_search

class ALICE(object):
    def __init__(self, language_model, classifier, mode, device="cpu"):
        self.classifier = classifier
        self.language_model = language_model
        self.device = device
        self.mode = mode

    def __call__(self, prompt):
        return self.generate(prompt)

    def generate(self, prompt):
        if self.mode == "neutral":
            flag = 0
        else:
            flag = 1
        return beam_search(prompt, self.language_model, self.classifier, flag, self.device)
