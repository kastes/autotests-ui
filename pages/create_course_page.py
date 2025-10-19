from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.image_upload_widget_component import EmptyViewComponent, ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SideBarComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier="create-course-preview")
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, identifier="create-course-exercises")
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises", description='Click on "Create exercise" button to create new exercise'
        )
