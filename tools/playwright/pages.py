import allure

from typing import Generator

from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, Page

from config import settings


def initiliaze_playwright_page(playwright: Playwright, test_name: str, storage_state=None) -> Generator[Page]:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state=storage_state, record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f"{test_name}.zip"))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f"{test_name}.zip"), name="trace", extension="zip")
    if (
        page.video is not None
    ):  # без этой проверки mypy выдаёт ошибку, т.к. тип свойства page.video - Union[Video, None]. Ещё можно
        # использовать assert page.video is not None или assert isinstance(page.video, Video)
        allure.attach.file(page.video.path(), name="video", attachment_type=AttachmentType.WEBM)
