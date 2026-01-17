"""Repository service for database access."""

from sqlmodel import Session, select

from app.models import City, WeatherCode


class Repository:
    """Unified repository for all database operations."""

    def __init__(self, session: Session) -> None:
        self.session = session

    # City methods

    def get_all_cities(self) -> list[City]:
        """Get all cities ordered by name."""
        return list(self.session.exec(select(City).order_by(City.name)).all())

    def get_city_by_name(self, name: str) -> City | None:
        """Find city by name."""
        return self.session.exec(select(City).where(City.name == name)).first()

    # WeatherCode methods

    def get_weather_description(self, code: int) -> str:
        """Get weather description by code."""
        weather_code = self.session.exec(
            select(WeatherCode).where(WeatherCode.code == code)
        ).first()
        return weather_code.description if weather_code else "Unknown"
