import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, filename: str, nth: int = 0, **kwargs):
        with allure.step(f'Set element "{self.type_of}" with name "{self.name}" to value "{filename}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(filename)
