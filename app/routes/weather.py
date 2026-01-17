"""Weather route handlers."""

from flask import Blueprint, Response, flash, g, jsonify, render_template

from app.forms import CityForm
from app.middleware import validate_form
from app.models import CITIES, get_city_by_name
from app.services import WeatherAPIError, WeatherService

bp = Blueprint("weather", __name__)


@bp.route("/")
def index() -> str:
    """Main page with city selector."""
    form = CityForm()
    return render_template("index.html", form=form, weather=None)


@bp.route("/api/cities")
def api_cities() -> Response:
    """Return JSON list of available Czech cities."""
    return jsonify({"cities": [city.model_dump() for city in CITIES]})


@bp.route("/weather", methods=["POST"])
@validate_form(CityForm, on_error="weather.index")
def weather(form: CityForm) -> str:
    """Fetch and display weather for selected city."""
    city = get_city_by_name(form.city.data)
    weather_data = None
    selected_city = None

    if city:
        selected_city = city
        weather_service: WeatherService = g.weather_service

        try:
            weather_data = weather_service.get_current_weather(
                latitude=city.latitude,
                longitude=city.longitude,
            )
        except WeatherAPIError as e:
            flash(f"Could not fetch weather data: {e}", "error")
    else:
        flash("Invalid city selected.", "error")

    return render_template(
        "index.html",
        form=form,
        weather=weather_data,
        selected_city=selected_city,
    )
