from django.shortcuts import render
import requests
from .models import City, Task
from .forms import CityForm, TaskForm


def index(request):
    task = Task.objects.all()
    appid = 'd2c5bb4010376409077d0bb086a6c65d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {'city': city,
                     'temp': res['main']['temp'],
                     'icon': res['weather'][0]['icon'],
                     }

        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form, 'title': 'Главная страница',
               'tasks': task, }

    return render(request, "index.html", context)


def about(request):
    task = Task.objects.all()
    return render(request, 'about.html', {'title': 'Главная страница', 'tasks': task})