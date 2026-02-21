import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

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
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

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

# Save file
df.to_csv("data/weather_data.csv", index=False)

print("Data saved successfully!")
