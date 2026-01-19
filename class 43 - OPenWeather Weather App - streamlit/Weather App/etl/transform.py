def transform_current_weather(data):
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'condition': data['weather'][0]['description'],
        'timestamp': data['dt']
    }

def transform_forecast_weather(data):
    forecast_list = []
    for item in data["list"]:
        forecast_list.append({
            "time": item["dt_txt"],
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "windspeed": item["wind"]["speed"],
            "condition": item["weather"][0]["description"]
        })
    return forecast_list
