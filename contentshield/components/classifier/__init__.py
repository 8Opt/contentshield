import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from contentshield.core.config import PRETRAINED_CLASSIFIER


class HateSpeechClassifier:
    def __init__(self, model_path, tokenizer_path=None):
        """
        Initializes a hate speech classifier.

        Args:
            model_path: Path to the pre-trained model.
            tokenizer_path: Path to the pre-trained tokenizer. If not provided, it is set to model_path.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path or model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path
        ).eval()

    def __call__(self, input_ids):
        """Performs classification using input IDs."""
        outputs = self.model(input_ids)
        return outputs

    def invoke(self, text):
        """Classifies text using tokenizer and model."""
        input_ids = self.tokenizer(text, return_tensors="pt")["input_ids"]
        logits = self(input_ids).logits
        probs = torch.softmax(logits, dim=1)[:, 1]  # Probability of hate speech
        return probs.detach().numpy() * 100  # Return percentage


class HateBERT(HateSpeechClassifier):
    def __init__(self):
        model_path = PRETRAINED_CLASSIFIER.HateBERT
        super().__init__(model_path)


class ToxDectRoBERTa(HateSpeechClassifier):
    def __init__(self):
        model_path = PRETRAINED_CLASSIFIER.ToxDectRoBERTa
        super().__init__(model_path)
