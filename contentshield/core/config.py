from dataclasses import dataclass

import torch


@dataclass
class CONFIG:
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"


class PRETRAINED_CLASSIFIER:
    HateBERT: str = (
        "GroNLP/hateBERT"  # HateBERT files: https://huggingface.co/GroNLP/hateBERT
    )
    ToxDectRoBERTa: str = (
        "Xuhui/ToxDect-roberta-large"  # ToxDectRoBERTa files: https://huggingface.co/Xuhui/ToxDect-roberta-large
    )
