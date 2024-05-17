import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import style
import json
import csv

url = 'http://api.openweathermap.org/data/2.5/forecast?id=112931&appid=19f42fb5690d136f4a1ada64d849337e&units=metric'
response = requests.get(url)
json_data = response.json()

#city name
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
df['Date & Time'] = pd.to_datetime(df['Date & Time'])

# Plotting
fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

# Plotting data
p1, = ax.plot(df['Date & Time'], df['Feels Like'], "C0", label="Feels Like")
p2, = ax.plot(df['Date & Time'], df['Min Temp'], "C1", label="Min Temp")
p3, = ax.plot(df['Date & Time'], df['Max Temp'], "C2", label="Max Temp")

# Adjusting tick frequency on the X-axis
ax.xaxis.set_major_locator(plt.MaxNLocator(12))

# Formatting plot
ax.set(xlabel="Date & Time", ylabel="Temperature")

# Adding legend
ax.legend(handles=[p1, p2, p3], loc='upper left')

plt.show()
