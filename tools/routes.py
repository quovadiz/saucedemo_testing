from enum import Enum


class AppRoute(str, Enum):
    BASE_URL = "."
    INVENTORY_URL = "./inventory.html"
    CART_URL = "./cart.html"
    CHECKOUT_STEP_ONE_URL = "./checkout-step-one.html"
    CHECKOUT_STEP_TWO_URL = "./checkout-step-two.html"
    CHECKOUT_COMPLETE_URL = "./checkout-complete.html"