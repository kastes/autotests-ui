import allure

from playwright.sync_api import expect
from ui_coverage_tool import ActionType  # type: ignore

from elements.base_element import BaseElement


class Input(BaseElement):

    def get_locator(self, nth: int = 0, **kwargs):
        locator = super().get_locator(nth, **kwargs)
        step = 'Get a nested locator "input"'
        with allure.step(step):
            self.logger.info(step)
            locator = locator.locator("input")
            return locator

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"{super().get_raw_locator(nth, **kwargs)}//input"

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill element "{self.type_of}" with name "{self.name}" to value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            locator.fill(value)

        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that element "{self.type_of}" with name "{self.name}" have value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            expect(locator).to_have_value(value)

        self.track_coverage(ActionType.VALUE, nth, **kwargs)
