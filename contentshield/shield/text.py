from typing import Union, Tuple, Dict

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
import torch


from contentshield.processor.pre_processing import clean
from contentshield.model_catalog import BINARY_CLASSIFIER, MULTI_CLASS_CLASSIFIER

class PretrainedClassifer(object): 

    def __init__(self, 
                 model_id:str, 
                 type:str,
                 **kwargs): 
    
        try: 
            if self.__valid_model(model_id=model_id, type=type): 
                self.tokeninzer, self.model = self.call_pretrained(model_id=model_id)
                
        except ValueError: 
            raise ValueError(f"Input `{model_id}` is not supported")

    def __call__(self, input_ids):
        with torch.no_grad():
          outputs = self.model(input_ids)
        return outputs
    
    def call_pretrained(self, model_id) -> Tuple[AutoTokenizer, AutoModelForSequenceClassification]: 
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSequenceClassification.from_pretrained(model_id).eval()

        return (tokenizer, model)  
    
    def classify(self, text, label:Union[Dict, None]=None) -> Dict: 
        result = {}

        text = clean(text=text)
        input_ids = self.tokenizer(text, return_tensors="pt")["input_ids"]
        logits = self.__call__(input_ids).logits

        result['is_toxic'] = logits.argmax().item()
        result['toxic_rate'] = 100*float(torch.softmax(logits, dim=1)[:, 1].detach().numpy())

        if label: 
            result['label'] = label[result['is_toxic']]

        return result
    
    def __valid_model(self, model_id, type:str='binary') -> bool: 
        match type: 
            case 'binary': 
                if model_id not in BINARY_CLASSIFIER: 
                    return False
                return True
            
            case 'multi-class': 
                if model_id not in MULTI_CLASS_CLASSIFIER: 
                    return False
                return True
