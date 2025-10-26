import allure

from playwright.sync_api import expect, Page
from typing import Pattern


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern: "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
