import allure
import pytest

from pages.authentication.login_page import LoginPage
from tools.routes import AppRoute


@allure.epic("Authorization")
@allure.feature("Login Feature")
@pytest.mark.regression
@pytest.mark.auth
class TestAuthorization:
    @allure.story("Successful Login")
    @allure.title("Successful login with standard user credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, login_page: LoginPage):
        login_page.visit(AppRoute.BASE_URL)
        login_page.login_form.fill(username="standard_user", password="secret_sauce")
        login_page.click_login_button()
        login_page.check_current_url(AppRoute.INVENTORY_URL)

    @allure.story("Failed Login / Restricted User")
    @allure.title("Login attempt with locked out user displays error message")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page:LoginPage):
        login_page.visit(AppRoute.BASE_URL)
        login_page.login_form.fill(username="locked_out_user", password="secret_sauce")
        login_page.click_login_button()
        login_page.check_visible_locked_out_error_message()
        login_page.check_current_url(AppRoute.BASE_URL)
