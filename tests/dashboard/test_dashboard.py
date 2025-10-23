import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
class TestDashboard:
    @allure.title("Displaying dashboard")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
        )

        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()

        dashboard_page_with_state.check_visible_activities_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_students_chart()
