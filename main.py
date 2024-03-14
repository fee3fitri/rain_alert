import requests

API_key = "8808e4b20388400281ba6b66634819b2"
URL_forecast = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
  "lat": 37.338207,
  "lon": -121.886330,
  "appid": API_key,
}

weather_res = requests.get(URL_forecast, params=weather_params)
weather_res.raise_for_status()
data_json = weather_res.json()

for data in data_json["list"]:
  if data["weather"][0]["main"] == "Clouds":
    date_time = data["dt_txt"].split()
    print(date_time)