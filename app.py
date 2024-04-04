import requests

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

location = input('Location:')
result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')


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
print(f'The weather in {location} is {temperature}°C with {description}')
print(f'It feels like {feels_like}°C')
print(f'Today, there is a max and min of {temp_max}°C - {temp_min}°C')
print(f'There is a humidity of {humidity}%, with wind speed of {wind_speed} m/s')
if rain_volume:
    print(f'There is {rain_volume} mm of rain')
print(f'The sun will rise at {sunrise_timestamp} and set at {sunset_timestamp}')
