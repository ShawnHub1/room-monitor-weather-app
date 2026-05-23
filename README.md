## Smart Weather & Room Monitoring System with alerts 
## Student Name: Shawn Cahill  
## Student ID: 20116761

---
# Demo video link to youtube

https://youtu.be/BLrCr3bGq7A

---

# Project Overview

This project is a Raspberry Pi based connected device system that monitors indoor room conditions and compares them with outdoor weather data.

The Raspberry Pi reads indoor temperature and humidity using the Sense HAT. The system then checks the readings against threshold values and sends live data to a Blynk IoT dashboard. The project also retrieves outdoor weather information from the Open-Meteo API, including outdoor temperature, humidity, rainfall, and wind speed.

The system provides live dashboard monitoring, alert indicators, email alert automation through Blynk, local Sense HAT LED status colours, and CSV logging for historical data.

---

## Project Aim

The aim of this project is to build a small connected monitoring system that can:

- collect indoor environmental data from a Raspberry Pi Sense HAT
- process readings using threshold checks and alert rules
- retrieve outdoor weather data from an external API
- display live readings on a Blynk dashboard
- provide alerts for indoor and outdoor conditions
- log readings to a CSV file for historical review

---

## System Architecture

The project follows the connected device layers from the assignment specification:

| Layer | Project Implementation |
|---|---|
| Data Source | Raspberry Pi Sense HAT and Open-Meteo API |
| Processing | Threshold checks, status calculation, rain and wind alert rules |
| Network / Communication | Blynk IoT platform and HTTP API request to Open-Meteo |
| Application | Blynk dashboard, email alerts, CSV history, Sense HAT LED output |

---

## Technologies Used

- Raspberry Pi
- Sense HAT
- Python
- Blynk IoT Platform
- Open-Meteo Weather API
- CSV file logging
- python-dotenv
- requests
- VS Code Remote SSH
- Git and GitHub

---


## Main Features

### Indoor Monitoring

The Raspberry Pi reads:

- indoor temperature
- indoor humidity

The readings can come from the real Sense HAT sensor or from simulated data for testing.

### Threshold Alerts

The system checks indoor readings against configured thresholds:

- temperature alert
- humidity alert

The threshold values are stored in the `.env` file.

### Outdoor Weather Data

The system retrieves outdoor weather data for Newbridge using the Open-Meteo API.

The outdoor data includes:

- outdoor temperature
- outdoor humidity
- current rain value
- wind speed

### Weather Alerts

The system generates outdoor weather alerts:

- rain alert
- wind alert

The wind alert is triggered when wind speed is above the configured threshold in the code.

### Blynk Dashboard

The live dashboard displays indoor and outdoor readings, along with alert indicators.

### CSV Logging

The application logs readings to `weather&sensor_log.csv` 

### Sense HAT LED Status

The Sense HAT LED matrix changes colour depending on the current alert state.

Example status colours:

| LED Colour | Meaning |
|---|---|
| Green | Normal |
| Red | Temperature alert |
| Yellow | Humidity alert |
| Purple | Temperature and humidity alert |
| Blue | Rain or wind alert |

---

## Blynk Dashboard Setup

The Blynk dashboard uses four gauges and four alert indicators.

### Blynk Virtual Pin Mapping

| Virtual Pin | Datastream | Widget Type | Purpose |
|---|---|---|---|
| V1 | Temperature | Gauge | Indoor temperature |
| V2 | Humidity | Gauge | Indoor humidity |
| V3 | Temp Alert | LED / Label | Indoor temperature alert |
| V4 | Humidity Alert | LED / Label | Indoor humidity alert |
| V5 | Outdoor Temperature | Gauge | Outdoor temperature |
| V6 | Outdoor Humidity | Gauge | Outdoor humidity |
| V7 | Rain Alert | LED / Label | Rain detected alert |
| V8 | Wind Alert | LED / Label | High wind alert |

### Recommended Datastream Ranges

| Datastream | Data Type | Min | Max | Unit |
|---|---|---:|---:|---|
| V1 Temperature | Double | 0 | 40 | °C |
| V2 Humidity | Double | 0 | 100 | % |
| V3 Temp Alert | Integer | 0 | 1 | none |
| V4 Humidity Alert | Integer | 0 | 1 | none |
| V5 Outdoor Temperature | Double | -5 | 40 | °C |
| V6 Outdoor Humidity | Double | 0 | 100 | % |
| V7 Rain Alert | Integer | 0 | 1 | none |
| V8 Wind Alert | Integer | 0 | 1 | none |

---

## Blynk Email Alerts

Blynk automations are used to send email alerts when alert datastreams change state.

Email alerts were configured for:

- temperature alert
- humidity alert
- rain alert
- wind alert

The alert datastreams use `0` and `1` values:

| Value | Meaning |
|---|---|
| 0 | Normal |
| 1 | Alert active |

A limit period can be set in Blynk automations to prevent repeated emails.

---

## CSV Logging

The system logs historical readings to a CSV file called:

```bash
weather&sensor_log.csv


## How to Run
Clone repository
git clone https://github.com/ShawnHub1/room-monitor-weather-app.git
cd room-monitor-weather-app

Activate the virtual environment:
source .venv/bin/activate
python -m src.main
