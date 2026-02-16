from flask import Flask, render_template, request
import os
import contextlib

# Google Gemini loglarını gizlemek için
with open(os.devnull, 'w') as devnull, contextlib.redirect_stderr(devnull):
    import google.generativeai as genai


# Flask uygulaması
app = Flask(__name__)

# API KEY (Environment Variable üzerinden)
# Windows için:
# setx GEMINI_API_KEY "API_KEY_BURAYA"
# Mac/Linux:
# export GEMINI_API_KEY="API_KEY_BURAYA"

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY ortam değişkeni bulunamadı!")

genai.configure(api_key=API_KEY)

# Model ayarları
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain"
}

# Gemini modeli
model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    generation_config=generation_config
)

# Kurumsal bilgiler (Prompt)
corporate_text = """
Aşağıda "Zengin Business" için hazırlanmış kurumsal işletme bilgileri ve kuralları yer almaktadır.
Bu metin; çalışma saatleri, kurs içerikleri, fiyatlandırma ve iletişim bilgilerini kapsar.
Tüm cevaplar bu bilgiler esas alınarak verilmelidir.

──────────────────────────────
ZENGİN BUSINESS – KURUMSAL BİLGİLER

1. İşletme Tanımı
Zengin Business, eğitim alanında faaliyet gösteren kurumsal bir eğitim kuruluşudur.
Amacı, bireylere yazılım, teknoloji ve bilişim alanlarında temel ve orta seviye bilgi kazandırmaktır.
Kurslar hem teorik hem de uygulamalı içeriklerden oluşur.

2. Çalışma Saatleri ve Günleri
Çalışma Saatleri: 07:00 – 17:00
Çalışma Günleri: Pazartesi – Cuma
Hafta sonları ve resmi tatillerde hizmet verilmemektedir.

3. Sunulan Kurslar ve Fiyatlar
- Python Programlama Kursu: 199 TL
- Web Tasarım Kursu: 199 TL
- Siber Güvenlik (Hacking) Kursu: 199 TL
- CMD (Komut Satırı) Kodlama Kursu: 129 TL

4. Adres Bilgisi
Kütahya / Tavşanlı
Define Sokak No:24 Daire:2

──────────────────────────────
YANITLAMA TALİMATLARI

- Kullanıcıya her zaman müşteri gibi hitap et.
- Sorulan soru bu metinde geçiyorsa, ilgili kısmı mutlaka alıntı yaparak belirt.
- Cevapları işletme sahibi veya yetkili temsilci gibi ver.
- Samimi ama kurumsal bir dil kullan.
- Gerektiğinde uygun emojiler kullan 😊
- Bu metin dışında bilgi uydurma veya tahmin yürütme.
"""

# Sohbet oturumu
chat_session = model.start_chat(history=[])

# Sohbet geçmişi
conversation = [
    {"sender": "Sistem", "message": "Zengin Business sohbet sistemine hoş geldiniz."}
]


@app.route("/", methods=["GET", "POST"])
def chat():
    global conversation

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        if not user_input:
            return render_template("chat.html", conversation=conversation)

        if user_input.lower() in ["exit", "quit", "çıkış"]:
            conversation.append({
                "sender": "Sistem",
                "message": "Sohbet sonlandırıldı."
            })
            return render_template("chat.html", conversation=conversation)

        # Kullanıcı mesajı
        conversation.append({
            "sender": "Müşteri",
            "message": user_input
        })

        # Model girdisi
        prompt = corporate_text + "\n\nSoru: " + user_input

        response = chat_session.send_message(prompt)

        # Model cevabı
        conversation.append({
            "sender": "Zengin Business",
            "message": response.text
        })

    return render_template("chat.html", conversation=conversation)


if __name__ == "__main__":
    app.run(debug=True)
