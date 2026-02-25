import requests
from typing import List, Dict, Any, Optional

class aiClient:
    BASE_URL = "https://api.xanaxway.com/v4/generative/model/completions"

    def __init__(self, token: str):
        self.token = token

    def generate(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        top_p: float = 0.9,
        stream: bool = False
    ) -> Dict[str, Any]:
        
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": messages,
            "generation_config": {
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": top_p
            },
            "stream": stream
        }

        try:
            response = requests.post(self.BASE_URL, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "Error",
                "message": str(e),
                "raw_response": getattr(response, 'text', '')
            }
