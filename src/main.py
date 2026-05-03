from time import sleep

import BlynkLib
from sense_hat import SenseHat

from src.config import (
    BLYNK_AUTH_TOKEN,
    TEMP_HIGH_THRESHOLD,
    HUMIDITY_HIGH_THRESHOLD,
)

sense = SenseHat()
sense.clear()

if not BLYNK_AUTH_TOKEN:
    raise ValueError("BLYNK_AUTH_TOKEN not found in .env file")

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)


def read_sensor_data():
    temperature = round(sense.get_temperature(), 1)
    humidity = round(sense.get_humidity(), 1)
    return temperature, humidity


def check_alerts(temperature, humidity):
    temp_alert = 1 if temperature > TEMP_HIGH_THRESHOLD else 0
    humidity_alert = 1 if humidity > HUMIDITY_HIGH_THRESHOLD else 0
    return temp_alert, humidity_alert


def update_blynk(temperature, humidity, temp_alert, humidity_alert):
    blynk.virtual_write(1, temperature)
    blynk.virtual_write(2, humidity)
    blynk.virtual_write(3, temp_alert)
    blynk.virtual_write(4, humidity_alert)


def update_led_status(temp_alert, humidity_alert):
    if temp_alert and humidity_alert:
        sense.clear(255, 0, 255)   # purple
    elif temp_alert:
        sense.clear(255, 0, 0)     # red
    elif humidity_alert:
        sense.clear(255, 255, 0)   # yellow
    else:
        sense.clear(0, 255, 0)     # green


if __name__ == "__main__":
    print("Blynk application started.")

    try:
        while True:
            blynk.run()

            temperature, humidity = read_sensor_data()
            temp_alert, humidity_alert = check_alerts(temperature, humidity)

            if temp_alert:
                print(f"WARNING: Temperature above limit ({TEMP_HIGH_THRESHOLD} C)")

            if humidity_alert:
                print(f"WARNING: Humidity above limit ({HUMIDITY_HIGH_THRESHOLD}%)")

            update_blynk(temperature, humidity, temp_alert, humidity_alert)
            update_led_status(temp_alert, humidity_alert)

            print(
                f"Temperature: {temperature} C | "
                f"Humidity: {humidity} % | "
                f"Temp alert: {temp_alert} | "
                f"Humidity alert: {humidity_alert}"
            )

            sleep(2)

    except KeyboardInterrupt:
        print("Blynk application stopped.")
        sense.clear()