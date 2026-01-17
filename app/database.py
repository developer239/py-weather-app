"""Database engine and session management."""

from collections.abc import Generator

from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from app.config import Settings


def get_engine(settings: Settings) -> Engine:
    """Create database engine from settings."""
    return create_engine(settings.database_url, echo=settings.debug)


def get_session(settings: Settings) -> Generator[Session, None, None]:
    """Yield a database session."""
    engine = get_engine(settings)
    with Session(engine) as session:
        yield session
