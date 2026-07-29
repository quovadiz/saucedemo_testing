import allure
from playwright.sync_api import Page

from components.cart.cart_component import CartItemComponent
from elements.button import Button
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_item = CartItemComponent(page)

        self.continue_shopping_btn = Button(
            page, "[data-test='continue-shopping']", "Continue Shopping button"
        )
        self.checkout_btn = Button(page, "[data-test='checkout']", "Checkout button")

    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping(self):
        self.continue_shopping_btn.check_visible()
        self.continue_shopping_btn.click()

    @allure.step("Click 'Checkout' button")
    def click_checkout(self):
        self.checkout_btn.check_visible()
        self.checkout_btn.click()

    @allure.step("Remove product from cart at index '{index}'")
    def remove_product(self, index: int = 0):
        self.cart_item.remove_from_cart(index=index)

    @allure.step("Check cart item at index '{index}' visibility and data")
    def check_cart_item(self, index: int, quantity: str, title: str, price: str, description: str):
        self.cart_item.check_visible(index=index, quantity=quantity, title=title, price=price, description=description)

    @allure.step("Check that cart item at index '{index}' is absent")
    def check_cart_item_is_absent(self, index: int = 0):
        self.cart_item.check_item_is_not_visible(index=index)