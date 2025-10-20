from playwright.sync_api import expect, Locator, Page


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator: str = self.locator.format(nth, **kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        locator: Locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        locator: Locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)

    def click(self, nth: int = 0, **kwargs) -> None:
        locator: Locator = self.get_locator(nth, **kwargs)
        locator.click()

    def hover(self, nth: int = 0, **kwargs) -> None:
        locator: Locator = self.get_locator(nth, **kwargs)
        locator.hover()
