import requests

APP_ID = "8e77ddd6"
APP_KEY = "401442e6ba4bf654cbd3995f8a64af87"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_params = {
    "query": input("Tell me what you did: "),
    "weight_kg": 55,
    "height_cm": 152,
    "age": 31,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(nutritionix_endpoint, json=user_params, headers=headers)
print(response.status_code)
result = response.json()
print(result)
