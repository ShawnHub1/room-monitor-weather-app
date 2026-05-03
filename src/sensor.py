from sense_hat import SenseHat
import time

from config import TEMP_HIGH_THRESHOLD, HUMIDITY_HIGH_THRESHOLD

# Define some colours
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialise Sense HAT
sense = SenseHat()
sense.clear()

def get_environmental_data():
    # Read sensor data
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    
    return temp, humidity


while True:
    # Get readings
    temp, humidity = get_environmental_data()
    
    # Check thresholds
    temp_alert = temp > TEMP_HIGH_THRESHOLD
    humidity_alert = humidity > HUMIDITY_HIGH_THRESHOLD

    # Print to command line
    print("Temp: {:.1f} C  Humidity: {:.1f}%".format(
        temp, humidity))
    
    if temp_alert:
        print(f"WARNING: Temperature is above limit ({TEMP_HIGH_THRESHOLD} C)")

    if humidity_alert:
        print(f"WARNING: Humidity is above limit ({HUMIDITY_HIGH_THRESHOLD}%)")

    # Display on LED matrix
    if temp_alert:
        sense.show_message(
            "TEMP HIGH {:.1f}C".format(temp),
            text_colour=RED
        )
    else:
        sense.show_message(
            "T:{:.1f}C".format(temp),
            text_colour=GREEN
        )

    if humidity_alert:
        sense.show_message(
            "HUM HIGH {:.1f}%".format(humidity),
            text_colour=YELLOW
        )
    else:
        sense.show_message(
            "H:{:.1f}%".format(humidity),
            text_colour=BLUE
        )


    
    # 2 second delay before next reading
    time.sleep(2)
