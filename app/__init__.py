"""Flask application factory."""

import logging

from flask import Flask

from app.config import Settings, get_settings
from app.errors import init_error_handlers
from app.middleware import (
    init_logging_middleware,
    init_security_middleware,
    init_services_middleware,
)
from app.routes import health_bp, weather_bp


def configure_logging() -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def create_app(settings: Settings | None = None) -> Flask:
    """Create and configure the Flask application."""
    configure_logging()

    if settings is None:
        settings = get_settings()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.secret_key

    # Initialize middleware
    init_logging_middleware(app)
    init_security_middleware(app)
    init_services_middleware(app, settings)

    # Initialize error handlers
    init_error_handlers(app)

    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(weather_bp)

    return app
