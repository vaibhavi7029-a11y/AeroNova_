import streamlit as st
import pandas as pd

from weather import Weather
from utils import (
    greeting,
    get_current_date,
    get_current_time,
    validate_city,
    weather_emoji,
    get_aqi_status,
    app_footer,
)

from styles import load_css
from map import WeatherMap


# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AeroNova Weather Map",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(load_css(), unsafe_allow_html=True)


# ----------------------------------
# Session State
# ----------------------------------

if "weather" not in st.session_state:
    st.session_state.weather = Weather()

if "data" not in st.session_state:
    st.session_state.data = None


# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.image("assets/logo.png", width=120)

    st.title("🌦 AeroNova")

    st.success(greeting())

    st.write("📅", get_current_date())

    st.write("🕒", get_current_time())

    st.divider()

    city = st.text_input(
        "📍 Search City",
        placeholder="Enter city name..."
    )

    search = st.button(
        "🔍 Search Weather",
        use_container_width=True
    )

    st.divider()

    st.info(
        """
        ### About

        ✔ Live Weather

        ✔ Interactive Map

        ✔ AQI

        ✔ 7 Day Forecast

        ✔ Weather Dashboard
        """
    )

    st.divider()

    st.caption(app_footer())


# ----------------------------------
# Header
# ----------------------------------

st.markdown(
    """
    <div class="main-title">
        🌦 AeroNova Weather Map
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Premium Real-Time Weather Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# ----------------------------------
# Search Weather
# ----------------------------------

if search:

    if validate_city(city):

        with st.spinner("Fetching weather..."):

            st.session_state.data = (
                st.session_state.weather.get_weather(city)
            )

    else:

        st.warning("Please enter a valid city name.")

# ----------------------------------
# Weather Dashboard
# ----------------------------------

if st.session_state.data:

    data = st.session_state.data

    if data["success"]:

        col1, col2 = st.columns([1.2, 1])

        # -------------------------
        # Left Side
        # -------------------------

        with col1:

            st.markdown(
                f"""
                <div class="glass-card">

                <div class="weather-title">

                {weather_emoji(data["condition"])}
                {data["city"]}, {data["country"]}

                </div>

                <br>

                <h1 style="text-align:center;">
                {data["temperature"]}°C
                </h1>

                <h4 style="text-align:center;">
                {data["condition"]}
                </h4>

                <p style="text-align:center;">
                Feels Like :
                {data["feels_like"]}°C
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "💧 Humidity",
                f'{data["humidity"]}%'
            )

            c2.metric(
                "💨 Wind",
                f'{data["wind"]} km/h'
            )

            c3.metric(
                "☀ UV",
                data["uv"]
            )

            c4, c5, c6 = st.columns(3)

            c4.metric(
                "🌬 Pressure",
                f'{data["pressure"]} mb'
            )

            c5.metric(
                "👁 Visibility",
                f'{data["visibility"]} km'
            )

            c6.metric(
                "🧭 Direction",
                data["wind_dir"]
            )

            st.markdown("### 🌿 Air Quality")

            aqi = data["air_quality"]

            if "us-epa-index" in aqi:

                st.success(
                    get_aqi_status(aqi["us-epa-index"])
                )

            st.markdown("### 📍 Location")

            st.write(
                f"**Region :** {data['region']}"
            )

            st.write(
                f"**Latitude :** {data['lat']}"
            )

            st.write(
                f"**Longitude :** {data['lon']}"
            )

            st.write(
                f"**Local Time :** {data['localtime']}"
            )

            st.write(
                f"**Last Updated :** {data['last_updated']}"
            )

        # -------------------------
        # Right Side
        # -------------------------

        with col2:

            st.markdown("## 🗺 Interactive Weather Map")

            WeatherMap.show(
                data["lat"],
                data["lon"],
                data["city"],
                data["condition"],
                data["temperature"]
            )

    else:

        st.error(data["message"])

# ----------------------------------
# 7-Day Forecast
# ----------------------------------

if st.session_state.data and st.session_state.data["success"]:

    st.divider()

    st.subheader("📅 7-Day Weather Forecast")

    forecast = st.session_state.data["forecast"]

    rows = []

    for day in forecast:

        rows.append({

            "Date": day["date"],

            "Condition": day["day"]["condition"]["text"],

            "Max °C": day["day"]["maxtemp_c"],

            "Min °C": day["day"]["mintemp_c"],

            "Avg °C": day["day"]["avgtemp_c"],

            "Humidity %": day["day"]["avghumidity"],

            "Rain %": day["day"]["daily_chance_of_rain"]

        })

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # -------------------------------
    # Sunrise / Sunset
    # -------------------------------

    st.divider()

    st.subheader("🌅 Sun & Moon")

    today = forecast[0]["astro"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🌅 Sunrise", today["sunrise"])

    c2.metric("🌇 Sunset", today["sunset"])

    c3.metric("🌙 Moonrise", today["moonrise"])

    c4.metric("🌑 Moonset", today["moonset"])


    # -------------------------------
    # Footer
    # -------------------------------

    st.divider()

    st.markdown(
        """
        <div class="footer">

        🌦 <b>AeroNova Weather Map</b><br><br>

        Powered by <b>WeatherAPI</b><br>

        Built using <b>Python • Streamlit • Folium</b><br><br>

        ❤️ Made by Vaibhavi

        </div>
        """,
        unsafe_allow_html=True
  )
