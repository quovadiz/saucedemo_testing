import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = Input(page, "username", "Username")
        self.password_input = Input(page, "password", "Password")

    @allure.step("Fill login form")
    def fill(self, username: str, password: str):
        self.username_input.check_visible()
        self.username_input.fill(username)

        self.password_input.check_visible()
        self.password_input.fill(password)

    @allure.step("Check visible login form")
    def check_visible(self, email: str, password: str):
        self.username_input.check_visible()
        self.username_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)