import pytest

from typing import Generator

from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initiliaze_playwright_page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
    registration_page.click_registration_button()

    context.storage_state(path="browser-state.json")

    browser.close()


@pytest.fixture
def chromium_page(playwright: Playwright, request: SubRequest) -> Generator[Page]:
    yield from initiliaze_playwright_page(playwright=playwright, test_name=request.node.name)


@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state: None, playwright: Playwright, request: SubRequest
) -> Generator[Page]:
    yield from initiliaze_playwright_page(
        playwright=playwright, test_name=request.node.name, storage_state="browser-state.json"
    )
