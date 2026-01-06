import requests

class NexaClient:
    BASE_URL = "https://api-lyricalabs.vercel.app/v4/llm/nexa/generative/model/completions"
    MODELS = [
        "nexa-5.0-preview",
        "nexa-3.7-pro",
        "nexa-5.0-intimate",
        "nexa-6.1-infinity",
        "gpt-5-mini-chatgpt",
        "nexa-6.1-code-llm", 
        "nexa-7.0-express"
    ] 

    def __init__(self, token: str):
        self.token = token

    def list_models(self):
        """Mevcut modelleri listeler"""
        return self.MODELS

    def generate_text(self, prompt: str, model: str = "nexa-5.0-preview",
                      temperature: float = 0.6, max_tokens: int = 4096,
                      top_p: float = 0.95, frequency_penalty: float = 0.2,
                      presence_penalty: float = 0.1, custom_system_instruction: str = ""):
        """Nexa API ile metin üretir"""
        if model not in self.MODELS:
            raise ValueError(f"Model bulunamadı! Mevcut modeller: {self.MODELS}")

        payload = {
            "token": self.token,
            "prompt": prompt,
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "custom_system_instruction": custom_system_instruction
        }

        headers = {"Content-Type": "application/json"}
        res = requests.post(self.BASE_URL, json=payload, headers=headers)
        res.raise_for_status()  # HTTP hatalarında exception fırlatır
        return res.json()
