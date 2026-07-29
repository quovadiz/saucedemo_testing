from enum import Enum


class AppRoute(str, Enum):
    INVENTORY_URL = "./inventory.html"
    CART_URL = "./cart.html"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    CREATE_COURSE = "./#/courses/create"