import re

import allure

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
from tools.routes import AppRoute


class SidebarComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.logout_list_item = SidebarListItemComponent(page, "logout")

    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.dashboard_list_item.check_visible("Dashboard")
        self.courses_list_item.check_visible("Courses")
        self.logout_list_item.check_visible("Logout")

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(AppRoute.DASHBOARD))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(AppRoute.COURSES))

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(AppRoute.LOGIN))
