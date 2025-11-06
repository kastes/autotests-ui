import pytest

from typing import Generator

from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from config import settings
from pages.authentication.registration_page import RegistrationPage
from tools.routes import AppRoute
from tools.playwright.pages import initiliaze_playwright_page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)

    page.close()
    context.close()
    browser.close()


@pytest.fixture(params=settings.browsers)
def browser_page(playwright: Playwright, request: SubRequest) -> Generator[Page]:
    yield from initiliaze_playwright_page(
        playwright=playwright, test_name=request.node.name, browser_type=request.param
    )


@pytest.fixture(params=settings.browsers)
def browser_page_with_state(
    initialize_browser_state: None, playwright: Playwright, request: SubRequest
) -> Generator[Page]:
    yield from initiliaze_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file,
    )
