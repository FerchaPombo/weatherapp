from django.shortcuts import render
from .models import Weather
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        result = get_weather(city)
        if result: 
            icon_url, temperature,description, city, country = result 
            Weather.objects.create(
                city=city,
                country=country,
                temperature=temperature,
                description=description,
                icon_url=icon_url
            )
    weathers = Weather.objects.all()
    return render(request, 'home.html', {'weathers': weathers})

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

