# openweather api로 요청을 해서
# 그 결과를 csv로 저장하는 py
import requests
import csv
from datetime import datetime
import os
import sqlite3
from datetime import datetime
import pytz


CITY = 'seoul'
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
temp = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']



# UTC+9 타임존 설정
tz = pytz.timezone('Asia/Seoul')
now = datetime.now(tz)
timezone = now.strftime("%Y-%m-%d %H:%M:%S")

csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]
csv_data = {"timezone":timezone,"temp": temp, "humidity": humidity, "description": description}

file_exists = os.path.exists(csv_filename)

with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(header)
    writer.writerow(csv_data.values())
    print("csv 저장 완료!!")
