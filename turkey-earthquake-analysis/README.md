# Türkiye Deprem Analizi

Bu projede usgs api'den türkiye'deki son 1 yılın deprem verilerini çektim.  
Çok profesyonel bir şey değil, daha çok veriyle uğraşmak için yaptım.

Veriyi çektikten sonra biraz temizledim, sonra grafiklere döktüm, en son da harita üzerinde göstermeye çalıştım.
Akış şu şekilde:
Veriyi çek -> Düzenle -> Grafiklere dök -> Görselleştir

---

Kullandığım veri kaynağı:
https://earthquake.usgs.gov/

Filtreler:
son 1 yıl  
2.0 üstü depremler  
türkiye civarı koordinatlar

---

Grafik kısmı şu şekilde:

Deprem büyüklüklerine baktım  
hangi büyüklükte daha çok deprem var diye histogram çizdim

Derinlik vs büyüklük  
burada açıkçası net bir şey çıkmadı ama scatter plot attım görmek için

Aylık deprem sayısı  
zamanla artıyor mu azalıyor mu diye kontrol ettim

En çok deprem olan şehirler  
ilk 10'u çıkardım, bazı isimler biraz saçma gelebilir çünkü veri direkt apiden geliyor

---

Harita kısmı şu şekilde:

Folium ile
her depremi noktaya çevirdim.
büyüklüğe göre boyut verdim.
5 üstünü kırmızı yaptım.
Yoğunluk nerede bakmak için heatmap denedim.

---

Kullandılan teknolojiler:  
python 3.10, pandas, matplotlib, seaborn, folium

---

Not:
Bu proje tamamen deneme amaçlı  
gerçek bir analiz falan değil, sadece veriyle uğraşmak için yaptım

---

Çalıştırmak için:

pip install -r requirements.txt  
python main.py

Çıktı olarak grafikler ve html haritalar oluşuyor
