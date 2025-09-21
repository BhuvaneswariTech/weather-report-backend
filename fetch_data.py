# fetch_data.py
import requests
import pandas as pd

def get_weather_data(lat=47.37, lon=8.55):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m,relative_humidity_2m"
        "&past_days=2"
    )

    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame({
        "timestamp": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"],
        "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    })

    return df
