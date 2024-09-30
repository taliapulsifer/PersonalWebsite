import requests
from django.shortcuts import render

def home(request):
    api_key = '51a4812b2711596a930e1419900d1444'
    city = "Austin"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(weather_url)

    # Print the status code to check if the request was successful
    print("API Status Code:", response.status_code)

    # Print the response content to see the raw data returned
    print("API Response:", response.json())

    weather_data = response.json()

    weather_disc = weather_data['main']

    if response.status_code == 200:
        weather_disc = weather_data['weather'][0]['description']  # Use the correct key to get the description
    else:
        weather_disc = "Could not retrieve weather data."

    return render(request, 'home.html', {'weather_disc': weather_disc})

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    # Dynamic data, easier to add and remove projects
    project_list = [
        {'name': 'Diet App', 'description': 'Track macros and calories', 'link': 'https://your-diet-app.herokuapp.com'},
    ]

    context = {'projects': project_list}
    return render(request, 'projects.html', context)