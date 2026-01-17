"""Open-Meteo API client for weather data."""

import os
from dataclasses import dataclass

import requests


class WeatherAPIError(Exception):
    """Raised when the weather API request fails."""

    pass


WEATHER_CODES: dict[int, str] = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


@dataclass
class WeatherData:
    """Weather data container."""

    temperature: float
    windspeed: float
    winddirection: int
    weathercode: int
    time: str

    @property
    def description(self) -> str:
        """Get human-readable weather description."""
        return WEATHER_CODES.get(self.weathercode, "Unknown")

    @property
    def wind_direction_text(self) -> str:
        """Convert wind direction degrees to cardinal direction."""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(self.winddirection / 45) % 8
        return directions[index]


class WeatherService:
    """Service for fetching weather data from Open-Meteo API."""

    def __init__(self) -> None:
        self.base_url = os.getenv("WEATHER_API_URL", "https://api.open-meteo.com/v1")

    def get_current_weather(self, latitude: float, longitude: float) -> WeatherData:
        """
        Fetch current weather for given coordinates.

        Args:
            latitude: Location latitude
            longitude: Location longitude

        Returns:
            WeatherData object with current conditions

        Raises:
            WeatherAPIError: If the API request fails
        """
        url = f"{self.base_url}/forecast"
        params: dict[str, str | float] = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": "true",
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            current = data.get("current_weather")
            if not current:
                raise WeatherAPIError("No current weather data in response")

            return WeatherData(
                temperature=current["temperature"],
                windspeed=current["windspeed"],
                winddirection=current["winddirection"],
                weathercode=current["weathercode"],
                time=current["time"],
            )

        except requests.RequestException as e:
            raise WeatherAPIError(f"API request failed: {e}") from e
        except (KeyError, ValueError) as e:
            raise WeatherAPIError(f"Invalid API response: {e}") from e
