import requests
from pprint import pprint

def get_weather_info_v1(city_name):
    api_key = "d651f7a4caa1d8e01f1687fc34a352a5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    data = requests.get(url).json()
    #pprint(data)

    temp = data['main']['temp'] - 273.15
    rounded_temp = round(temp,2)
    desc = data['weather'][0]['description'].title()
    # print(rounded_temp)
    # print(desc)
    return[rounded_temp, desc]

# location_1= get_weather_info("Manila")
# print(location_1)
# location_2= get_weather_info("Milford Sound")
# print(location_2)

