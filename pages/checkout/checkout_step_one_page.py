import allure
from playwright.sync_api import Page

from components.checkout.checkout_step_one_form_component import CheckoutStepOneFormComponent
from elements.button import Button
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.checkout_form = CheckoutStepOneFormComponent(page)
        self.continue_btn = Button(page, "[data-test='continue']", "Continue button")

    @allure.step("Fill checkout form with First Name '{first_name}', Last Name '{last_name}', Postal Code '{postal_code}' and continue")
    def fill_form_and_continue(self, first_name: str, last_name: str, postal_code: str):
        self.checkout_form.fill(first_name, last_name, postal_code)
        self.continue_btn.check_visible()
        self.continue_btn.click()