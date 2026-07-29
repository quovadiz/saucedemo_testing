import pytest
from playwright.sync_api import expect

from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.cart
class TestCart:
    def test_navigate_to_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        # Переходим в корзину через кнопку в шапке каталога
        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

    def test_cart_composition(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        # Считываем данные товара из каталога перед добавлением
        title = inventory_page.product_card.title.get_locator(0).inner_text()
        price = inventory_page.product_card.price.get_locator(0).inner_text()
        description = inventory_page.product_card.description.get_locator(0).inner_text()

        # Добавляем товар в корзину и переходим в нее
        inventory_page.add_product_to_cart(index=0)
        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

        # Проверяем состав и детали товара в корзине через компонент CartItemComponent
        cart_page.cart_item.check_visible(
            index=0,
            quantity="1",
            title=title,
            price=price,
            description=description,
        )

    def test_remove_product_from_cart(self, inventory_page: InventoryPage, cart_page: CartPage):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        # Добавляем товар и переходим в корзину
        inventory_page.add_product_to_cart(index=0)
        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)

        # Удаляем товар прямо из корзины
        cart_page.cart_item.remove_from_cart(index=0)

        # Проверяем, что товар больше не отображается в корзине
        expect(cart_page.cart_item.title.get_locator(0)).not_to_be_visible()

    def test_return_to_catalog(self, cart_page: CartPage):
        # Открываем страницу корзины напрямую
        cart_page.visit(AppRoute.CART_URL)
        cart_page.check_current_url(AppRoute.CART_URL)

        # Возвращаемся к каталогу кнопкой продолжения покупок
        cart_page.continue_shopping_btn.click()
        cart_page.check_current_url(AppRoute.INVENTORY_URL)