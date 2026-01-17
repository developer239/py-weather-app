"""Pytest fixtures for E2E tests."""

import threading
import time
from collections.abc import Generator

import pytest
from playwright.sync_api import Page

from app import create_app


@pytest.fixture(scope="session")
def app_server() -> Generator[str, None, None]:
    """Start Flask server in background thread."""
    app = create_app()
    server = threading.Thread(
        target=lambda: app.run(port=5001, use_reloader=False),
        daemon=True,
    )
    server.start()
    time.sleep(0.5)
    yield "http://localhost:5001"


@pytest.fixture
def test_page(app_server: str, page: Page) -> Page:
    """Page fixture with base URL configured."""
    page.goto(app_server)
    return page
