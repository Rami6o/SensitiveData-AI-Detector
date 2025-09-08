# SensitiveData-AI-Detector

Python tabanlı, regex + yapay zeka destekli hassas veri sızıntısı tespit aracı.

## 🚀 Özellikler
- 📌 Regex tabanlı hızlı tarama
- 🤖 Derin öğrenme tabanlı hassas veri modeli
- 📊 HTML & JSON raporlama
- 🐳 Docker desteği
- ✅ Unit test entegrasyonu (pytest)

## 🔧 Kurulum

```bash
git clone https://github.com/<KullaniciAdiniz>/SensitiveData-AI-Detector.git
cd SensitiveData-AI-Detector
pip install -r requirements.txt
```

## ▶️ Kullanım

```bash
python main.py --file test.txt
```

## 🧪 Test Çalıştırma

```bash
pytest tests/
```

## 📦 Docker ile Çalıştırma

```bash
docker build -t sensitive-detector .
docker run -it sensitive-detector --file test.txt
```

## 📌 Yol Haritası
- [ ] API desteği
- [ ] Web arayüzü
- [ ] Gerçek zamanlı log tarama
