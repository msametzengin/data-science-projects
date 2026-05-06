import os  # dosya işlemleri
import requests  # api isteği atmak için
import pandas as pd  # veri işlemleri
import matplotlib.pyplot as plt  # grafik
import seaborn as sns  # daha güzel grafik
import folium  # harita
from datetime import datetime, timedelta
from folium.plugins import HeatMap  # heatmap


# Veri çekme (son 1 yıl)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# türkiye sınırlarını verme
params = {
    "format": "geojson",
    "starttime": start_date.strftime("%Y-%m-%d"),
    "endtime": end_date.strftime("%Y-%m-%d"),
    "minmagnitude": 2.0,
    "minlatitude": 35,
    "maxlatitude": 43,
    "minlongitude": 25,
    "maxlongitude": 45
}

# apiye istek atıp json olarak alma
response = requests.get(url, params=params)
data = response.json()

features = data["features"]

records = []

# gelen json içinden ihtiyacımız olanları çekme
for feature in features:
    prop = feature["properties"]
    geo = feature["geometry"]["coordinates"]
    
    records.append({
        "date": pd.to_datetime(prop["time"], unit="ms"),
        "magnitude": prop["mag"],
        "depth": geo[2],
        "latitude": geo[1],
        "longitude": geo[0],
        "location": prop["place"]
    })

# dataframe'e çevirme
df = pd.DataFrame(records)

print("Total earthquakes:", df.shape[0])



# Veri temizleme

# sadece türkiye içindekileri alma (api bazen geniş dönebiliyor)
df = df[df["location"].str.contains("Turkey")]
print("Only Turkey earthquakes:", df.shape[0])

# şehir bilgisini string içinden ayıklama
df["city"] = df["location"].str.split("of ").str[-1]
df["city"] = df["city"].str.replace(", Turkey", "", regex=False)



# Görselleştirme işlemleri

# çıktı klasörü oluşturma
os.makedirs("screenshots", exist_ok=True)

# büyüklük dağılımı
plt.figure(figsize=(8,6))
sns.histplot(df['magnitude'], bins=20, kde=True)
plt.title("Magnitude Distribution (Last 1 Year)")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.savefig("screenshots/1-magnitude-distribution.png")
plt.show()

# derinlik vs büyüklük ilişkisi
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='depth', y='magnitude')
plt.title("Magnitude vs Depth")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.savefig("screenshots/2-depth-vs-magnitude.png")
plt.show()

# tarihleri aylık gruplama
df['month'] = df['date'].dt.to_period('M')
monthly_counts = df.groupby('month').size()

plt.figure(figsize=(10,6))
monthly_counts.plot(kind='line')
plt.title("Monthly Earthquake Trend")
plt.xlabel("Month")
plt.ylabel("Number of Earthquakes")
plt.savefig("screenshots/3-monthly-earthquake-trend.png")
plt.xticks(rotation=45)
plt.show()

# en çok deprem olan ilk 10 şehir
top_cities = df['city'].value_counts().head(10)

print("\nTop 10 Most Active Cities:")
print(top_cities)

plt.figure(figsize=(10,6))
top_cities.plot(kind='bar')
plt.title("Top 10 Most Active Cities")
plt.xlabel("City")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=45)
plt.savefig("screenshots/4-top-10-active-cities.png")
plt.show()



# Harita

# türkiye ortasına harita açma
m = folium.Map(location=[39,35], zoom_start=6)

# her deprem için nokta ekleme
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['magnitude'] * 2,  # büyüklüğe göre boyut
        popup=f"{row['location']}<br>Mag:{row['magnitude']}<br>Depth:{row['depth']} km",
        color='red' if row['magnitude'] >= 5 else 'blue',  # büyükler kırmızı
        fill=True
    ).add_to(m)

os.makedirs("outputs", exist_ok=True)
m.save("outputs/Earthquake_map.html")

print("Map created successfully.")

# Heatmap(yoğunluk haritası)

# heatmap için veri formatı hazırlama
heat_data = [[row['latitude'], row['longitude'], row['magnitude']] 
             for _, row in df.iterrows()]

heat_map = folium.Map(location=[39,35], zoom_start=6)

# yoğunluk haritası ekleme
HeatMap(heat_data, radius=15).add_to(heat_map)

heat_map.save("outputs/Earthquake_heatmap.html")

print("Heatmap created successfully.")