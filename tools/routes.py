from enum import Enum


class AppRoute(str, Enum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"
    DASHBOARD = "./#/dashboard"
