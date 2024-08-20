from abc import ABC, abstractmethod

class BaseToxicDetector(ABC): 

    @abstractmethod
    def detect(self, content):
        raise NotImplementedError