import requests
from pprint import pprint

import json
import csv
# import pandas as pd
# import csv

# # url = api.openweathermap.org/data/2.5/weather?q=London&mode=xml
# url = 'http://api.openweathermap.org/data/2.5/forecast?id=112931&appid=19f42fb5690d136f4a1ada64d849337e&units=metric&mode=xml'
# res = requests.get(url)

# print(data)
# # ourdata=[]

# # for x in data:
# #     listing  = [x['temp'],x['humidity']]
# #     ourdata.append[listing]

# # pprint(ourdata)

# # a = type(data)
# # print (a)

# # print(datas["main"]["temp"])

# a = 0
# for i in data:
#     if i == "t":
#         if




# :{"temp":21.32,"feels_like:18.8,"temp_min":19.3,"temp_max":19.3,"press:17.71,"feels
# pprint(data)

# Fetch JSON data from API

url = 'http://api.openweathermap.org/data/2.5/forecast?id=112931&appid=19f42fb5690d136f4a1ada64d849337e&units=metric'

response = requests.get(url)
json_data = response.json()

city_name = json_data['city']['name']

# Prepare CSV file
csv_file = 'weather_forecast.csv'
csv_obj = open(csv_file, 'w', newline='')
csv_writer = csv.writer(csv_obj)

# Write header
header = ['City', 'Date & Time', 'Temperature', 'Feels Like', 'Min Temp', 'Max Temp', 'Pressure', 'Humidity', 'Weather Description']
csv_writer.writerow(header)

# Write data rows
for item in json_data['list']:
    dt_txt = item['dt_txt']
    temp = item['main']['temp']
    feels_like = item['main']['feels_like']
    temp_min = item['main']['temp_min']
    temp_max = item['main']['temp_max']
    pressure = item['main']['pressure']
    humidity = item['main']['humidity']
    weather_description = item['weather'][0]['description']  # Assuming you want the first weather condition
    
    csv_writer.writerow([city_name, dt_txt, temp, feels_like, temp_min, temp_max, pressure, humidity, weather_description])

csv_obj.close()