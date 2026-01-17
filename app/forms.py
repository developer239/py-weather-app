"""Form definitions for the weather application."""

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

from app.models import CITIES


class CityValidator:
    """Validator that checks if city is in the allowed list."""

    def __init__(self, message: str | None = None) -> None:
        self.message = message or "Invalid city selected."

    def __call__(self, form: FlaskForm, field: SelectField) -> None:
        """Validate that selected city is in the allowed list."""
        valid_names = {city.name for city in CITIES}
        if field.data not in valid_names:
            raise ValueError(self.message)


class CityForm(FlaskForm):  # type: ignore[misc]
    """Form for selecting a Czech city."""

    city = SelectField(
        "City",
        validators=[
            DataRequired(message="Please select a city."),
            CityValidator(),
        ],
        choices=[],  # Populated dynamically in routes
    )
