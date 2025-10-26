import allure

from playwright.sync_api import expect, Locator, Page


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name

    @property
    def type_of(self) -> str:
        return self.__class__.__name__

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator: str = self.locator.format(nth, **kwargs)
        with allure.step(f'Get locator with data-testid="{locator}" at index="{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Checking that element "{self.type_of}" with name "{self.name}" is visible'):
            locator: Locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Checking that element "{self.type_of}" with name "{self.name}" have text "{text}"'):
            locator: Locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

    def click(self, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Clicking on element "{self.type_of}" with name "{self.name}"'):
            locator: Locator = self.get_locator(nth, **kwargs)
            locator.click()

    def hover(self, nth: int = 0, **kwargs) -> None:
        with allure.step(f'Hovering on element "{self.type_of}" with name "{self.name}"'):
            locator: Locator = self.get_locator(nth, **kwargs)
            locator.hover()
