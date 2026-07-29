import allure
import pytest

from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from tools.routes import AppRoute


@allure.epic("Inventory Catalog")
@allure.feature("Product & Cart Interactions")
@pytest.mark.regression
@pytest.mark.inventory
class TestInventory:
    @allure.story("Add Product to Cart")
    @allure.title("Add a single product to cart from the inventory page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.product_card.add_to_cart(index=0)
        inventory_page.check_cart_badge_count("1")

    @allure.story("Add Multiple Products")
    @allure.title("Add multiple products to cart and verify cart badge count")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_multiple_products_to_cart(self, inventory_page: InventoryPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.add_product_to_cart(index=0)
        inventory_page.add_product_to_cart(index=1)
        inventory_page.add_product_to_cart(index=2)

        inventory_page.check_cart_badge_count("3")

    @allure.story("Remove Product from Catalog")
    @allure.title("Remove a product directly from the inventory catalog view")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_product_from_catalog(self, inventory_page: InventoryPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.add_product_to_cart(index=0)
        inventory_page.check_cart_badge_count("1")

        inventory_page.remove_product_from_cart(index=0)
        inventory_page.check_cart_badge_is_absent()

    @allure.story("Cart Badge Quantity Validation")
    @allure.title("Verify cart badge count dynamically using parameterized quantities")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "items_to_add, expected_count",
        [
            (1, "1"),
            (2, "2"),
            (3, "3"),
        ],
    )
    def test_cart_badge_quantity(
            self, inventory_page: InventoryPage, items_to_add: int, expected_count: str
    ):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        for index in range(items_to_add):
            inventory_page.add_product_to_cart(index=index)

        inventory_page.check_cart_badge_count(expected_count)
