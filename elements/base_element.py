from playwright.sync_api import expect, Locator, Page


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name

    def get_locator(self, **kwargs) -> Locator:
        locator: str = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def check_visible(self, **kwargs) -> None:
        locator: Locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs) -> None:
        locator: Locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)

    def click(self, **kwargs) -> None:
        locator: Locator = self.get_locator(**kwargs)
        locator.click()

    def hover(self, **kwargs) -> None:
        locator: Locator = self.get_locator(**kwargs)
        locator.hover()
