"""Services middleware for dependency injection."""

from flask import Flask, g

from app.config import Settings
from app.services import WeatherService


def init_services_middleware(app: Flask, settings: Settings) -> None:
    """Initialize services middleware for dependency injection."""

    @app.before_request
    def inject_services() -> None:
        """Inject services into Flask's g object."""
        g.weather_service = WeatherService(settings)
