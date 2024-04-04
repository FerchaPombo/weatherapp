import tkinter as tk 
from tkinter import *
from tkinfer import messagebox
from PIL import Image, ImageTk
import requests
import ttkbootstrap

# Define a function  to search for weather in a city
def search():
    city = city.entry.get() # gets users imput
    result =  get_weather(city)
    

root = ttkbootstrap.Window(themename="minty")
root.title('Weather App')
root.geometry('400x400')

# Entry widget to entry city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button widget -> to search for weather info
search_button = ttkbootstrap.Button(root, text='Search', command=search, bootstyle=Warning)
search_button.pack(pady=10)

# label widget -> to show the city/country name
location_label = tk.Label(root, font='Helvetica,25')
location_label.pack(pady=20)

# Label widget -> to show the weather icon 
icon_label = tk.label(root)
icon_label.pack()

# Label widget -> to show the temperature 
temperature_label = tk.Label(root, font='Helvetica, 20')
temperature_label.pack()

# Label widget -> to show weather description 
description_label = tk.Label(root, font='Helvetica, 20')
description_label.pack()

root.mainloop()


'''
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

while True:
    location = input('City:')
    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
    if result.json()['cod'] == '404':
        print("This place only exists in your imagination")
        continue
    break

# Extracting weather data from the response
weather_data = result.json()

# Extracting specific weather information
description = weather_data['weather'][0]['description']
temperature = round(weather_data['main']['temp'])
feels_like = round(weather_data['main']['feels_like'])
temp_min = round(weather_data['main']['temp_min'])
temp_max = round(weather_data['main']['temp_max'])
humidity = round(weather_data['main']['humidity'])

# Check if 'wind' key is present
wind_speed = round(weather_data.get('wind', {}).get('speed', 0))

# Check if 'rain' key is present
rain_volume = round(weather_data.get('rain', {}).get('1h', 0))

# Extract sunrise and sunset timestamps
sunrise_timestamp = weather_data['sys']['sunrise']
sunset_timestamp = weather_data['sys']['sunset']

# Print weather information
print(f'The weather in {location[0].upper()}{location[1:]} is {temperature}°C with {description}')
print(f'It feels like {feels_like}°C')
print(f'Today, there is a max and min of {temp_max}°C - {temp_min}°C')
print(f'There is a humidity of {humidity}%, with wind speed of {wind_speed} m/s')
if rain_volume:
    print(f'There is {rain_volume} mm of rain')
print(f'The sun will rise at {sunrise_timestamp} and set at {sunset_timestamp}')
'''