import allure

from playwright.sync_api import expect, Locator, Page

from tools.logger import get_logger


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name
        self.logger = get_logger(self.__module__)

    @property
    def type_of(self) -> str:
        return self.__class__.__name__

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator: str = self.locator.format(nth, **kwargs)
        step = f'Get locator with data-testid="{locator}" at index="{nth}"'
        with allure.step(step):
            self.logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        step = f'Checking that element "{self.type_of}" with name "{self.name}" is visible'
        with allure.step(step):
            locator: Locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        step = f'Checking that element "{self.type_of}" with name "{self.name}" have text "{text}"'
        with allure.step(step):
            locator: Locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            expect(locator).to_have_text(text)

    def click(self, nth: int = 0, **kwargs) -> None:
        step = f'Clicking on element "{self.type_of}" with name "{self.name}"'
        with allure.step(step):
            locator: Locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            locator.click()

    def hover(self, nth: int = 0, **kwargs) -> None:
        step = f'Hovering on element "{self.type_of}" with name "{self.name}"'
        with allure.step(step):
            locator: Locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            locator.hover()
