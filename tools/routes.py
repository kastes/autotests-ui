from enum import Enum


class AppRoute(str, Enum):
    LOGIN = r"./#/auth/login"
    REGISTRATION = r"./#/auth/registration"
    COURSES = r"./#/courses"
    COURSES_CREATE = r"./#/courses/create"
    DASHBOARD = r"./#/dashboard"
