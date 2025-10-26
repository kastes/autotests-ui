import allure

from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.name = identifier.capitalize()
        self.icon = Icon(page, f"{identifier}-drawer-list-item-icon", self.name + " icon")
        self.title = Text(page, f"{identifier}-drawer-list-item-title-text", self.name + " title")
        self.button = Button(page, f"{identifier}-drawer-list-item-button", self.name + " button")

    @allure.step("Check visible {title} sidebar list item")
    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        with allure.step(f'Navigate from sidebar to "{self.name}" page'):
            self.button.click()
            self.check_current_url(expected_url)
