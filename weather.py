import requests
from config import WEATHER_API_KEY, BASE_URL


class Weather:

    def __init__(self):
        self.api_key = WEATHER_API_KEY

    def get_weather(self, city):

        url = f"{BASE_URL}/weather"

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params, timeout=10)

            data = response.json()

            if response.status_code != 200:
                return {
                    "success": False,
                    "message": data.get("message", "Unable to fetch weather.")
                }

            return {
                "success": True,
                "city": data["name"],
                "country": data["sys"]["country"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "condition": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                "wind": data["wind"]["speed"]
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }
