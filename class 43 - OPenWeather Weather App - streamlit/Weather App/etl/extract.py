from api_client.openweather_client import fetch_current_weather, fetch_forecast_weather


def extract_weather_data(city):
    return {
        'current': fetch_current_weather(city),
        'forecast': fetch_forecast_weather(city)
    }