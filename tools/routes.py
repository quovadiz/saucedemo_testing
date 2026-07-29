from enum import Enum


class AppRoute(str, Enum):
    INVENTORY_URL = "./inventory.html"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    CREATE_COURSE = "./#/courses/create"