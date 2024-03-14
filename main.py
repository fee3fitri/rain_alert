import requests
import urllib.request
import urllib.parse

# ------- Sends SMS Notification ------- #
def sendSMS(sms_api, numbers, sender, message):
  data = urllib.parse.urlencode({
    "apikey": sms_api,
    "numbers": numbers,
    "message": message,
    "sender": sender
  })

  data = data.encode("utf-8")
  request = urllib.request.Request("https://api.txtlocal.com/send/?")
  f = urllib.request.urlopen(request,data)
  fr = f.read()
  return fr


# ------- Getting weather data ------- #
SMS_API_key = "NmI2YTVhN2E2OTQzN2EzMDY4Njg0MTRkNzQ0OTRhNzE="
weather_API_key = "8808e4b20388400281ba6b66634819b2"
URL_forecast = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = { # Tulsa location
  "lat": 36.153980,
  "lon": -95.992775,
  "appid": weather_API_key,
  "cnt": 4,
  "units": "imperial",
}

weather_res = requests.get(URL_forecast, params=weather_params)
weather_res.raise_for_status()
data_json = weather_res.json()

for data in data_json["list"]:
  if data["weather"][0]["id"] < 600:
    [date, time] = data["dt_txt"].split()