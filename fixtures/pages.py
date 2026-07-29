import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from pages.checkout.checkout_complete_page import CheckoutCompletePage
from pages.checkout.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout.checkout_step_two_page import CheckoutStepTwoPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def inventory_page(chromium_page_with_state: Page) -> InventoryPage:
    return InventoryPage(page=chromium_page_with_state)

@pytest.fixture
def cart_page(chromium_page_with_state: Page) -> CartPage:
    return CartPage(page=chromium_page_with_state)

@pytest.fixture
def checkout_step_one_page(chromium_page_with_state: Page) -> CheckoutStepOnePage:
    return CheckoutStepOnePage(page=chromium_page_with_state)

@pytest.fixture
def checkout_step_two_page(chromium_page_with_state: Page) -> CheckoutStepTwoPage:
    return CheckoutStepTwoPage(page=chromium_page_with_state)

@pytest.fixture
def checkout_complete_page(chromium_page_with_state: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page=chromium_page_with_state)

