# src/main.py
from time import sleep
from random import uniform
from services.weather_api import get_outdoor_weather

def read_simulated_sensor():
    return {
        "temperature": round(uniform(18, 28), 1),
        "humidity": round(uniform(40, 70), 1),
    }


if __name__ == "__main__":
    while True:
        reading = read_simulated_sensor()
        weather = get_outdoor_weather(53.1819, -6.7967)
       
        print(reading)
        print("Outdoor weather:", weather)
       
        sleep(5)


