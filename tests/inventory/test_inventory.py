import pytest

from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.inventory
class TestInventory:
    def test_add_product_to_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.product_card.add_to_cart(index=0)
        inventory_page.check_cart_badge_count("1")

    def test_add_multiple_products_to_cart(self, inventory_page: InventoryPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.add_product_to_cart(index=0)
        inventory_page.add_product_to_cart(index=1)
        inventory_page.add_product_to_cart(index=2)

        inventory_page.check_cart_badge_count("3")

    def test_remove_product_from_cart(self, inventory_page: InventoryPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        inventory_page.add_product_to_cart(index=0)
        inventory_page.check_cart_badge_count("1")

        inventory_page.remove_product_from_cart(index=0)
        inventory_page.check_cart_badge_is_absent()

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
