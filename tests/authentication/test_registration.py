import allure
import pytest

from allure_commons.types import Severity
from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.routes import AppRoute
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_succesfull_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form.check_visible()
        registration_page.registration_form.fill(
            email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password
        )

        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from registration page to login page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_registration_to_authorization(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.click_login_link()
        login_page.login_form.check_visible()
