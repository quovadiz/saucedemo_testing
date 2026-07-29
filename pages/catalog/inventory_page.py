import allure
from playwright.sync_api import Page

from components.catalog.product_card_componnet import ProductCardComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_card = ProductCardComponent(page)
        self.cart_button = Button(page, "[data-test='shopping-cart-link']", "Shopping Cart")
        self.cart_badge = Text(page, "[data-test='shopping-cart-badge']", "Cart Badge")

    @allure.step("Add product to cart by index '{index}'")
    def add_product_to_cart(self, index: int = 0):
        self.product_card.add_to_cart(index=index)

    @allure.step("Remove product from cart by index '{index}'")
    def remove_product_from_cart(self, index: int = 0):
        self.product_card.remove_from_cart(index=index)

    @allure.step("Go to shopping cart")
    def go_to_cart(self):
        self.cart_button.click()

    @allure.step("Check cart badge has count '{expected_count}'")
    def check_cart_badge_count(self, expected_count: str):
        self.cart_badge.check_visible()
        self.cart_badge.check_have_text(expected_count)

    @allure.step("Check that cart badge is not visible (empty cart)")
    def check_cart_badge_is_absent(self):
        self.cart_badge.check_hidden()
