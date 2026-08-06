import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

if "OPENWEATHER_API_KEY" in st.secrets:
    OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]
else:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"
