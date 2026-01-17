"""Application configuration using Pydantic Settings."""

from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Flask
    secret_key: str = "dev-secret-key-change-in-production"
    debug: bool = False

    # Weather API
    weather_api_url: str = "https://api.open-meteo.com/v1"
    weather_api_timeout: int = 10

    # Database (using PG* environment variables)
    pghost: str = "localhost"
    pgport: int = 5432
    pguser: str = "postgres"
    pgpassword: str = "postgres"
    pgdatabase: str = "czech_weather"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def database_url(self) -> str:
        """Build PostgreSQL connection URL."""
        return (
            f"postgresql+psycopg://{self.pguser}:{self.pgpassword}"
            f"@{self.pghost}:{self.pgport}/{self.pgdatabase}"
        )


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
