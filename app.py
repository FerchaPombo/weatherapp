import requests

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

location = input('Location:')
result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
print(result.json())

