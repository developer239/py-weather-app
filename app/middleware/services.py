"""Services middleware for dependency injection."""

from flask import Flask, g
from sqlmodel import Session

from app.config import Settings
from app.database import get_engine
from app.services import WeatherService


def init_services_middleware(app: Flask, settings: Settings) -> None:
    """Initialize services middleware for dependency injection."""
    engine = get_engine(settings)

    @app.before_request
    def inject_services() -> None:
        """Inject services into Flask's g object."""
        g.db_session = Session(engine)
        g.weather_service = WeatherService(settings, g.db_session)

    @app.teardown_request
    def cleanup_session(exception: BaseException | None = None) -> None:
        """Close database session after request."""
        session: Session | None = g.pop("db_session", None)
        if session is not None:
            session.close()
