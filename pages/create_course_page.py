from playwright.sync_api import expect, Page

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.views.image_upload_widget_component import EmptyViewComponent, ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SideBarComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier="create-course-preview")
        self.create_course_form = CreateCourseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, identifier="create-course-exercises")
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)

        # заголовок и кнопка создания курса
        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("create-course-toolbar-create-course-button")

        # блок добавления упражнений
        self.exercises_title = page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.create_exercise_button = page.get_by_test_id("create-course-exercises-box-toolbar-create-exercise-button")

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text("Create course")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text("Exercises")

    def check_visible_create_exercise_button(self):
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises", description='Click on "Create exercise" button to create new exercise'
        )
