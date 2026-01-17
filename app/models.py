"""Pydantic models for the weather application."""

from pydantic import BaseModel, computed_field


class City(BaseModel):
    """Czech city with coordinates."""

    name: str
    latitude: float
    longitude: float


class WeatherData(BaseModel):
    """Weather data from Open-Meteo API."""

    temperature: float
    windspeed: float
    winddirection: int
    weathercode: int
    time: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def description(self) -> str:
        """Get human-readable weather description."""
        return WEATHER_CODES.get(self.weathercode, "Unknown")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def wind_direction_text(self) -> str:
        """Convert wind direction degrees to cardinal direction."""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(self.winddirection / 45) % 8
        return directions[index]


# WMO Weather interpretation codes
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

# Predefined Czech cities
CITIES: list[City] = [
    City(name="Praha", latitude=50.0755, longitude=14.4378),
    City(name="Brno", latitude=49.1951, longitude=16.6068),
    City(name="Ostrava", latitude=49.8209, longitude=18.2625),
    City(name="Plzeň", latitude=49.7384, longitude=13.3736),
    City(name="Liberec", latitude=50.7671, longitude=15.0562),
    City(name="Olomouc", latitude=49.5938, longitude=17.2509),
    City(name="České Budějovice", latitude=48.9745, longitude=14.4745),
    City(name="Hradec Králové", latitude=50.2104, longitude=15.8252),
    City(name="Pardubice", latitude=50.0343, longitude=15.7812),
    City(name="Zlín", latitude=49.2331, longitude=17.6679),
]


def get_city_by_name(name: str) -> City | None:
    """Find a city by name from the predefined list."""
    for city in CITIES:
        if city.name == name:
            return city
    return None
