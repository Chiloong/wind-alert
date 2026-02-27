import requests
import os

LAT = 35.24
LON = 113.24

API_KEY = os.environ["API_KEY"]
BARK_KEY = os.environ["BARK_KEY"]

WIND_SPEED_THRESHOLD = 2.5
NE_MIN = 20
NE_MAX = 100

def send_bark(msg):
    requests.get(f"https://api.day.app/{BARK_KEY}/{msg}")

def check_weather():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    )

    data = requests.get(url, timeout=10).json()

    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]

    if wind_speed >= WIND_SPEED_THRESHOLD and NE_MIN <= wind_deg <= NE_MAX:
        send_bark(f"⚠️ 东向风提醒\n风速:{wind_speed}m/s\n风向:{wind_deg}°")

if __name__ == "__main__":
    check_weather()
