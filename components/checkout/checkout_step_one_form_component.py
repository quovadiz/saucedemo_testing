import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input


class CheckoutStepOneFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = Input(page, "firstName", "First Name")
        self.last_name_input = Input(page, "lastName", "Last Name")
        self.postal_code_input = Input(page, "postalCode", "Postal Code")

    @allure.step("Fill checkout form")
    def fill(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.check_visible()
        self.first_name_input.fill(first_name)

        self.last_name_input.check_visible()
        self.last_name_input.fill(last_name)

        self.postal_code_input.check_visible()
        self.postal_code_input.fill(postal_code)