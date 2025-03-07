import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

#twilio account side
account_sid = ""
auth_token = ""

def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella. ☂️ Uulan mamaya!",
        from_="whatsapp:+14155238886",
        to="whatsapp:YOUR NUMBER",
    )

    print(message.status)


weather_params = {
    "lat": 11.694760,
    "lon": 122.366859,
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
    print("done sent a text 'Bring an umbrella. ☂️'")


