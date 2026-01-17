"""Weather code model for WMO weather interpretation codes."""

from sqlmodel import Field, SQLModel


class WeatherCode(SQLModel, table=True):
    """WMO weather interpretation code."""

    __tablename__ = "weather_codes"

    code: int = Field(primary_key=True)
    description: str
