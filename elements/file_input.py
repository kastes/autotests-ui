from pathlib import Path
import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):

    def set_input_files(self, filename: str | Path, nth: int = 0, **kwargs):
        step = f'Set element "{self.type_of}" with name "{self.name}" to value "{filename}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            self.logger.info(step)
            locator.set_input_files(filename)
