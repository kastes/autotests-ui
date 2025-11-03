import allure

from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that element "{self.type_of}" with name "{self.name}" is enabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that element "{self.type_of}" with name "{self.name}" is disabled'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            expect(locator).to_be_disabled()
