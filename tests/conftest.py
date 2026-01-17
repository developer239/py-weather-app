"""Pytest fixtures for E2E tests."""

import os
import threading
import time
from collections.abc import Generator

import pytest
from playwright.sync_api import Page
from sqlmodel import Session, text

from app import create_app
from app.config import get_settings
from app.database import get_engine


def check_database_connection() -> None:
    """Check database is reachable, raise clear error if not."""
    settings = get_settings()
    try:
        engine = get_engine(settings)
        with Session(engine) as session:
            session.exec(text("SELECT 1"))  # type: ignore[call-overload]
    except Exception:
        pytest.exit(
            f"\n\nDatabase connection failed!\n"
            f"   Host: {settings.pghost}:{settings.pgport}\n"
            f"   Database: {settings.pgdatabase}\n"
            f"   \n"
            f"   Make sure PostgreSQL is running: docker compose up -d database\n"
            f"   \n",
            returncode=1,
        )


@pytest.fixture(scope="session")
def app_url() -> Generator[str, None, None]:
    """
    Get app URL - either from environment or start local server.
    
    For CI: Set APP_URL env var to test against running container.
    For local: Starts Flask dev server automatically.
    """
    external_url = os.environ.get("APP_URL")

    if external_url:
        # CI mode: use external server
        yield external_url
    else:
        # Local mode: check DB and start server
        check_database_connection()

        app = create_app()
        server = threading.Thread(
            target=lambda: app.run(port=5001, use_reloader=False),
            daemon=True,
        )
        server.start()
        time.sleep(0.5)
        yield "http://localhost:5001"


@pytest.fixture
def test_page(app_url: str, page: Page) -> Page:
    """Page fixture with base URL configured."""
    page.goto(app_url)
    return page
