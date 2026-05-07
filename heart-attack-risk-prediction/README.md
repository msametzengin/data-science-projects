# Kalp krizi risk tahmini

Bu projede makine öğrenmesi kullanarak kalp krizi risk tahmini yapmaya çalıştım. Gerçek bir veri seti kullandım ve birkaç farklı modeli karşılaştırdım. Profesyonel bir medikal sistem değil, daha çok machine learning pratiği yapmak için geliştirdim.

Genel mantık:
Veriyi hazırla -> modeli eğit -> tahmin yap

---

Kullandığım veri seti:
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

---

Projede yaptığım şeyler:

Veriyi temizledim ve düzenledim. Kategorik verileri sayısal hale çevirdim. Veriyi train/test verisi olarak ayırdım. Veri dengesiz olduğu için SMOTE kullandım çünkü model tek tarafa fazla kayıyordu. Daha sonra verileri scale edip modeli eğittim. Ana model olarak basit bir ANN kullandım. Ve diğer modellerle (Random forest, Decision tree, Logistic regression) karşılaştırdım.

---

Kullanıcı terminal üzerinden kendi verisini girip tahmin alabiliyor. Örneğin: yaş, tansiyon, kolesterol gibi bilgiler giriliyor. Model de risk tahmini yapıyor

---

Kullandığım teknolojiler:  
Python 3.10, pandas, numpy, scikit-learn, tensorflow / keras, matplotlib, smote

---

Not: Bu proje tamamen öğrenme amaçlı gerçek tıbbi kullanım için uygun değil. Ayrıca proje bir machine learning kursundan ilerleyerek geliştirildi. Ama kodları düzenleyip anlamaya çalıştım

---

Çalıştırmak için:

pip install -r requirements.txt

python main.py
