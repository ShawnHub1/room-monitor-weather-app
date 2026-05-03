#!/usr/bin/env python3
import os, time, json
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# Config (env variables with defaults) 
USER_ID = os.getenv("USER_ID", "SCahill")
BROKER    = os.getenv("MQTT_BROKER", "test.mosquitto.org")
TELEMETRY_PERIOD_S = float(os.getenv("TELEMETRY_PERIOD_S", "10"))

#Topics
TELEMETRY_TOPIC = f"/{USER_ID}/telemetry/environment"

#Hardware
sense = SenseHat()
sense.clear(0, 0, 0)

#MQTT client
client = mqtt.Client(client_id=f"{USER_ID}-edge")

def read_environment():
    return {
        "temp": round(sense.temperature, 2),
        "humidity": round(sense.humidity, 2),
    }

def main():
    client.connect(BROKER)

    next_pub = time.monotonic()  # heartbeat timer

    while True:
        # Process MQTT network I/O without using a background thread
        client.loop(timeout=0.5)

        now = time.monotonic()
        if now >= next_pub:
            env = read_environment()
            payload = {
                "userID": USER_ID,
                "temp": env["temp"],
                "humidity": env["humidity"],
                "ts": int(time.time())
            }
            # QoS 0 for frequent telemetry; retain latest for late subscribers
            client.publish(TELEMETRY_TOPIC, json.dumps(payload), qos=0, retain=True)
            print("Telemetry:", payload)
            next_pub = now + TELEMETRY_PERIOD_S

        time.sleep(0.1)

if __name__ == "__main__":
    main()
