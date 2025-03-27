import os

import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")

nutritionix_endpoint = os.environ.get("nutritionix_endpoint")
#what_i_did = "ran 2 miles for 30 mins and walk 3 km for 15 mins"
what_i_did = input("Tell me what you did: ")
user_params = {
    "query": what_i_did,
    "weight_kg": 55,
    "height_cm": 152,
    "age": 31,
}

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(nutritionix_endpoint, json=user_params, headers=nutritionix_headers)
print(response.status_code)
result = response.json()  #this is the json from nutriotinix
#print(result["exercises"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = os.environ.get("sheet_endpoint")
sheety_headers = {
    "Authorization": AUTHORIZATION
}

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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)
