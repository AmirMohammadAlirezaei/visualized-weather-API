import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import json
import csv

url = 'http://api.openweathermap.org/data/2.5/forecast?id=112931&appid=19f42fb5690d136f4a1ada64d849337e&units=metric'

response = requests.get(url)
json_data = response.json()

city_name = json_data['city']['name']

csv_file = 'weather_forecast.csv'
csv_obj = open(csv_file, 'w', newline='')
csv_writer = csv.writer(csv_obj)

header = ['City', 'Date & Time', 'Temperature', 'Feels Like', 'Min Temp', 'Max Temp', 'Pressure', 'Humidity', 'Weather Description']
csv_writer.writerow(header)

for item in json_data['list']:
    dt_txt = item['dt_txt']
    temp = item['main']['temp']
    feels_like = item['main']['feels_like']
    temp_min = item['main']['temp_min']
    temp_max = item['main']['temp_max']
    pressure = item['main']['pressure']
    humidity = item['main']['humidity']
    weather_description = item['weather'][0]['description']
    
    csv_writer.writerow([city_name, dt_txt, temp, feels_like, temp_min, temp_max, pressure, humidity, weather_description])

csv_obj.close()

df = pd.read_csv('weather_forecast.csv')

my_xaxis = list()
my_xaxis = df.loc[:, 'Date & Time']

df.plot(x='Date & Time', y='Temperature', kind='line', fontsize = 7)
plt.title('Visualization of Two Columns')
plt.xlabel('Date & Time', fontsize=10)
plt.ylabel('Temperature')
plt.legend(['Temperature'])

plt.show()