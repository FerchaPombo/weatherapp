from django.shortcuts import render
from .models import Weather
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        result = get_weather(city)
        if result: 
            # Clear existing weather data
            Weather.objects.all().delete()

            # Save new weather data
            icon_url, temperature, description, city, country, feels_like, temp_min, temp_max, humidity = result 
            Weather.objects.create(
                city=city,
                country=country,
                temperature=temperature,
                description=description,
                icon_url=icon_url,
                feels_like=feels_like,
                temp_min=temp_min,
                temp_max=temp_max,
                humidity=humidity
            )
    weathers = Weather.objects.all()
    return render(request, 'home.html', {'weathers': weathers})

def get_weather(city):
    API_key = '0ee939522a1dcd8789c86cdb16ac0966'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("This city only exists in your imagination")
        return None

    # Parse the response JSON to get the weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    feels_like = weather['main']['feels_like']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']
    humidity = weather['main']['humidity']

    # Construct the weather icon URL
    icon_url = f'https://openweathermap.org/img/wn/{icon_id}.png'
    return (icon_url, temperature, description, city, country, feels_like, temp_min, temp_max, humidity)