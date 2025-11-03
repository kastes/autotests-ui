import allure

from playwright.sync_api import expect, Page
from typing import Pattern

from tools.logger import get_logger


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern: "{expected_url.pattern}"'
        with allure.step(step):
            self.logger.info(step)
            expect(self.page).to_have_url(expected_url)
