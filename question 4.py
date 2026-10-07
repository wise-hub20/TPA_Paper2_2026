#question 4
#112307753

import random
from datetime import datetime

# Storage for  the temp readings
readings = []


def generate_temperature(temp=None):
    if temp is None:
        temp = random.randint(10, 40)
    return temp


def generate_light(light=None):
    if light is None:
        light = random.randint(0, 100)
    return light


def classify_temperature(temp):
    if 18 <= temp <= 30:
        return "Normal"
    else:
        return "Alert"


def record_reading(learner_id, temp=None, light=None):
    temp = generate_temperature(temp)
    light = generate_light(light)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    classification = classify_temperature(temp)

    reading = {
        "learner_id": learner_id,
        "temperature": temp,
        "light": light,
        "timestamp": timestamp,
        "classification": classification
    }
    readings.append(reading)
    return reading


def display_latest_reading():
    if readings:
        latest = readings[-1]
        print(f"Timestamp: {latest['timestamp']}")
        print(f"Learner/Session: {latest['learner_id']}")
        print(f"Temperature: {latest['temperature']} °C ({latest['classification']})")
        print(f"Light Level: {latest['light']} %")
    else:
        print("No readings recorded yet.")

#usage
record_reading("Learner001")  # generates random values
record_reading("LabSessionA", temp=25, light=80)  # accepts given values
display_latest_reading()
