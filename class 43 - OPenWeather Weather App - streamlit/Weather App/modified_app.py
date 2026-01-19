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

st.set_page_config(
    page_title="Weather Analytics Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# page heading
st.markdown(
    """
    <h1 style='text-align: center;'>🌦️ Weather Analytics Dashboard</h1>
    <p style='text-align: center; color: gray;'>
    Real-time weather insights & 5-day forecast analysis
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# creating side bar
st.sidebar.header("⚙️ Settings")

city = st.sidebar.text_input("City", "London")     # Enter city
fetch_weather = st.sidebar.button("Get Weather")   # get weather
show_forecast = st.sidebar.checkbox("Show Forecast", True)
show_analysis = st.sidebar.checkbox("Show Analysis", True)


if fetch_weather:
    raw_data = extract_weather_data(city)

    current = transform_current_weather(raw_data["current"])
    forecast = transform_forecast_weather(raw_data["forecast"])


    # Showing current weather
    st.subheader(f"📍 Current Weather: {city}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌡 Temperature (°C)", current["temperature"])

    with col2:
        st.metric("💧 Humidity (%)", current["humidity"])

    with col3:
        st.metric("💨 Wind Speed (m/s)", current["wind_speed"])

    with col4:
        st.metric("☁ Condition", current["condition"])


    st.write('Updated', datetime.fromtimestamp(current['timestamp']).strftime("%d %b %Y, %H:%M"))

    # show temperature forecast
    if show_forecast:
        st.markdown("### 📈 Forecast Overview")
        st.pyplot(plot_current_and_forecast_temp(current, forecast))


    # show analytics
    if show_analysis:
        st.markdown("### 📊 Weather Analytics")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["🌡 Temperature", "💧 Humidity", "💨 Wind", "🌦️ Weather Condition Distribution"]
        )

        with tab1:
            st.pyplot(plot_daily_avg_temperature(forecast))
            st.pyplot(plot_temperature_by_hour(forecast))

        with tab2:
            st.pyplot(plot_humidity_trend(forecast))

        with tab3:
            st.pyplot(plot_wind_speed_trend(forecast))

        with tab4:
            st.pyplot(plot_weather_condition_distribution(forecast))

st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
    Weather data powered by OpenWeather API | Built with Streamlit
    </p>
    """,
    unsafe_allow_html=True
)