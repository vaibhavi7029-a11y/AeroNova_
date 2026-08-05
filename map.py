"""
map.py
Interactive Weather Map
"""

import folium
from streamlit_folium import st_folium


class WeatherMap:

    @staticmethod
    def show(lat, lon, city, condition, temperature):
        """
        Display interactive weather map.
        """

        weather_map = folium.Map(
            location=[lat, lon],
            zoom_start=10,
            control_scale=True,
            tiles="CartoDB positron"
        )

        popup = f"""
        <b>{city}</b><br>
        🌡 Temperature: {temperature} °C<br>
        ☁ {condition}
        """

        folium.Marker(
            location=[lat, lon],
            popup=popup,
            tooltip=city,
            icon=folium.Icon(
                color="blue",
                icon="cloud"
            )
        ).add_to(weather_map)

        folium.Circle(
            location=[lat, lon],
            radius=3000,
            color="#2563EB",
            fill=True,
            fill_opacity=0.25
        ).add_to(weather_map)

        st_folium(
            weather_map,
            width=None,
            height=500
        )
