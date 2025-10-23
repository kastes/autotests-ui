import allure
import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    def test_succesfull_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        registration_page.registration_form.check_visible()
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")

        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from registration page to login page")
    def test_navigate_from_registration_to_authorization(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.click_login_link()
        login_page.login_form.check_visible()
