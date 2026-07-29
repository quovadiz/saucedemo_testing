import allure
import pytest

from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from tools.routes import AppRoute


@allure.epic("Shopping Cart")
@allure.feature("Cart Management")
@pytest.mark.regression
@pytest.mark.cart
class TestCart:
    @allure.story("Cart Navigation")
    @allure.title("Navigate from inventory to shopping cart page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

    @allure.story("Cart Content")
    @allure.title("Verify product composition and details in the shopping cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_composition(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        title = inventory_page.product_card.title.get_locator(0).inner_text()
        price = inventory_page.product_card.price.get_locator(0).inner_text()
        description = inventory_page.product_card.description.get_locator(0).inner_text()

        inventory_page.add_product_to_cart(index=0)
        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

        cart_page.cart_item.check_visible(
            index=0,
            quantity="1",
            title=title,
            price=price,
            description=description,
        )

    @allure.story("Cart Management")
    @allure.title("Remove product from the shopping cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_from_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.add_product_to_cart(index=0)
        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

        cart_page.remove_product(index=0)

        cart_page.check_cart_item_is_absent(index=0)

    @allure.story("Cart Navigation")
    @allure.title("Return to catalog from cart using continue shopping button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_return_to_catalog(self, cart_page: CartPage):
        cart_page.visit(AppRoute.CART_URL)
        cart_page.check_current_url(AppRoute.CART_URL)

        cart_page.continue_shopping_btn.click()
        cart_page.check_current_url(AppRoute.INVENTORY_URL)