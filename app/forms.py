"""Form definitions for the weather application."""

from typing import Any

from flask import g
from flask_wtf import FlaskForm
from sqlmodel import Session, select
from wtforms import SelectField
from wtforms.validators import DataRequired, ValidationError

from app.models import City


class CityValidator:
    """Validator that checks if city is in the allowed list."""

    def __init__(self, message: str | None = None) -> None:
        self.message = message or "Invalid city selected."

    def __call__(self, form: FlaskForm, field: SelectField) -> None:
        """Validate that selected city is in the database."""
        session: Session = g.db_session
        city = session.exec(select(City).where(City.name == field.data)).first()
        if not city:
            raise ValidationError(self.message)


class CityForm(FlaskForm):  # type: ignore[misc]
    """Form for selecting a Czech city."""

    city = SelectField(
        "City",
        validators=[
            DataRequired(message="Please select a city."),
            CityValidator(),
        ],
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        session: Session = g.db_session
        cities = session.exec(select(City).order_by(City.name)).all()
        self.city.choices = [(c.name, c.name) for c in cities]
