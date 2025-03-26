import requests
from datetime import datetime

APP_ID = "8e77ddd6"
APP_KEY = "401442e6ba4bf654cbd3995f8a64af87"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
what_i_did = "ran 2 miles for 30 mins and walk 3 km for 15 mins"
#what_i_did = input("Tell me what you did: ")
user_params = {
    "query": what_i_did,
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
#print(result["exercises"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = "https://api.sheety.co/dca3ae1b6cd5aafc699bf906e187f2a7/workoutTracking/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)



