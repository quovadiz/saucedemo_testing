import pytest

from pages.cart.cart_page import CartPage
from pages.catalog.inventory_page import InventoryPage
from pages.checkout.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout.checkout_complete_page import CheckoutCompletePage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.checkout
class TestCheckout:
    def test_successful_order_placement(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_step_one_page: CheckoutStepOnePage,
        checkout_step_two_page: CheckoutStepTwoPage,
        checkout_complete_page: CheckoutCompletePage,
    ):
        inventory_page.visit(AppRoute.INVENTORY_URL)
        inventory_page.check_current_url(AppRoute.INVENTORY_URL)

        title = inventory_page.product_card.title.get_locator(0).inner_text()
        price = inventory_page.product_card.price.get_locator(0).inner_text()
        description = inventory_page.product_card.description.get_locator(0).inner_text()

        inventory_page.add_product_to_cart(index=0)

        inventory_page.cart_button.click()
        cart_page.check_current_url(AppRoute.CART_URL)
        cart_page.checkout_btn.click()
        cart_page.check_current_url(AppRoute.CHECKOUT_STEP_ONE_URL)

        checkout_step_one_page.fill_form_and_continue(
            first_name="Denis", last_name="Automation", postal_code="12345"
        )
        checkout_step_one_page.check_current_url(AppRoute.CHECKOUT_STEP_TWO_URL)

        checkout_step_two_page.check_product_in_overview(
            index=0, quantity="1", title=title, price=price, description=description
        )

        checkout_step_two_page.click_finish()

        checkout_complete_page.check_current_url(AppRoute.CHECKOUT_COMPLETE_URL)
        checkout_complete_page.check_checkout_complete_success()