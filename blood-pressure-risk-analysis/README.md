# tansiyon risk analizi

Bu projede günlük tansiyon verilerini analiz edip günleri riskli veya normal olarak ayırmaya çalıştım.

Makine öğrenmesinde gözetimsiz öğrenme tarafını görmek için yaptım.  
Verileri excel dosyasından okuyup KMeans ile kümelendirdim.

Genel mantık:
Veriyi oku -> değerleri ayır -> kümelendir -> risk durumunu belirle

---

Kullandığım veri:

Yapay veri seti, Excel dosyasında sabah ve akşam tansiyon değerleri var.

Örnek:
120/80, 130/85 gibi değerleri alıp sistolik ve diyastolik olarak ayırdım.

---

Projede yaptığım şeyler:

Sabah ve akşam tansiyonlarını ayrı ayrı işledim

Toplamda:
sabah sistolik, sabah diyastolik / akşam sistolik, akşam diyastolik olacak şekilde 4 veri kullandım
Daha sonra KMeans ile verileri 2 kümeye ayırdım

Ortalama tansiyonu daha yüksek olan kümeyi: "Riskli"  
diğerini ise: "Normal" olarak etiketledim

---

Sonuç olarak:
Her gün için risk durumu oluşturuluyor ve yeni bir excel dosyasına kaydediliyor. Konsolda da sonuçlar görünüyor

---

Kullandığım teknolojiler:

python 3.10, pandas, numpy, scikit-learn

---

Not:
Bu proje tamamen öğrenme amaçlı yapıldı gerçek bir medikal analiz sistemi değil. Ayrıca KMeans mantığını daha iyi anlamak için geliştirdim

---

Çalıştırmak için:

pip install -r requirements.txt

python app.py