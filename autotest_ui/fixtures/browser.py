import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_page(request) -> Page:
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()