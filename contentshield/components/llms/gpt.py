import json
import requests

class GPT:
    def __init__(self, endpoint_url, api_key):
        self.api_key = api_key
        self.endpoint_url = endpoint_url

    def _prepare_payload(self, prompt, top_k, max_tokens):
        """Prepares the API request payload."""
        prompts = [p.replace("'", "").replace('"', "") for p in (prompt if isinstance(prompt, list) else [prompt])]
        return {
            "prompt": prompts,
            "max_tokens": max_tokens,
            "temperature": 0.9,
            "n": 1,
            "stream": False,
            "logprobs": top_k,
            "stop": ["<|endoftext|>", "\\n"],
        }

    def _make_api_request(self, payload):
        """Makes the API request and handles the response."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(self.endpoint_url, headers=headers, json=payload)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()

    def __call__(self, prompt, top_k=1, max_tokens=1):
        """Makes a GPT-3 API call and returns the full JSON response."""
        payload = self._prepare_payload(prompt, top_k, max_tokens)
        return self._make_api_request(payload)

    def generate_text(self, prompt, top_k=10, max_tokens=10):
        """Makes a GPT-3 API call and returns only the generated text."""
        response = self.__call__(prompt, top_k, max_tokens)
        try:
            return response["choices"][0]["text"]
        except (KeyError, IndexError) as e:
            print(f"Error parsing GPT-3 response: {e}, Response: {response}")
            return None # or raise the error, depending on your error handling strategy