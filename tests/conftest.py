import pytest

from playwright.sync_api import Playwright, Page
from typing import Generator


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
