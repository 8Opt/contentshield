from abc import ABC, abstractmethod
from typing import Any, Union, Tuple, Dict

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from contentshield.tools.text_processing import clean
from contentshield.model_catalog import TRANSLATION_CONFIG

class BaseTranslator(ABC): 

    def __init__(self, 
                 from_lang:Union[str, None] =None, 
                 to_lang:str ='en', 
                 auto_clean:bool=False): 
        
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.auto_clean = auto_clean

    @abstractmethod
    def translate(self, text:str) -> str: 
        raise NotImplementedError
    

class GoogleTranslator(BaseTranslator):

    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        try: 
            from googletrans import Translator

            if from_lang is None: 
                from_lang = 'auto'
            self.from_lang = from_lang
            self.translator = Translator()
        except ValueError: 
            raise ValueError('`googletrans` is not installed. Please try `pip install googletrans`')
    
    def translate(self, text: str) -> str:
        result = self.__call__(text)
        return result
    
    def __call__(self, text):
        if self.auto_clean: 
            text = clean(text)
        result = self.translator.translate(text, dest=self.to_lang, src=self.from_lang).text
        assert type(result) == str
        return result
    

class Translator(BaseTranslator):

    def __init__(self, from_lang='vi', to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        try: 
            from translate import Translator

            if from_lang is None: 
                from_lang = 'autodetect'
            self.from_lang = from_lang

            self.translator = Translator(from_lang=self.from_lang, to_lang=self.to_lang)
        except ValueError: 
            raise ValueError('`translate` is not installed. Please try `pip install translate`')
        
    def translate(self, text: str) -> str:
        result = self.__call__(text)
        return result
    
    def __call__(self, text):
        if self.auto_clean: 
            text = clean(text)
        result = self.translator.translate(text)
        assert type(result) == str
        return result
    

class PTMTranslator(BaseTranslator): 

    def __init__(self, model_id, llm_config):
        super().__init__()

        if llm_config: 
            self.llm_config = llm_config
        else: 
            self.llm_config = TRANSLATION_CONFIG

        try: 
            if model_id: 
                self.tokenizer, self.model = self.call_pretrained(model_id)
        except ValueError: 
            raise ValueError("`model_id` is in wrong format, which means that either it is not ")
        
    def translate(self, text: str) -> str:
        input_ids = self.tokenizer(text, return_tensors="pt")["input_ids"]
        outputs = self.__call__(input_ids)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result
    

    def __call__(self, input_ids) -> Any:
        outputs = self.model.generate(input_ids, **self.llm_config)
        return outputs
    

    def call_pretrained(self, model_id) -> Tuple[AutoTokenizer, AutoModelForSeq2SeqLM]: 
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id).eval()
        return (tokenizer, model)  
    

