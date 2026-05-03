# src/services/weather_api.py
import requests

def get_outdoor_weather(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,rain",
        "hourly": "precipitation_probability",
        "forecast_days": 1
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    current = data.get("current", {})
    return {
        "outdoor_temperature": current.get("temperature_2m"),
        "outdoor_humidity": current.get("relative_humidity_2m"),
        "rain_now": current.get("rain"),
    }