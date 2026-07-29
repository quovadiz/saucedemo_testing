import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def inventory_page(chromium_page_with_state: Page) -> InventoryPage:
    return InventoryPage(page=chromium_page_with_state)

@pytest.fixture
def cart_page(chromium_page_with_state: Page) -> CartPage:
    return CartPage(page=chromium_page_with_state)


