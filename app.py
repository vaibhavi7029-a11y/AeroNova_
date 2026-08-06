import streamlit as st

from config import OPENWEATHER_API_KEY
from weather import Weather
from utils import (
    greeting,
    get_current_date,
    get_current_time,
    validate_city,
    weather_emoji,
    app_footer,
)
from styles import load_css
from map import WeatherMap

st.set_page_config(
    page_title="AeroNova Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# Debug
st.write("API:", OPENWEATHER_API_KEY)


# -------------------------------------
# Page Configuration
# -------------------------------------

st.set_page_config(
    page_title="AeroNova Weather",
    page_icon="🌦",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)


# -------------------------------------
# Session State
# -------------------------------------

if "weather" not in st.session_state:
    st.session_state.weather = Weather()

if "data" not in st.session_state:
    st.session_state.data = None


# -------------------------------------
# Sidebar
# -------------------------------------

with st.sidebar:

    st.title("🌦 AeroNova")

    st.success(greeting())

    st.write("📅", get_current_date())

    st.write("🕒", get_current_time())

    st.divider()

    city = st.text_input(
        "📍 Enter City",
        placeholder="Mumbai"
    )

    search = st.button(
        "🔍 Get Weather",
        use_container_width=True
    )

    st.divider()

    st.info(
        """
### Features

✅ Live Weather

✅ Interactive Map

✅ Temperature

✅ Humidity

✅ Wind Speed

✅ Pressure

✅ Visibility
"""
    )

    st.divider()

    st.caption(app_footer())


# -------------------------------------
# Header
# -------------------------------------

st.markdown(
    """
<div class="main-title">
🌦 AeroNova Weather Dashboard
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="sub-title">
Live Weather Information using OpenWeather API
</div>
""",
    unsafe_allow_html=True,
)

st.write("")


# -------------------------------------
# Search
# -------------------------------------

if search:

    if validate_city(city):

        with st.spinner("Fetching Weather..."):

            st.session_state.data = (
                st.session_state.weather.get_weather(city)
            )

    else:

        st.warning("Please enter a city name.")

# -------------------------------------
# Weather Dashboard
# -------------------------------------

if st.session_state.data:

    data = st.session_state.data

    if data["success"]:

        col1, col2 = st.columns([1.2, 1])

        # -----------------------------
        # Left Panel
        # -----------------------------

        with col1:

            st.markdown(
                f"""
<div class="glass-card">

<h2 style="text-align:center;">
{weather_emoji(data["condition"])}
{data["city"]}, {data["country"]}
</h2>

<p style="text-align:center;">
<img src="{data['icon']}" width="90">
</p>

<h1 style="text-align:center;">
{data["temperature"]} °C
</h1>

<h4 style="text-align:center;">
{data["description"].title()}
</h4>

<p style="text-align:center;">
Feels Like {data["feels_like"]} °C
</p>

</div>
""",
                unsafe_allow_html=True,
            )

            st.write("")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "💧 Humidity",
                f'{data["humidity"]}%'
            )

            c2.metric(
                "💨 Wind",
                f'{data["wind"]} m/s'
            )

            c3.metric(
                "🌬 Pressure",
                f'{data["pressure"]} hPa'
            )

            st.write("")

            c4, c5 = st.columns(2)

            c4.metric(
                "👁 Visibility",
                f'{data["visibility"]/1000:.1f} km'
            )

            c5.metric(
                "🌡 Feels Like",
                f'{data["feels_like"]} °C'
            )

            st.write("")

            st.subheader("📍 Location")

            st.write(f"**City:** {data['city']}")
            st.write(f"**Country:** {data['country']}")
            st.write(f"**Latitude:** {data['lat']}")
            st.write(f"**Longitude:** {data['lon']}")

        # -----------------------------
        # Right Panel
        # -----------------------------

        with col2:

            st.subheader("🗺 Weather Map")

            WeatherMap.show(
                data["lat"],
                data["lon"],
                data["city"],
                data["condition"],
                data["temperature"]
            )

    else:

        st.error(data["message"])

        # -------------------------------------
# Footer
# -------------------------------------

st.divider()

st.markdown(
    """
    <div class="glass-card">

    <h3 align="center">🌦 AeroNova Weather Dashboard</h3>

    <p align="center">
    Live Weather Information powered by OpenWeather API
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -------------------------------------
# Weather Tips
# -------------------------------------

if st.session_state.data and st.session_state.data["success"]:

    temp = st.session_state.data["temperature"]

    st.subheader("💡 Weather Tips")

    if temp >= 35:

        st.warning(
            "🔥 It's very hot. Stay hydrated and avoid direct sunlight."
        )

    elif temp >= 25:

        st.info(
            "😎 Pleasant weather. Great day for outdoor activities."
        )

    elif temp >= 15:

        st.success(
            "🌤 Cool and comfortable weather."
        )

    else:

        st.warning(
            "🧥 It's cold outside. Wear warm clothes."
        )


# -------------------------------------
# About
# -------------------------------------

with st.expander("ℹ About AeroNova"):

    st.markdown("""
### AeroNova Weather Dashboard

Features

- 🌦 Live Weather
- 🌡 Temperature
- 💧 Humidity
- 💨 Wind Speed
- 🌬 Pressure
- 👁 Visibility
- 🗺 Interactive Map
- 📍 Latitude & Longitude

Built using

- Python
- Streamlit
- OpenWeather API
- Folium
""")


# -------------------------------------
# Bottom Footer
# -------------------------------------

st.divider()

st.caption("🌦 AeroNova Weather Dashboard v1.0")

st.caption("Powered by OpenWeather API")

st.caption("Made with ❤️ using Streamlit")
