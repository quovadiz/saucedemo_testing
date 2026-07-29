import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button


class MenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.burger_btn = Button(page, "react-burger-menu-btn", "Burger menu button")
        self.logout_link = Button(page, "logout-sidebar-link", "Logout sidebar link")
        self.all_items_link = Button(page, "inventory-sidebar-link", "All Items sidebar link")
        self.reset_link = Button(page, "reset-sidebar-link", "Reset App State sidebar link")

    @allure.step("Perform logout via burger menu")
    def logout(self):
        self.burger_btn.check_visible()
        self.burger_btn.click()

        self.logout_link.check_visible()
        self.logout_link.click()