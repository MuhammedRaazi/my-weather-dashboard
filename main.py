import requests
import pandas as pd
from datetime import datetime
import os

api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    raise ValueError("API key not found!")

cities = [
    "Chennai",
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Kolkata",
    "Pune",
    "Jaipur",
    "Ahmedabad",
    "Kochi",
]

data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather = response.json()

        city_data = {
            "City": city,
            "Temperature_C": round(weather["main"]["temp"] - 273.15, 2),
            "Feels_Like_C": round(weather["main"]["feels_like"] - 273.15, 2),
            "Humidity": weather["main"]["humidity"],
            "Pressure": weather["main"]["pressure"],
            "Wind_Speed": weather["wind"]["speed"],
            "Weather_Description": weather["weather"][0]["description"],
            "Timestamp": datetime.now(),
        }

        data.append(city_data)

    except Exception as e:
        print(f"Error fetching data for {city}: {e}")

# Create DataFrame
df = pd.DataFrame(data)

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Feature Engineering

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Temp_Diff"] = df["Temperature_C"] - df["Feels_Like_C"]

df["Comfort_Level"] = df["Temperature_C"].apply(
    lambda x: "Cool" if x < 20 else "Moderate" if x <= 30 else "Hot"
)

df["Wind_Category"] = df["Wind_Speed"].apply(
    lambda x: "Calm" if x < 2 else "Breezy" if x <= 5 else "Windy"
)

df["Hour"] = df["Timestamp"].dt.hour
df["Date"] = df["Timestamp"].dt.date


# Save file
df.to_csv(
    "data/weather_data.csv",
    mode="a",
    header=not os.path.exists("data/weather_data.csv"),
    index=False,
)

print("Data saved successfully!")
