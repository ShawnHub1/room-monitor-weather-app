from sense_hat import SenseHat
import time

# Define some colours
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialise Sense HAT
sense = SenseHat()
sense.clear()

def get_environmental_data():
    # Read sensor data
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    return temp, humidity, pressure


while True:
    # Get readings
    temp, humidity, pressure = get_environmental_data()
    
    # Print to command line
    print("Temp: {:.1f} C  Humidity: {:.1f}%  Pressure: {:.1f} hPa".format(
        temp, humidity, pressure))
    
    # Display on LED matrix (one after the other)
    sense.show_message("T:{:.1f}C".format(temp), text_colour=RED)
    sense.show_message("H:{:.1f}%".format(humidity), text_colour=BLUE)
    sense.show_message("P:{:.1f}".format(pressure), text_colour=GREEN)
    
    # 2 second delay before next reading
    time.sleep(2)
