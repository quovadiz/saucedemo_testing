import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        loc = self.locator.format(**kwargs)
        with allure.step(f'Getting locator "{loc}" at index "{nth}"'):
            if any(char in loc for char in ["[", ".", ">", "*", "^", "#", " "]):
                locator_obj = self.page.locator(loc)
            else:
                locator_obj = self.page.locator(f"[data-test='{loc}']")

            return locator_obj.nth(nth)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_hidden(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is hidden'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_hidden()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)
