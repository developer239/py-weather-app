"""City model for Czech cities."""

from sqlmodel import Field, SQLModel


class City(SQLModel, table=True):
    """Czech city with coordinates."""

    __tablename__ = "cities"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    latitude: float
    longitude: float
