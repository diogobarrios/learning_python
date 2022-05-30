#! python3

# quickWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py <location>')
    sys.exit()

location = ' '.join(sys.argv[1:])
api = '1e409b17284acb75d2a12036c3d605a2'
# Download the JSON data from OpenWeatherMap.org's API
url_location = 'https://api.openweathermap.org/data/2.5/weather?q='
url_api = '&appid='
url = url_location + location + url_api + api
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions.
https://api.openweathermap.org/data/2.5/weather?q=funchal&
units=metric&
lang=pt&
appid=1e409b17284acb75d2a12036c3d605a2
