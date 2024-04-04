import tkinter as tk 
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

import ttkbootstrap

# Function to get the weather information 
def get_weather(city):
    API_key = '0ee939522a1dcd8789c86cdb16ac0966'
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("This city only exists in your imagination")
        return None
    # Parse the response JSon to get the weather information 
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # get the weather icon URL and all the weather information
    icon_url = 'https://openweathermap.org/img/wn/{icon_id}10d@2x.png'
    return (icon_url, temperature, description, city, country)



# Define a function  to search for weather in a city
def search():
    city = city.entry.get() # gets users imput
    result =  get_weather(city) #calls the get weather function to retrieve the data 
    if result is None:
        return
    # if the city is found, unpack the weather information 
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f'{city}, {country}')

    # Get the weather icon image from the url
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # updat the temp and description labels 
    temperature_label.configure(text=f'Tempersture: {temperature:.2}°C')
    description_label.configure(text=f'Description: {description}')



root = ttkbootstrap.Window(themename='morph')
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