import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


def plot_current_and_forecast_temp(current_weather: dict, forecast_weather: list):
    """
    current_weather: dict from transform_current_weather
    forecast_weather: list from transform_forecast_weather
    """

    # ----- Current temperature -----
    current_time = [datetime.now()]
    current_temp = [current_weather["temperature"]]

    # ----- Forecast temperature -----
    forecast_times = [
        datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S")
        for item in forecast_weather
    ]
    forecast_temps = [item["temp"] for item in forecast_weather]

    # ----- Plot -----
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        current_time,
        current_temp,
        marker='o',
        color='red',
        label='Current Temperature'
    )

    ax.plot(
        forecast_times,
        forecast_temps,
        marker='o',
        linestyle='--',
        color='blue',
        label='Forecast Temperature'
    )

    ax.set_title("Current vs Forecast Temperature Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True)

    return fig

def plot_daily_avg_temperature(forecast_weather):
    df = pd.DataFrame(forecast_weather)
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = df["time"].dt.date

    daily_avg = df.groupby("date")["temp"].mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(daily_avg.index, daily_avg.values, marker="o")
    ax.set_title("Daily Average Temperature (5 Days)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)

    return fig


def plot_humidity_trend(forecast_weather):
    times = [datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S") for item in forecast_weather]
    humidity = [item["humidity"] for item in forecast_weather]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(times, humidity, marker="o")
    ax.set_title("Humidity Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("Humidity (%)")
    ax.grid(True)

    return fig


def plot_wind_speed_trend(forecast_weather):
    times = [datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S") for item in forecast_weather]
    wind_speed = [item["windspeed"] for item in forecast_weather]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(times, wind_speed, marker="o")
    ax.set_title("Wind Speed Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("Wind Speed (m/s)")
    ax.grid(True)

    return fig


def plot_weather_condition_distribution(forecast_weather):
    conditions = [item["condition"] for item in forecast_weather]
    condition_counts = pd.Series(conditions).value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(condition_counts.index, condition_counts.values)
    ax.set_title("Weather Condition Distribution")
    ax.set_xlabel("Condition")
    ax.set_ylabel("Frequency")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y")

    return fig


def plot_temperature_by_hour(forecast_weather):
    df = pd.DataFrame(forecast_weather)
    df["time"] = pd.to_datetime(df["time"])
    df["hour"] = df["time"].dt.hour

    hourly_avg = df.groupby("hour")["temp"].mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(hourly_avg.index, hourly_avg.values, marker="o")
    ax.set_title("Average Temperature by Hour")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)

    return fig
