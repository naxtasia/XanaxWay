import requests

class NexaClient:
    BASE_URL = "https://api-lyricalabs.vercel.app/api/nexaforxanax"
    MODELS = [
        "nexa-5.0-preview",
        "nexa-3.7-pro",
        "nexa-5.0-intimate",
        "nexa-6.1-infinity",
        "gpt-5-mini-chatgpt",
        "nexa-6.1-code-llm"
    ]

    def __init__(self, token: str):
        self.token = token

    def list_models(self):
        return self.MODELS

    def generate_text(self, prompt: str, model: str = "nexa-5.0-preview"):
        if model not in self.MODELS:
            raise ValueError(f"Model bulunamadı! Mevcut modeller: {self.MODELS}")
        url = f"{self.BASE_URL}?prompt={prompt}&model={model}&token={self.token}"
        res = requests.get(url)
        return res.json()
