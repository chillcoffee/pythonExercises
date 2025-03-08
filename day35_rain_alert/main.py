import requests
import os
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")


account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Dala ka raincoat Yii♥️\n Uulan🌧️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639487600322",
    )

    print(message.status)

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Dala ka raincoat Yii♥️\n Uulan🌧️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639982529594",
    )

    print(message.status)


weather_params = {
    "lat": 11.582617,
    "lon": 122.322561,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
will_rain = False
weather_data = response.json()
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    send_sms()



