import allure


@allure.step("Start browser {name}")  # передача параметра в декоратор
def start_browser(name: str):
    pass


def close_browser():
    with allure.step("Close browser"):
        pass


def test_feature():
    with allure.step("Open browser"):
        with allure.step("Search browser"):
            pass
        with allure.step("Setup browser"):
            pass
        pass

    start_browser("chrom")

    close_browser()


class TestFeature:
    @allure.step("Open class browser")
    def test_open_browser_feature(self):
        with allure.step("Search browser"):
            pass
        with allure.step("Setup browser"):
            pass
        pass
