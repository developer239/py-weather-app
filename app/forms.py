"""Form definitions for the weather application."""

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired


class CityForm(FlaskForm):  # type: ignore[misc]
    """Form for selecting a Czech city."""

    city = SelectField(
        "City",
        validators=[DataRequired(message="Please select a city.")],
        choices=[],  # Populated dynamically in routes
    )
