"""Weather data model for API responses."""

from pydantic import BaseModel


class WeatherData(BaseModel):
    """Weather data from Open-Meteo API."""

    temperature: float
    windspeed: float
    winddirection: int
    weathercode: int
    time: str
    description: str = "Unknown"

    @property
    def wind_direction_text(self) -> str:
        """Convert wind direction degrees to cardinal direction."""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(self.winddirection / 45) % 8
        return directions[index]
