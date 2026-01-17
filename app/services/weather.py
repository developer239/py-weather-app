"""Open-Meteo API client for weather data."""

import httpx
from sqlmodel import Session, select

from app.config import Settings
from app.models import WeatherCode, WeatherData


class WeatherAPIError(Exception):
    """Raised when the weather API request fails."""

    pass


class WeatherService:
    """Service for fetching weather data from Open-Meteo API."""

    def __init__(self, settings: Settings, session: Session) -> None:
        self.base_url = settings.weather_api_url
        self.timeout = settings.weather_api_timeout
        self.session = session

    def _get_weather_description(self, code: int) -> str:
        """Look up weather code description from database."""
        weather_code = self.session.exec(
            select(WeatherCode).where(WeatherCode.code == code)
        ).first()
        return weather_code.description if weather_code else "Unknown"

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
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                data = response.json()

            current = data.get("current_weather")
            if not current:
                raise WeatherAPIError("No current weather data in response")

            weathercode = current["weathercode"]

            return WeatherData(
                temperature=current["temperature"],
                windspeed=current["windspeed"],
                winddirection=current["winddirection"],
                weathercode=weathercode,
                time=current["time"],
                description=self._get_weather_description(weathercode),
            )

        except httpx.HTTPStatusError as e:
            msg = f"API returned error: {e.response.status_code}"
            raise WeatherAPIError(msg) from e
        except httpx.RequestError as e:
            raise WeatherAPIError(f"API request failed: {e}") from e
        except (KeyError, ValueError) as e:
            raise WeatherAPIError(f"Invalid API response: {e}") from e
