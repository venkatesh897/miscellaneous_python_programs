#Program to print temperature of a given city
import requests
import json

try:
  city = argv[1]
else:
  city = input("Enter city: ")
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=f9ba15284b25d77cf2aae3a2733bb72a&units=metric'%(city))

weather_report = json.loads(response.text)

print('Temperature in %s is '%(city),end="")
print(weather_report['main']['temp'])
