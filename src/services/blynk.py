
from time import time, sleep

import BlynkLib
from src.config import (
    BLYNK_AUTH_TOKEN,
    TEMP_HIGH_THRESHOLD,
    HUMIDITY_HIGH_THRESHOLD
)

from sense_hat import SenseHat

#initialise SenseHAT
sense = SenseHat()
sense.clear()

if not BLYNK_AUTH_TOKEN:
    raise ValueError("BLYNK_AUTH_TOKEN not found in .env file")

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Time in seconds before process times out / shuts down
INACTIVITY_TIMEOUT = 30
last_activity = time()


if __name__ == "__main__":
    print("Blynk application started.")

    try:
        while True:
            blynk.run()

            temperature = round(sense.get_temperature(), 1)
            humidity = round(sense.get_humidity(), 1)

            temp_alert = 1 if temperature > TEMP_HIGH_THRESHOLD else 0
            humidity_alert = 1 if humidity > HUMIDITY_HIGH_THRESHOLD else 0

            blynk.virtual_write(1, temperature)
            blynk.virtual_write(2, humidity)
            blynk.virtual_write(3, temp_alert)
            blynk.virtual_write(4, humidity_alert)
            

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