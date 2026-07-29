import allure
from playwright.sync_api import Page

from components.menu.menu_component import MenuComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = MenuComponent(page)

        self.page_title = Text(page, "title", "Checkout Complete Page Title")
        self.pony_express_img = Image(page, "pony-express", "Pony Express image")
        self.complete_header = Text(page, "complete-header", "Success Header")
        self.complete_text = Text(page, "complete-text", "Success Description Text")
        self.back_home_button = Button(page, "back-to-products", "Back Home button")

    @allure.step("Check checkout complete page is opened and content is correct")
    def check_checkout_complete_success(self):
        self.page_title.check_visible()
        self.page_title.check_have_text("Checkout: Complete!")

        self.pony_express_img.check_visible()

        self.complete_header.check_visible()
        self.complete_header.check_have_text("Thank you for your order!")

        self.complete_text.check_visible()
        self.complete_text.check_have_text(
            "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        )

        self.back_home_button.check_visible()

    @allure.step("Click back home button")
    def click_back_home(self):
        self.back_home_button.click()

    @allure.step("Perform logout from complete page")
    def logout(self):
        self.menu.logout()