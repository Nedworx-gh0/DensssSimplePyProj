import requests
from pprint import pprint   

def get_weather_info(city_name):
    api_key = "d651f7a4caa1d8e01f1687fc34a352a5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    data = requests.get(url).json()

    temp = data['main']['temp'] - 273.15
    rounded_temp = round(temp, 2)
    desc = data['weather'][0]['description'].title()
    temp = data['main']['temp'] - 273.15
    vision = data['visibility']
    country = data['sys']['country']
    return[rounded_temp, desc, vision, country]


