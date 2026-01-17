"""Route blueprints for the weather application."""

from app.routes.health import bp as health_bp
from app.routes.weather import bp as weather_bp

__all__ = ["health_bp", "weather_bp"]
