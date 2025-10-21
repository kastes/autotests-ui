import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_succesfull_authorization(
        self, registration_page: RegistrationPage, login_page: LoginPage, dashboard_page: DashboardPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username="username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username="username")
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize(
        "email,password",
        [
            ("user.name@gnmail.com", "password"),
            ("  ", "password"),
            ("user.name@gnmail.com", "  "),
        ],
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.check_visible()
        login_page.login_form.fill(email, password)
        login_page.login_form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()
