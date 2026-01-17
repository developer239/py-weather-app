"""Flask application factory."""

import os

from dotenv import load_dotenv
from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application."""
    load_dotenv()

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["WEATHER_API_URL"] = os.getenv(
        "WEATHER_API_URL", "https://api.open-meteo.com/v1"
    )

    from app import routes

    app.register_blueprint(routes.bp)

    return app
