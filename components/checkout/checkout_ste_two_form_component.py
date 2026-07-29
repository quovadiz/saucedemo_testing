import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class CheckoutStepTwoFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.quantity = Text(page, "[data-test='item-quantity']", "Checkout Item Quantity")
        self.title = Text(page, "[data-test='inventory-item-name']", "Checkout Item Title")
        self.description = Text(page, "[data-test='inventory-item-desc']", "Checkout Item Description")
        self.price = Text(page, "[data-test='inventory-item-price']", "Checkout Item Price")

    @allure.step('Check visible checkout item at index "{index}"')
    def check_visible(self, index: int, quantity: str, title: str, price: str, description: str):
        self.quantity.check_visible(nth=index)
        self.quantity.check_have_text(quantity, nth=index)

        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        self.price.check_visible(nth=index)
        self.price.check_have_text(price, nth=index)

        self.description.check_visible(nth=index)
        self.description.check_have_text(description, nth=index)