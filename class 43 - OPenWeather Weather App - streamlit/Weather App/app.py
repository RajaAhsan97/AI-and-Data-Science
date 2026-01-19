import streamlit as st
from etl.extract import extract_weather_data
from etl.transform import (
    transform_current_weather,
    transform_forecast_weather
)
from datetime import datetime
from analysis.temperature_analysis import (
    plot_current_and_forecast_temp,
    plot_daily_avg_temperature,
    plot_humidity_trend, 
    plot_wind_speed_trend,
    plot_weather_condition_distribution,
    plot_temperature_by_hour
)
#from analysis.weather_analysis import average_temperature
#from utils.time_utils import format_timestamp

st.title("🌦️ Weather App")

city = st.text_input("Enter City", "London")

if st.button("Get Weather"):
    raw_data = extract_weather_data(city)

    current = transform_current_weather(raw_data["current"])
    forecast = transform_forecast_weather(raw_data["forecast"])

    st.subheader(f"Current weather {city}")
    st.metric("Temperature [degC]", current["temperature"])
    st.metric("Humidity [%]", current["humidity"])
    st.metric("Wind speed [m/s]", current["wind_speed"])
    #st.write("Updated:", format_timestamp(current["timestamp"]))
    st.write('Updated', datetime.fromtimestamp(current['timestamp']).strftime("%d %b %Y, %H:%M"))

    #st.subheader("Forecast")
    #st.write(forecast[:5])
    st.subheader("Temperature Trend")
    fig = plot_current_and_forecast_temp(current, forecast)
    st.pyplot(fig)
    
    st.subheader("Daily Average temperature")
    fig = plot_daily_avg_temperature(forecast)
    st.pyplot(fig)

    st.subheader("Humidity Trend")
    fig = plot_humidity_trend(forecast)
    st.pyplot(fig)

    st.subheader("Windspeed Trend")
    fig = plot_wind_speed_trend(forecast)
    st.pyplot(fig)

    st.subheader("Weather condition Distribution")
    fig = plot_weather_condition_distribution(forecast)
    st.pyplot(fig)

    st.subheader("Temperature by hour of the day")
    fig = plot_temperature_by_hour(forecast)
    st.pyplot(fig)