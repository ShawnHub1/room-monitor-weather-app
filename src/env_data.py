from sense_hat import SenseHat

def get_environmental_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp, 2),
        "humidity": round(humidity, 2)
    }
    
    return data

# Allow standalone testing of this module(just checks if module is being run directly or imported into another program)
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice1"
    environmental_data = get_environmental_data(deviceID)
    # Print the data in JSON format for testing
    print(environmental_data)
