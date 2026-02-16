# Heart Attack Risk Prediction  
(Kalp Krizi Risk Tahmini)

This project aims to predict heart disease (heart attack) risk using real-world medical data and basic machine learning techniques.  
(Bu proje, gerçek tıbbi veriler kullanılarak temel makine öğrenmesi teknikleri ile **kalp hastalığı (kalp krizi) riski tahmini** yapmayı amaçlamaktadır.)

A simple Artificial Neural Network (ANN) model is trained after data preprocessing, class balancing with SMOTE, and feature scaling.  
(Veri ön işleme, SMOTE ile sınıf dengeleme ve ölçeklendirme sonrası basit bir **Yapay Sinir Ağı (ANN)** modeli eğitilmiştir.)

Model performance is also compared with other machine learning algorithms.  
(Ayrıca model performansı diğer makine öğrenmesi algoritmaları ile karşılaştırılmıştır.)

The project allows users to enter their own data via the terminal and receive a risk prediction.  
(Proje, kullanıcıların terminal üzerinden kendi verilerini girerek risk tahmini almasına olanak tanır.)

---

## 📌 Project Description (Proje Açıklaması)

- Predicts heart attack risk using machine learning  
  (Makine öğrenmesi kullanarak kalp krizi riski tahmini yapar)
- Uses SMOTE to handle class imbalance  
  (Sınıf dengesizliğini gidermek için SMOTE kullanır)
- Trains an ANN-based classification model  
  (ANN tabanlı bir sınıflandırma modeli eğitir)
- Compares ANN with: (ANN diğer modeller ile karşılaştırıldı)
  - Random Forest  
  - Decision Tree  
  - Logistic Regression  
- Supports user input from the terminal  
  (Terminal üzerinden kullanıcı girdisi ile tahmin yapılabilir)

---

## 📊 Dataset / Veri Seti

**Heart Failure Prediction Dataset**

- Source / Kaynak:  
  https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

This dataset is publicly available and used for educational purposes only.  
(Bu veri seti herkese açık olup yalnızca eğitim ve analiz amaçlı kullanılmıştır.)

---

## 🧠 Methodology (Yöntem)

1. Dataset is loaded and preprocessed  
   (Veri seti yüklenir ve ön işleme tabi tutulur)
2. Categorical features are encoded  
   (Kategorik değişkenler sayısal hale getirilir)
3. Data is split into training and testing sets  
   (Veri eğitim ve test setlerine ayrılır)
4. Class imbalance is handled using SMOTE  
   (SMOTE ile sınıf dengesizliği giderilir)
5. Features are scaled using StandardScaler  
   (Özellikler StandardScaler ile ölçeklendirilir)
6. ANN model is trained  
   (Yapay sinir ağı modeli eğitilir)
7. User input is taken from the terminal for prediction  
   (Tahmin için terminalden kullanıcı verisi alınır)

---

## 🛠️ Technologies / Kullanılan Teknolojiler

- Python (3.10.11)
- NumPy
- Pandas
- Scikit-learn
- Imbalanced-learn (SMOTE)
- TensorFlow / Keras
- Matplotlib

---
## 📌 Project Note (Proje Notu)

This project was developed by following an online machine learning course  
and further customized for learning and practice purposes.  
The implementation was modified, analyzed, and documented by the author  
to better understand the applied methods.

(Bu proje bir çevrim içi makine öğrenmesi kursu takip edilerek geliştirilmiş,  
öğrenme ve pratik amacıyla tarafımdan düzenlenmiş, analiz edilmiş  
ve dokümante edilmiştir.)

## ⚠️ Disclaimer (Uyarı)

This project is for educational and experimental purposes only
and should not be used for medical diagnosis or clinical decision-making.

(Bu proje eğitim ve deneysel amaçlıdır
ve tıbbi tanı veya klinik karar verme amacıyla kullanılmamalıdır.)

## ▶️ Usage / Kullanım

Install required libraries (Gerekli kütüphaneleri yükleyin):
```bash
pip install -r requirements.txt
