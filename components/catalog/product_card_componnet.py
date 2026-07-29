import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text


class ProductCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "[data-test='inventory-item-name']", "Title")
        self.price = Text(page, "[data-test='inventory-item-price']", "Price")
        self.description = Text(page, "[data-test='inventory-item-desc']", "Description")
        self.image = Image(page, "[data-test*='-img']", "Preview")

        self.add_to_cart_btn = Button(page, "[data-test^='add-to-cart']", "Add to cart button")
        self.remove_btn = Button(
            page,
            "[data-test^='remove']",
            "Remove button"
        )

    @allure.step('Check visible product card at index "{index}"')
    def check_visible(self, index: int, title: str, price: str, description: str):
        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        self.image.check_visible(nth=index)

        self.price.check_visible(nth=index)
        self.price.check_have_text(price, nth=index)

        self.description.check_visible(nth=index)
        self.description.check_have_text(description, nth=index)

        self.add_to_cart_btn.check_visible(nth=index)

    @allure.step("Add product to cart at index '{index}'")
    def add_to_cart(self, index: int = 0):
        self.add_to_cart_btn.check_visible(nth=index)
        self.add_to_cart_btn.click(nth=index)

    @allure.step("Remove product from cart at index '{index}'")
    def remove_from_cart(self, index: int = 0):
        self.remove_btn.check_visible(nth=index)
        self.remove_btn.click(nth=index)