# ============================================
# EARTHQUAKE ANALYSIS PROJECT (TURKEY)
# Data Source: USGS API
# ============================================

import os                    # For outputs
import requests              # For API requests
import pandas as pd          # Data manipulation
import matplotlib.pyplot as plt  # Basic plotting
import seaborn as sns        # Statistical visualization
import folium                # Interactive maps
from datetime import datetime, timedelta
from folium.plugins import HeatMap  # Heatmap visualization


# ============================================
# 1) DATA COLLECTION FROM USGS API
# ============================================

# Define time range (Last 1 Year)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# USGS Earthquake API endpoint
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# API parameters (Turkey bounding box)
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

# Send request to API
response = requests.get(url, params=params)
data = response.json()

# Extract earthquake records
features = data["features"]

records = []
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

# Convert to DataFrame
df = pd.DataFrame(records)

print("Total earthquakes:", df.shape[0])


# ============================================
# 2) DATA CLEANING & FILTERING
# ============================================

# Keep only earthquakes inside Turkey
df = df[df["location"].str.contains("Turkey")]
print("Only Turkey earthquakes:", df.shape[0])

# Extract city name from location string
df["city"] = df["location"].str.split("of ").str[-1]
df["city"] = df["city"].str.replace(", Turkey", "", regex=False)


# ============================================
# 3) DATA VISUALIZATION
# ============================================

os.makedirs("screenshots", exist_ok=True)

# Magnitude distribution
plt.figure(figsize=(8,6))
sns.histplot(df['magnitude'], bins=20, kde=True)
plt.title("Magnitude Distribution (Last 1 Year)")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.savefig("screenshots/1-magnitude-distribution.png")
plt.show()

# Magnitude vs Depth relationship
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='depth', y='magnitude')
plt.title("Magnitude vs Depth")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.savefig("screenshots/2-depth-vs-magnitude.png")
plt.show()


# ============================================
# 4) MONTHLY EARTHQUAKE TREND
# ============================================

# Group earthquakes by month
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


# ============================================
# 5) TOP 10 MOST ACTIVE CITIES
# ============================================

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


# ============================================
# 6) INTERACTIVE EARTHQUAKE MAP
# ============================================

# Create base map centered on Turkey
m = folium.Map(location=[39,35], zoom_start=6)

# Add circle markers for each earthquake
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['magnitude'] * 2,
        popup=f"{row['location']}<br>Mag:{row['magnitude']}<br>Depth:{row['depth']} km",
        color='red' if row['magnitude'] >= 5 else 'blue',
        fill=True
    ).add_to(m)

os.makedirs("outputs", exist_ok=True)
m.save("outputs/Earthquake_map.html")
print("Map created successfully.")


# ============================================
# 7) HEATMAP (EARTHQUAKE DENSITY)
# ============================================

# Prepare data for heatmap (Latitude, Longitude, Magnitude as weight)
heat_data = [[row['latitude'], row['longitude'], row['magnitude']] 
             for _, row in df.iterrows()]

heat_map = folium.Map(location=[39,35], zoom_start=6)

HeatMap(heat_data, radius=15).add_to(heat_map)

heat_map.save("outputs/Earthquake_heatmap.html")

print("Heatmap created successfully.")
