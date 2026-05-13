## Smart Weather & Room Monitoring System with alerts 
## Student Name: Shawn Cahill  
## Student ID: 20116761

---

# Project Overview

This project is an IoT-based smart monitoring system built using a Raspberry Pi. The system combines live room environment data with online weather forecast data to provide monitoring, alerts and historical analysis through a web dashboard.

The Raspberry Pi will collect room temperature and humidity data using the SenseHAT sensor. The project will also connect to an external weather API to retrieve current and forecast weather conditions.

The application will process this data and apply programmed logic and threshold checks. Example functionality includes:
- Alerting when room temperature becomes too high
- Detecting high humidity levels
- Notifying the user when rain is expected
- Comparing indoor and outdoor conditions
- Logging historical sensor readings for trend analysis

The aim of the project is to build a proof-of-concept connected device system that demonstrates:
- Data collection
- Processing and analysis
- Networking and communication
- Dashboard visualisation
- Alerts and notifications

---

# Technologies and Equipment

## Hardware
- Raspberry Pi
- SenseHAT
- WiFi connection
- Laptop/PC for development

---

## Programming Languages
- Python
- HTML
- CSS
- JavaScript

---

## Networking and Communication
- Blynk


---

## Software and Frameworks
- Blynk
- OpenWeather API

---

## Development Tools
- VS Code
- Git
- GitHub

---

# Planned Features

## Data Sources
- SenseHAT temperature readings
- SenseHAT humidity readings
- External weather API data

---

## Processing
- Threshold checks
- Average calculations
- Weather comparisons
- Alert generation
- Historical trend analysis

---

## Networking
- Raspberry Pi publishes data using MQTT or HTTP
- JSON formatted data messages between components

---

## Application Layer
- Live dashboard
- Historical graphs and charts
- Alerts and notifications
- Data logging to database

---

# Blynk mapping table

| Virtual Pin | Purpose |
| V1 | Indoor Temperature |
| V2 | Indoor Humidity |
| V3 | Temperature Alert |
| V4 | Humidity Alert |
| V5 | Outdoor Temperature |
| V6 | Outdoor Humidity |
| V7 | Rain Alert |
| V8 | Wind Alert |



## How to Run

Activate the virtual environment:
source .venv/bin/activate

python -m src.main
