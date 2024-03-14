weather_res = requests.get(URL_forecast, params=weather_params)
# weather_res.raise_for_status()
# data = weather_res.json()