import allure

from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Textarea(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = super().get_locator(nth, **kwargs)
        with allure.step('Get a nested locator ("textarea").first'):
            locator = locator.locator("textarea").first
            return locator

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill element "{self.type_of}" with name "{self.name}" to value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that element "{self.type_of}" with name "{self.name}" have value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
