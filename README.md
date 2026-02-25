# XanaxWay AI GateWay Python Kütüphanesi

**XanaxWay** tarafından sunulan yüzlerce LLM modellerine erişim sağlayan Python kütüphanesidir. Bu kütüphane ile **yapay zeka modellerini kolayca kullanabilir** ve metin üretimi, kod analizi gibi senaryolarda hızlıca entegre edebilirsiniz.

---

## 📦 Kurulum

```bash
pip install xanaxway

```
---

🔑 API Token Alma

Kütüphaneyi kullanmak için **API** token’a ihtiyacınız var:

1. [XanaxWay Dashboard](https://xanaxway.com/auth/login) adresine girin


2. GitHub/X/Google/Spotify hesaplarınızın birisi ile kayıt olun veya giriş yapın


3. Dashboard’dan [API](https://xanaxway.com/dashboard) token’ınızı alın




---

🚀 Hızlı Başlangıç
```python
from xanaxway import aiClient

# API token'ınız ile client oluşturun
client = aiClient(token="API_TOKENİNİZ")

# Mesaj geçmişi formatında yapı (System ve User rolleri ile)
messages = [
    {"role": "system", "content": "Cevapları Türkçe ve samimi ver."},
    {"role": "user", "content": "Python'da yapay zeka uygulamaları nasıl geliştirilir?"}
]

# Yanıt üretme
response = client.generate(
    messages=messages,
    model="sambanova/deepseek-v3",  # Kullanmak istediğiniz model ismi
    temperature=0.7,               # Yaratıcılık seviyesi (0.0 - 1.0)
    max_tokens=1024,               # Üretilecek maksimum token sayısı
    top_p=0.9                      # Çeşitlilik kontrolü
)

# Yanıtı kontrol etme
if "choices" in response:
    content = response["choices"][0]["message"]["content"]
    print("✅ Yanıt:\n", content)
else:
    print("❌ Hata oluştu:")
    print(response.get("message"))

```

---

📚 Mevcut Modeller

[Modeller sayfasına bakarak modellerin limitlerini ve hangi üyelikleri desteklediklerini görün.](https://docs.xanaxway.com/models/supported-models) 

**XanaxWay** hazır modelleri sunmak ile kalmayıp, kendi modellerinide sunabiliyor, _Nexa, Alyx ve Wiggly_ modellerinide kullanabilirsiniz. 


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
model_info = client.get_model_info("alyx-ix")
print(f"""
Model: {model_info['name']}
Açıklama: {model_info['description']}
Kategori: {model_info['category']}
""")
```
###💡 İpucu: Sistem Talimatları (System Instructions)
​Eski sürümdeki custom_system_instruction parametresi yerine, artık messages listesinin en başına bir system rolü ekleyerek modelin davranışını belirleyebilirsiniz:
```python
messages = [
    {"role": "system", "content": "Sen bir yazılım uzmanısın. Sadece kod blokları ile cevap ver."},
    {"role": "user", "content": "Python ile ekrana 'Merhaba' yazdır."}
]
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

