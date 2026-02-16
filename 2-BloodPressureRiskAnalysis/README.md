# Blood Pressure Risk Analysis with KMeans  
(KMeans ile Tansiyon Risk Analizi)

This project analyzes daily blood pressure measurements and classifies days as **Risky** or **Normal** using an unsupervised machine learning approach.  
(Bu proje günlük tansiyon ölçümlerini analiz eder ve gözetimsiz makine öğrenmesi yöntemi kullanarak günleri **Riskli** veya **Normal** olarak sınıflandırır.)

Blood pressure data is read from an Excel file, processed, and clustered with **KMeans** to identify higher-risk patterns based on morning and evening measurements.  
(Tansiyon verileri bir Excel dosyasından okunur, işlenir ve sabah–akşam ölçümlerine göre yüksek riskli desenleri belirlemek için **KMeans** ile kümelenir.)

---

## 📌 Features (Özellikler)

- Reads blood pressure data from an Excel file  
  (Excel dosyasından tansiyon verilerini okur)
- Splits systolic and diastolic values (e.g. `120/80`)  
  (Sistolik ve diyastolik değerleri ayırır)
- Uses **KMeans clustering** to group days into risk categories  
  (Günleri risk kategorilerine ayırmak için **KMeans kümeleme** kullanır)
- Automatically determines the risky cluster  
  (Riskli kümeyi otomatik olarak belirler)
- Labels each day as **Risky** or **Normal**  
  (Her günü **Riskli** veya **Normal** olarak etiketler)
- Exports the results to a new Excel file  
  (Sonuçları yeni bir Excel dosyasına aktarır)

---

## 📂 Input Data Format (Girdi Veri Formatı)

The input Excel file (`tansiyon.xlsx`) should contain the following columns:  
(Girdi Excel dosyası (`tansiyon.xlsx`) aşağıdaki sütunları içermelidir:)

- `Date` (Tarih)
- `Morning Blood Pressure` (Sabah Tansiyonu – örn. `120/80`)
- `Evening Blood Pressure` (Akşam Tansiyonu – örn. `130/85`)

---

## 🧠 Methodology (Yöntem)

1. Blood pressure values are parsed into systolic and diastolic components  
   (Tansiyon değerleri sistolik ve diyastolik bileşenlerine ayrılır)
2. Four features are used for clustering:  
   (Kümeleme için dört özellik kullanılır:)
   - Morning systolic (Sabah sistolik)
   - Morning diastolic (Sabah diyastolik)
   - Evening systolic (Akşam sistolik)
   - Evening diastolic (Akşam diyastolik)
3. KMeans is applied with **2 clusters**  
   (KMeans **2 küme** olacak şekilde uygulanır)
4. The cluster with the higher average systolic values is labeled as **Risky**  
   (Ortalama sistolik değeri daha yüksek olan küme **Riskli** olarak etiketlenir)
5. Results are merged back into the original dataset  
   (Sonuçlar orijinal veri setine eklenir)

---

## 📤 Output (Çıktı)

- Daily risk classification printed to the console  
  (Günlük risk durumu konsola yazdırılır)
- A new Excel file (`tansiyon_sonuc.xlsx`) containing:  
  (Aşağıdaki bilgileri içeren yeni bir Excel dosyası oluşturulur:)
  - Original data (Orijinal veriler)
  - Risk label for each day (Her gün için risk etiketi)

---

## 🛠️ Technologies Used (Kullanılan Teknolojiler)

- Python (3.10.11)
- Pandas
- NumPy
- Scikit-learn

---
## 📌 Project Note (Proje Notu)

This project was created as part of guided learning through online resources  
and adapted to analyze personal blood pressure data using KMeans clustering  
for educational purposes.

(Bu proje, çevrim içi kaynaklar eşliğinde yapılan rehberli öğrenme sürecinin  
bir parçası olarak geliştirilmiş ve kişisel tansiyon verileri üzerinde  
KMeans kümeleme yöntemi uygulanacak şekilde uyarlanmıştır.)

## ⚠️ Disclaimer (Uyarı)

This project is for educational and experimental purposes only
and should not be used for medical diagnosis.

(Bu proje eğitim ve deneysel amaçlıdır
ve tıbbi tanı amacıyla kullanılmamalıdır.)
---
## ▶️ How to Run (Çalıştırma)

```bash
pip install -r requirements.txt
python app.py
