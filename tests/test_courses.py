import pytest

from playwright.sync_api import expect

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    courses_empty_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_empty_icon).to_be_visible()

    courses_empty_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_empty_title).to_be_visible()
    expect(courses_empty_title).to_have_text("There is no results")

    courses_empty_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_empty_description).to_be_visible()
    expect(courses_empty_description).to_have_text("Results from the load test pipeline will be displayed here")


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")  # 1
    create_course_page.check_visible_create_course_title()  # 2
    create_course_page.check_disabled_create_course_button()  # 3
    create_course_page.check_visible_image_preview_empty_view()  # 4
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)  # 5
    create_course_page.check_visible_create_course_form(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )  # 6
    create_course_page.check_visible_exercises_title()  # 7
    create_course_page.check_visible_create_exercise_button()  # 8
    create_course_page.check_visible_exercises_empty_view()  # 9
    create_course_page.upload_preview_image("./testdata/files/playwright-logo.png")  # 10
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)  # 11
    create_course_page.check_visible_preview_image()
    create_course_page.fill_create_course_form(
        title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10"
    )  # 12
    create_course_page.click_create_course_button()  # 13
    courses_list_page.check_visible_courses_title()  # 14
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )  # 15
