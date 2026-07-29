import pytest

from config import settings
from pages.authentication.login_page import LoginPage
from tools.routes import AppRoute


@pytest.mark.regression
class TestAuthorization:
    def test_successful_login(self, login_page: LoginPage):
        login_page.visit(settings.base_url)
        login_page.login_form.fill(username="standard_user", password="secret_sauce")
        login_page.click_login_button()
        login_page.check_current_url(AppRoute.INVENTORY)

    def test_wrong_email_or_password_authorization(self, login_page:LoginPage):
        login_page.visit(settings.base_url)
        login_page.login_form.fill(username="locked_out_user", password="secret_sauce")
        login_page.click_login_button()
        login_page.check_visible_locked_out_error_message()
        login_page.check_current_url(settings.base_url)
