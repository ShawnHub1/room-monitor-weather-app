
from time import time, sleep

import BlynkLib
from src.config import BLYNK_AUTH_TOKEN

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


@blynk.on("V1")  # type: ignore[misc]
def handle_v1_write(value):
    global last_activity
    button_value = value[0]
    last_activity = time()
    print(f"Current button value: {button_value}")

    if button_value=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()


if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()
            blynk.virtual_write(1,sense.temperature)  # Send temperature to virtual pin V0

            now = time()

            if now - last_activity > INACTIVITY_TIMEOUT:
                print(f"No activity for {INACTIVITY_TIMEOUT} seconds. Exiting.")
                break

            sleep(0.1)
    except KeyboardInterrupt:
        print("Blynk application stopped.")