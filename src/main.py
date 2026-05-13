from time import sleep, monotonic
from datetime import datetime
from random import uniform
import csv
from pathlib import Path
import BlynkLib
from sense_hat import SenseHat

from src.config import (
    BLYNK_AUTH_TOKEN,
    TEMP_HIGH_THRESHOLD,
    HUMIDITY_HIGH_THRESHOLD,
)

from src.services.weather_api import get_outdoor_weather

sense = SenseHat()
sense.clear()

if not BLYNK_AUTH_TOKEN:
    raise ValueError("BLYNK_AUTH_TOKEN not found in .env file")

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

CSV_FILE = Path("sensor_log.csv")

# Set details for Newbridge 
LATITUDE = 53.180385646267816
LONGITUDE = -6.798848036455396

# Refresh outdoor weather every 10 minutes
WEATHER_REFRESH_SECONDS = 600

# Wind alert threshold in km/h
WIND_ALERT_THRESHOLD = 30

def ensure_csv_exists():
    if not CSV_FILE.exists():
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "sensor_mode",
                "indoor_temp_c",
                "indoor_humidity_percent",
                "temp_status",
                "humidity_status",
                "outdoor_temp_c",
                "outdoor_humidity_percent",
                "rain_mm",
                "wind_kmh",
                "rain_status",
                "wind_status",
            ])


SIMULATE_SENSOR = False

def read_sensor_data():
    if SIMULATE_SENSOR:
        temperature = round(uniform(15, 40), 1)
        humidity = round(uniform(21, 80), 1)
    else:
        temperature = round(sense.get_temperature(), 1)
        humidity = round(sense.get_humidity(), 1)
    return temperature, humidity


def check_alerts(temperature, humidity):
    temp_alert = 1 if temperature > TEMP_HIGH_THRESHOLD else 0
    humidity_alert = 1 if humidity > HUMIDITY_HIGH_THRESHOLD else 0
    return temp_alert, humidity_alert

def check_weather_alerts(rain_now, wind_speed):
    rain_alert = 1 if rain_now is not None and rain_now > 0 else 0
    wind_alert = 1 if wind_speed is not None and wind_speed > WIND_ALERT_THRESHOLD else 0
    weather_warning = 1 if rain_alert or wind_alert else 0
    return rain_alert, wind_alert, weather_warning

def update_blynk(temperature, humidity, temp_alert, humidity_alert, outdoor_temperature, outdoor_humidity, rain_alert, wind_alert):
    blynk.virtual_write(1, temperature)
    blynk.virtual_write(2, humidity)
    blynk.virtual_write(3, temp_alert)
    blynk.virtual_write(4, humidity_alert)
    blynk.virtual_write(5, outdoor_temperature if outdoor_temperature is not None else 0)
    blynk.virtual_write(6, outdoor_humidity if outdoor_humidity is not None else 0)    
    blynk.virtual_write(7, rain_alert)
    blynk.virtual_write(8, wind_alert)    


def update_led_status(temp_alert, humidity_alert, rain_alert, wind_alert):
    if temp_alert and humidity_alert:
        sense.clear(255, 0, 255)   # purple
    elif temp_alert:
        sense.clear(255, 0, 0)     # red
    elif humidity_alert:
        sense.clear(255, 255, 0)   # yellow
    elif rain_alert or wind_alert:
        sense.clear(0, 0, 255)     # blue
    else:
        sense.clear(0, 255, 0)     # green

def log_to_csv(
    temperature,
    humidity,
    temp_alert,
    humidity_alert,
    outdoor_temperature,
    outdoor_humidity,
    rain_now,
    wind_speed,
    rain_alert,
    wind_alert,
):

    sensor_mode = "simulated" if SIMULATE_SENSOR else "real"

    temp_status = "HIGH" if temp_alert else "OK"
    humidity_status = "HIGH" if humidity_alert else "OK"
    rain_status = "RAIN" if rain_alert else "CLEAR"
    wind_status = "WIND RISK" if wind_alert else "OK"

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sensor_mode,
            temperature,
            humidity,
            temp_status,
            humidity_status,
            outdoor_temperature,
            outdoor_humidity,
            rain_now,
            wind_speed,
            rain_status,
            wind_status,
        ])

if __name__ == "__main__":
    print("Blynk application started.")
    ensure_csv_exists()
    outdoor_temperature = None
    outdoor_humidity = None
    rain_now = None
    wind_speed = None
    next_weather_refresh = 0
    
    try:
        while True:
            blynk.run()

            temperature, humidity = read_sensor_data()
            temp_alert, humidity_alert = check_alerts(temperature, humidity)

            now = monotonic()
            if now >= next_weather_refresh:
                weather = get_outdoor_weather(LATITUDE, LONGITUDE)
                outdoor_temperature = weather.get("outdoor_temperature")
                outdoor_humidity = weather.get("outdoor_humidity")
                rain_now = weather.get("rain_now")
                wind_speed = weather.get("wind_speed")
                next_weather_refresh = now + WEATHER_REFRESH_SECONDS

            rain_alert, wind_alert, weather_warning  = check_weather_alerts(rain_now, wind_speed)


            if temp_alert:
                print(f"WARNING: Temperature above limit ({TEMP_HIGH_THRESHOLD} C)")

            if humidity_alert:
                print(f"WARNING: Humidity above limit ({HUMIDITY_HIGH_THRESHOLD}%)")

            if rain_alert:
                print(f"WARNING: Rain detected outside")

            if wind_alert:
                print(f"WARNING: High wind detected outside ({wind_speed} km/h)")    

            update_blynk(temperature, humidity, temp_alert, humidity_alert, outdoor_temperature, outdoor_humidity, rain_alert, wind_alert)
            update_led_status(temp_alert, humidity_alert, rain_alert, wind_alert)
            log_to_csv(
                temperature,
                humidity,
                temp_alert,
                humidity_alert,
                outdoor_temperature,
                outdoor_humidity,
                rain_now,
                wind_speed,
                rain_alert,
                wind_alert,
           ) 
            
            print(
                f"Indoor Temp: {temperature} C | "
                f"Indoor Humidity: {humidity} % | "
                f"Temp alert: {temp_alert} | "
                f"Humidity alert: {humidity_alert} | "
                f"Outdoor Temp: {outdoor_temperature} C | "
                f"Outdoor Humidity: {outdoor_humidity} % | "
                f"Rain now: {rain_now} | "
                f"Wind speed: {wind_speed} km/h | "
                f"Rain alert: {rain_alert} | "
                f"Wind alert: {wind_alert} | "
            )

            sleep(2)

    except KeyboardInterrupt:
        print("Blynk application stopped.")
        sense.clear()