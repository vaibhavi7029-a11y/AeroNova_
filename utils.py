"""
utils.py
Helper Functions for AeroNova Weather Map
"""

from datetime import datetime


def get_current_date():
    """Return today's date."""
    return datetime.now().strftime("%d %B %Y")


def get_current_time():
    """Return current time."""
    return datetime.now().strftime("%I:%M:%S %p")


def greeting():
    """Return greeting based on current time."""

    hour = datetime.now().hour

    if hour < 12:
        return "🌞 Good Morning"

    elif hour < 17:
        return "☀️ Good Afternoon"

    elif hour < 21:
        return "🌇 Good Evening"

    return "🌙 Good Night"


def validate_city(city):
    """Validate city name."""

    if city is None:
        return False

    city = city.strip()

    if len(city) < 2:
        return False

    return True


def get_aqi_status(aqi):
    """
    Convert AQI value into status.
    """

    if aqi <= 50:
        return "🟢 Good"

    elif aqi <= 100:
        return "🟡 Moderate"

    elif aqi <= 150:
        return "🟠 Unhealthy (Sensitive)"

    elif aqi <= 200:
        return "🔴 Unhealthy"

    elif aqi <= 300:
        return "🟣 Very Unhealthy"

    return "⚫ Hazardous"


def weather_emoji(condition):
    """
    Return emoji based on weather condition.
    """

    condition = condition.lower()

    if "sun" in condition or "clear" in condition:
        return "☀️"

    elif "cloud" in condition:
        return "☁️"

    elif "rain" in condition:
        return "🌧️"

    elif "storm" in condition or "thunder" in condition:
        return "⛈️"

    elif "snow" in condition:
        return "❄️"

    elif "mist" in condition or "fog" in condition:
        return "🌫️"

    return "🌦️"


def format_temperature(temp):
    """Return formatted temperature."""
    return f"{temp} °C"


def format_speed(speed):
    """Return formatted wind speed."""
    return f"{speed} km/h"


def format_pressure(pressure):
    """Return formatted pressure."""
    return f"{pressure} mb"


def format_visibility(visibility):
    """Return formatted visibility."""
    return f"{visibility} km"


def app_footer():
    """Footer text."""

    return (
        "🌦 AeroNova Weather Map • "
        "Powered by WeatherAPI • "
        "Made with ❤️ using Streamlit"
  )
