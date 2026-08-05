import requests
from config import WEATHER_API_KEY, BASE_URL


class Weather:

    def __init__(self):
        self.api_key = WEATHER_API_KEY

    def get_weather(self, city):
        """
        Get current weather + 7-day forecast + AQI
        """

        url = f"{BASE_URL}/forecast.json"

        params = {
            "key": self.api_key,
            "q": city,
            "days": 7,
            "aqi": "yes",
            "alerts": "yes"
        }

        try:
            response = requests.get(url, params=params, timeout=15)

            if response.status_code != 200:
                return {
                    "success": False,
                    "message": response.json().get(
                        "error", {}
                    ).get(
                        "message",
                        "Unable to fetch weather."
                    )
                }

            data = response.json()

            return {
                "success": True,

                # ------------------------
                # Location
                # ------------------------

                "city": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "lat": data["location"]["lat"],
                "lon": data["location"]["lon"],
                "localtime": data["location"]["localtime"],

                # ------------------------
                # Current Weather
                # ------------------------

                "temperature": data["current"]["temp_c"],
                "feels_like": data["current"]["feelslike_c"],
                "condition": data["current"]["condition"]["text"],
                "icon": "https:" + data["current"]["condition"]["icon"],
                "humidity": data["current"]["humidity"],
                "wind": data["current"]["wind_kph"],
                "wind_dir": data["current"]["wind_dir"],
                "pressure": data["current"]["pressure_mb"],
                "visibility": data["current"]["vis_km"],
                "uv": data["current"]["uv"],
                "air_quality": data["current"].get("air_quality", {}),
                "last_updated": data["current"]["last_updated"],

                # ------------------------
                # Forecast
                # ------------------------

                "forecast": data["forecast"]["forecastday"]
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }
