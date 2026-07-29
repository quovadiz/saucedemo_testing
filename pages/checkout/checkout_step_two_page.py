import allure
from playwright.sync_api import Page

from components.checkout.checkout_ste_two_form_component import CheckoutStepTwoFormComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Подключаем компонент элементов для Overview
        self.checkout_item = CheckoutStepTwoFormComponent(page)

        self.subtotal_label = Text(page, "[data-test='subtotal-label']", "Subtotal Label")
        self.tax_label = Text(page, "[data-test='tax-label']", "Tax Label")
        self.total_label = Text(page, "[data-test='total-label']", "Total Label")
        self.finish_btn = Button(page, "[data-test='finish']", "Finish button")

    @allure.step("Click 'Finish' button to complete order")
    def click_finish(self):
        self.finish_btn.check_visible()
        self.finish_btn.click()

    @allure.step("Check product item details on checkout overview at index '{index}'")
    def check_product_in_overview(self, index: int, quantity: str, title: str, price: str, description: str):
        self.checkout_item.check_visible(
            index=index, quantity=quantity, title=title, price=price, description=description
        )