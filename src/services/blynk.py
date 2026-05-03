
from time import time, sleep

import BlynkLib
from src.config import BLYNK_AUTH_TOKEN

if not BLYNK_AUTH_TOKEN:
    raise ValueError("BLYNK_AUTH_TOKEN not found in .env file")

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Time in seconds before process times out / shuts down
INACTIVITY_TIMEOUT = 30
last_activity = time()


@blynk.on("V0")  # type: ignore[misc]
def handle_v0_write(value):
    global last_activity
    button_value = value[0]
    last_activity = time()
    print(f"Current button value: {button_value}")


if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()
            now = time()

            if now - last_activity > INACTIVITY_TIMEOUT:
                print(f"No activity for {INACTIVITY_TIMEOUT} seconds. Exiting.")
                break

            sleep(0.1)
    except KeyboardInterrupt:
        print("Blynk application stopped.")