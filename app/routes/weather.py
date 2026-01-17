"""Weather route handlers."""

from flask import Blueprint, Response, flash, g, jsonify, render_template

from app.forms import CityForm
from app.models import CITIES, get_city_by_name
from app.services import WeatherAPIError, WeatherService

bp = Blueprint("weather", __name__)


def _get_city_choices() -> list[tuple[str, str]]:
    """Get city choices for the form."""
    return [(city.name, city.name) for city in CITIES]


@bp.route("/")
def index() -> str:
    """Main page with city selector."""
    form = CityForm()
    form.city.choices = _get_city_choices()  # type: ignore[assignment]
    return render_template("index.html", form=form, weather=None)


@bp.route("/api/cities")
def api_cities() -> Response:
    """Return JSON list of available Czech cities."""
    return jsonify({"cities": [city.model_dump() for city in CITIES]})


@bp.route("/weather", methods=["POST"])
def weather() -> str:
    """Fetch and display weather for selected city."""
    form = CityForm()
    form.city.choices = _get_city_choices()  # type: ignore[assignment]

    weather_data = None
    selected_city = None

    if form.validate_on_submit():
        city_name = form.city.data
        city = get_city_by_name(city_name)

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
    else:
        for errors in form.errors.values():
            for error in errors:
                flash(f"{error}", "error")

    return render_template(
        "index.html",
        form=form,
        weather=weather_data,
        selected_city=selected_city,
    )
