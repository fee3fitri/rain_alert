import requests

API_key = "8808e4b20388400281ba6b66634819b2"
URL_forecast = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
  "lat": 44.34,
  "lon": 10.99,
  "appid": API_key,
}

weather_res = requests.get(URL_forecast, params=weather_params)
weather_res.raise_for_status()
data = weather_res.json()

print(data)