import requests
OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = "825a9682f806aef7999ce7324fc996a0"

weather_params = {
    "lat": 11.694760,
    "lon": 122.366859,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)

weather_data = response.json()
for hour_data in weather_data["list"]:
    print(hour_data)