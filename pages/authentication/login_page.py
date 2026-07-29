import allure
from playwright.sync_api import Page

from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, "login-button", "Login")
        self.locked_out_user_message = Text(
            page, "error", "Locked out user message"
        )

    def click_login_button(self):
        self.login_button.click()

    @allure.step("Check visible locked out message")
    def check_visible_locked_out_error_message(self):
        self.locked_out_user_message.check_visible()
        self.locked_out_user_message.check_have_text("Epic sadface: Sorry, this user has been locked out.")
