import requests
import os
import json

LAT = 35.24
LON = 113.24

API_KEY = os.environ["API_KEY"]
BARK_KEY = os.environ["BARK_KEY"]

def send_bark(msg):
    requests.get(f"https://api.day.app/{BARK_KEY}/{msg}")

def check_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    wind_speed = data["wind"].get("speed", "无")
    wind_deg = data["wind"].get("deg", "无")

    msg = (
        f"OW原始数据\n"
        f"speed: {wind_speed} m/s\n"
        f"deg: {wind_deg}°\n"
        f"\n完整wind字段:\n{json.dumps(data['wind'])}"
    )

    send_bark(msg)

if __name__ == "__main__":
    check_weather()
