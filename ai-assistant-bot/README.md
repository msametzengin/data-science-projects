# Zengin Chat – AI Destekli Kurumsal Chatbot

Bu proje, yapay zekâ destekli bir kurumsal sohbet uygulamasıdır.  
Flask web framework’ü ve Google Gemini API kullanılarak geliştirilmiştir.

Projenin amacı, generative AI modellerinin gerçek bir iş senaryosunda  
nasıl kullanılabileceğini öğrenmek ve uygulamaktır.

---

## 🚀 Proje Özeti

Zengin Chat, önceden tanımlanmış kurumsal bilgiler doğrultusunda
kullanıcı sorularını yanıtlayan bir chatbot sistemidir.

Sistem:
- Belirlenen işletme kurallarının dışına çıkmaz
- Kurumsal ve samimi bir dil kullanır
- Kullanıcıyla müşteri gibi iletişim kurar

Bu proje, öğrenme sürecinde geliştirilen bir **kişisel uygulama projesidir**.

---

## 🛠️ Kullanılan Teknolojiler

- Python
- Flask
- Google Gemini API
- HTML / CSS
- Jinja2 Template Engine

---

## ⚙️ Kurulum

1. Projeyi klonlayın:
```
git clone https://github.com/kullanici-adi/zengin-chat.git
cd zengin-chat
```
2. Gerekli kütüphaneyi yükleyin:
```
pip install google-generativeai flask
```
3. API anahtarını ortam değişkeni olarak tanımlayın:

Windows (PowerShell):
setx GEMINI_API_KEY="API_KEY_BURAYA"

Mac / Linux:
export GEMINI_API_KEY="API_KEY_BURAYA"

4. Uygulamayı çalıştırın:
```
python app.py
```
5. Tarayıcıdan açın:

http://127.0.0.1:5000

📸 Ekran Görüntüsü
"screenshots\chat.png" adlı dosyada örnek bir ekran görüntüsü bulunmaktadır.

🎯 Amaç ve Öğrenilenler

Bu proje ile:
 - Generative AI API entegrasyonu
 - Prompt tasarımı
 - Flask ile basit web uygulaması geliştirme
 - Kurumsal senaryo kurgulama
 - konularında pratik yapılmıştır.

📌 Not
Bu proje bir öğrenme çalışmasıdır ve eğitim sürecinde edinilen
bilgilerin pekiştirilmesi amacıyla geliştirilmiştir.
