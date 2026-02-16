# XanaxWay AI GateWay Python Kütüphanesi

**XanaxWay** tarafından geliştirilen geniş veri LLM modellerine erişim sağlayan Python kütüphanesidir. Bu kütüphane ile **yapay zeka modellerini kolayca kullanabilir** ve metin üretimi, kod analizi gibi senaryolarda hızlıca entegre edebilirsiniz.

---

## 📦 Kurulum

```bash
pip install xanaxway

```
---

🔑 API Token Alma

Kütüphaneyi kullanmak için **API** token’a ihtiyacınız var:

1. [XanaxWay Dashboard](https://xanaxway.com/auth) adresine girin


2. GitHub/X/Google/Spotify hesaplarınızın birisi ile kayıt olun veya giriş yapın


3. Dashboard’dan [API](https://xanaxway.com/dashboard) token’ınızı alın




---

🚀 Hızlı Başlangıç
```python
from xanaxway import aiClient

# API token'ınız ile client oluşturun
client = aiClient(token="API_TOKENİNİZ")

# Örnek prompt ve parametreler
prompt = "Python'da yapay zeka uygulamaları nasıl geliştirilir?"

response = client.generate(
    prompt=prompt,
    model="nexa-7.0-express",      # Hızlı yanıt modeli
    temperature=0.6,               # Yaratıcılık seviyesi
    max_tokens=500,                # Üretilecek maksimum token
    top_p=0.95,                    # Çeşitlilik kontrolü
    frequency_penalty=0.2,         # Tekrar cezası
    presence_penalty=0.1,          # Yeni konu ödülü
    custom_system_instruction="Cevapları Türkçe ve samimi ver."  # Opsiyonel sistem talimatı
)

if response.get("basarilimi"):
    print("✅ Yanıt:\n", response.get("output"))
else:
    print("❌ Hata oluştu:")
    print(response.get("message"))
    print("Raw response:", response.get("raw_response"))
```

---

📚 Mevcut Modeller

[Modeller sayfasına bakarak modellerin limitlerini ve hangi üyelikleri desteklediklerini görün.](https://docs.xanaxway.com/models/supported-models) 

**XanaxWay** hazır modelleri sunmak ile kalmayıp, kendi modellerinide sunabiliyor, _Nexa ve Wiggly_ modellerinide kullanabilirsiniz. 


---
"""

---

🔍 Model Bilgisi Alma
```python
# Tüm modelleri açıklamalarıyla listeleyin
models = client.list_models(with_descriptions=True)
for model, desc in models.items():
    print(f"{model}: {desc}")

# Belirli bir model hakkında detaylı bilgi
model_info = client.get_model_info("nexa-7.0-insomnia")
print(f"""
Model: {model_info['name']}
Açıklama: {model_info['description']}
Kategori: {model_info['category']}
""")
```


---

❓ Sık Sorulan Sorular

1. API token’ımı nasıl alırım?
XanaxWay platformundan kayıt olun ve Dashboard'dan token oluşturun.


2. Hangi modeli kullanmalıyım?

Genel kullanım: nexa-5.0-preview

Duygusal içerik: nexa-7.0-insomnia

Kod yazma: nexa-6.1-code-llm

Hızlı yanıt: nexa-7.0-express



3. Rate limit var mı?
- Evet, üyelik tipine göre değişir. Dashboard’dan kontrol edin.




---

📞 Destek ve İletişim

Website: https://xanaxway.com

Nexa API Docs: https://docs.xanaxway.com

Email: xanaxway@gmail.com

GitHub Issues: Sorun bildirin





---

