"""Seed database with initial data."""

from sqlmodel import Session, delete

from app.config import get_settings
from app.database import get_engine
from app.models import City, WeatherCode

CITIES_DATA = [
    {"name": "Praha", "latitude": 50.0755, "longitude": 14.4378},
    {"name": "Brno", "latitude": 49.1951, "longitude": 16.6068},
    {"name": "Ostrava", "latitude": 49.8209, "longitude": 18.2625},
    {"name": "Plzeň", "latitude": 49.7384, "longitude": 13.3736},
    {"name": "Liberec", "latitude": 50.7671, "longitude": 15.0562},
    {"name": "Olomouc", "latitude": 49.5938, "longitude": 17.2509},
    {"name": "České Budějovice", "latitude": 48.9745, "longitude": 14.4745},
    {"name": "Hradec Králové", "latitude": 50.2104, "longitude": 15.8252},
    {"name": "Pardubice", "latitude": 50.0343, "longitude": 15.7812},
    {"name": "Zlín", "latitude": 49.2331, "longitude": 17.6679},
]

WEATHER_CODES_DATA = [
    {"code": 0, "description": "Clear sky"},
    {"code": 1, "description": "Mainly clear"},
    {"code": 2, "description": "Partly cloudy"},
    {"code": 3, "description": "Overcast"},
    {"code": 45, "description": "Fog"},
    {"code": 48, "description": "Depositing rime fog"},
    {"code": 51, "description": "Light drizzle"},
    {"code": 53, "description": "Moderate drizzle"},
    {"code": 55, "description": "Dense drizzle"},
    {"code": 61, "description": "Slight rain"},
    {"code": 63, "description": "Moderate rain"},
    {"code": 65, "description": "Heavy rain"},
    {"code": 71, "description": "Slight snow"},
    {"code": 73, "description": "Moderate snow"},
    {"code": 75, "description": "Heavy snow"},
    {"code": 80, "description": "Slight rain showers"},
    {"code": 81, "description": "Moderate rain showers"},
    {"code": 82, "description": "Violent rain showers"},
    {"code": 85, "description": "Slight snow showers"},
    {"code": 86, "description": "Heavy snow showers"},
    {"code": 95, "description": "Thunderstorm"},
    {"code": 96, "description": "Thunderstorm with slight hail"},
    {"code": 99, "description": "Thunderstorm with heavy hail"},
]


def main() -> None:
    """Run database seeding."""
    settings = get_settings()
    engine = get_engine(settings)

    with Session(engine) as session:
        # Clear existing data
        session.exec(delete(City))
        session.exec(delete(WeatherCode))

        # Insert fresh data
        for data in CITIES_DATA:
            session.add(City(**data))

        for data in WEATHER_CODES_DATA:
            session.add(WeatherCode(**data))

        session.commit()

    print(f"Seeded {len(CITIES_DATA)} cities")
    print(f"Seeded {len(WEATHER_CODES_DATA)} weather codes")


if __name__ == "__main__":
    main()
