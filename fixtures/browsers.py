import allure
import pytest

from typing import Generator

from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage


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
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="./videos")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()

    allure.attach.file(f"./tracing/{request.node.name}.zip", name="trace", extension="zip")
    assert (
        page.video is not None
    )  # без этой проверки mypy выдаёт ошибку, т.к. тип свойства page.video - Union[Video, None]
    allure.attach.file(page.video.path(), name="video", attachment_type=AttachmentType.WEBM)


@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state: None, playwright: Playwright, request: SubRequest
) -> Generator[Page]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json", record_video_dir="./videos")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()

    allure.attach.file(f"./tracing/{request.node.name}.zip", name="trace", extension="zip")
    if (
        page.video is not None
    ):  # без этой проверки mypy выдаёт ошибку, т.к. тип свойства page.video - Union[Video, None]
        allure.attach.file(page.video.path(), name="video", attachment_type=AttachmentType.WEBM)
