# Earthquake Data Analysis & Interactive Mapping (Turkey)

This project analyzes real-time earthquake data in Turkey using the USGS public API.
It performs statistical analysis, time-series trend evaluation, and interactive geographic mapping.

The project demonstrates real-world API integration, structured data transformation, exploratory data analysis (EDA), and geospatial visualization using Python.

---

## 📡 Data Source

Earthquake data is retrieved dynamically from:

USGS (United States Geological Survey) Earthquake API
https://earthquake.usgs.gov/

The analysis covers:
 - Last 1 year of earthquake activity
 - Minimum magnitude threshold: 2.0
 - Turkey geographic bounding box
    -Latitude: 35 – 43
    -Longitude: 25 – 45

All data is fetched in GeoJSON format and processed dynamically at runtime.

---

## 📊 Analyses Performed

### 1️⃣ Magnitude Distribution
- Histogram with KDE
- Frequency analysis of earthquake magnitudes
- Identification of magnitude concentration patterns
### 2️⃣ Depth vs Magnitude Analysis
- Scatter plot showing relationship between depth and magnitude
- Visual inspection of potential correlation between depth and strength
### 3️⃣ Monthly Trend Analysis
- Number of earthquakes per month
- Time-based seismic activity tracking
- Time-series aggregation using date-period transformation
### 4️⃣ Top 10 Most Active Cities
- Earthquake frequency ranking by city
- Identification of regional seismic hotspots

---

## 🗺️ Interactive Map Visualization

### Standard Map
- Circle markers for each earthquake
- Marker size proportional to magnitude
- Color-coded by severity (Red ≥ 5.0, Blue < 5.0)
- Interactive popups displaying location, magnitude, and depth

### Heatmap
- Density-based visualization
- Magnitude-weighted intensity
- Identifies seismic clusters and activity concentration zones

---

## 🧠 Technical Highlights

- REST API integration using requests
- JSON parsing and structured data extraction
- Data cleaning and filtering using Pandas
- Time-series grouping with .dt.to_period()
- Statistical visualization with Matplotlib and Seaborn
- Interactive geospatial visualization using Folium
- Heatmap generation with folium.plugins.HeatMap

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Folium
- Requests

---

## ⚠️ Disclaimer

This project is developed for educational and analytical purposes only.
It is not intended for official seismic risk assessment, governmental decision-making, or emergency planning.

---

## ▶️ Usage

Install required libraries:

pip install -r requirements.txt

Run the script:

python main.py

The project generates:
- Statistical plots (PNG format)
- Earthquake_map.html (Interactive earthquake map)
- Earthquake_heatmap.html (Interactive density heatmap)

## 🇹🇷 Türkçe Açıklama

Bu proje, USGS API kullanılarak Türkiye’deki deprem verilerinin dinamik olarak çekilmesini, temizlenmesini, analiz edilmesini ve interaktif harita üzerinde görselleştirilmesini amaçlamaktadır.

Proje kapsamında:
- API entegrasyonu
- Veri temizleme ve dönüştürme
- Zaman serisi analizi
- İstatistiksel görselleştirme
- Coğrafi yoğunluk haritalaması uygulanmıştır.