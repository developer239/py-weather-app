"""End-to-end tests for the weather application."""

from playwright.sync_api import Page, expect


def test_user_can_get_weather_for_city(test_page: Page) -> None:
    """User selects a city and sees weather data."""
    # Assert page loads with title and form
    expect(test_page).to_have_title("Czech Weather")
    expect(test_page.locator("select")).to_be_visible()
    expect(test_page.get_by_role("button", name="Get Weather")).to_be_visible()

    # Select city and submit
    test_page.locator("select").select_option("Praha")
    test_page.get_by_role("button", name="Get Weather").click()

    # Assert weather card appears with temperature
    expect(test_page.locator("article")).to_be_visible()
    expect(test_page.locator("article")).to_contain_text("Praha")
    expect(test_page.locator("article")).to_contain_text("°C")
