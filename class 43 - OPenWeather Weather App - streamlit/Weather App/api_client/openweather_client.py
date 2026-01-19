import requests
#from dotenv import load_dotenv
import os
import streamlit as st
#from config import settings 
#from config.settings import API_KEY, BASE_URL


# Load environment variables from .env file
#load_dotenv()

#API_KEY = os.getenv("OPENWEATHER_API_KEY")

API_KEY = st.secrets["OPENWEATHER_API_KEY"]
BASE_URL = "https://api.openweathermap.org/data/2.5"

def fetch_current_weather(city):
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    return requests.get(url, params=params).json()


def fetch_forecast_weather(city):
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    return requests.get(url, params=params).json()