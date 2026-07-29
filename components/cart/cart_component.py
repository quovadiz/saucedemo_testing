import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CartItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.quantity = Text(page, "[data-test='item-quantity']", "Quantity")
        self.title = Text(page, "[data-test='inventory-item-name']", "Title")
        self.description = Text(page, "[data-test='inventory-item-desc']", "Description")
        self.price = Text(page, "[data-test='inventory-item-price']", "Price")
        self.remove_btn = Button(page, "[data-test^='remove']", "Remove button")

    @allure.step('Check visible cart item at index "{index}"')
    def check_visible(self, index: int, quantity: str, title: str, price: str, description: str):
        self.quantity.check_visible(nth=index)
        self.quantity.check_have_text(quantity, nth=index)

        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        self.price.check_visible(nth=index)
        self.price.check_have_text(price, nth=index)

        self.description.check_visible(nth=index)
        self.description.check_have_text(description, nth=index)

        self.remove_btn.check_visible(nth=index)

    @allure.step("Remove product from cart at index '{index}'")
    def remove_from_cart(self, index: int = 0):
        self.remove_btn.check_visible(nth=index)
        self.remove_btn.click(nth=index)