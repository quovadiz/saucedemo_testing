import allure
import pytest

from components.menu.menu_component import MenuComponent
from pages.authentication.login_page import LoginPage
from pages.catalog.inventory_page import InventoryPage
from tools.routes import AppRoute


@allure.epic("Authentication")
@allure.feature("Logout and Relogin Feature")
@pytest.mark.regression
@pytest.mark.auth
class TestRelogin:
    @allure.story("Logout and Login with Another User")
    @allure.title("Successful logout and relogin with performance glitch user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_and_relogin_with_another_user(self, login_page: LoginPage):
        inventory_page = InventoryPage(login_page.page)
        menu = MenuComponent(login_page.page)

        login_page.visit(AppRoute.BASE_URL)
        login_page.login_form.fill(username="standard_user", password="secret_sauce")
        login_page.click_login_button()
        login_page.check_current_url(AppRoute.INVENTORY_URL)

        menu.logout()
        login_page.check_current_url(AppRoute.BASE_URL)

        login_page.login_form.fill(username="performance_glitch_user", password="secret_sauce")
        login_page.click_login_button()
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)