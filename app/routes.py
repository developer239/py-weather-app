"""Route handlers for the weather application."""

from flask import Blueprint, render_template, request, jsonify, flash

from app.forms import CityForm
from app.services.weather_api import WeatherService, WeatherAPIError

bp = Blueprint("main", __name__)

# Czech cities with coordinates
CITIES = [
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


def get_city_by_name(name: str) -> dict | None:
    """Find a city by name from the predefined list."""
    for city in CITIES:
        if city["name"] == name:
            return city
    return None


@bp.route("/")
def index():
    """Main page with city selector and weather display."""
    form = CityForm()
    form.city.choices = [(city["name"], city["name"]) for city in CITIES]
    return render_template("index.html", form=form, weather=None)


@bp.route("/api/cities")
def api_cities():
    """Return JSON list of available Czech cities."""
    return jsonify({"cities": CITIES})


@bp.route("/weather", methods=["POST"])
def weather():
    """Fetch and display weather for selected city."""
    form = CityForm()
    form.city.choices = [(city["name"], city["name"]) for city in CITIES]
    
    weather_data = None
    selected_city = None

    if form.validate_on_submit():
        city_name = form.city.data
        city = get_city_by_name(city_name)
        
        if city:
            selected_city = city
            weather_service = WeatherService()
            
            try:
                weather_data = weather_service.get_current_weather(
                    latitude=city["latitude"],
                    longitude=city["longitude"]
                )
            except WeatherAPIError as e:
                flash(f"Could not fetch weather data: {e}", "error")
        else:
            flash("Invalid city selected.", "error")
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{error}", "error")

    return render_template(
        "index.html", 
        form=form, 
        weather=weather_data, 
        selected_city=selected_city
    )
