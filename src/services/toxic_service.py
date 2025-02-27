from src.services.base import BaseSerivce


class ToxicDetectService(BaseSerivce):
    def __init__(self):
        super().__init__()
        # Cache for storing previous results
        self.cache = {}
    
    async def inference(self, sentences):
        if isinstance(sentences, str):
            sentences = [sentences]
            
        results = []
        uncached = []
        
        # Check cache first
        for sentence in sentences:
            if sentence in self.cache:
                results.append(self.cache[sentence])
            else:
                uncached.append(sentence)
        
        # Only process sentences not in cache
        if uncached:
            new_results = await super().inference(uncached)
            # Update cache with new results
            for sent, result in zip(uncached, new_results):
                self.cache[sent] = result
            results.extend(new_results)
            
        return results
