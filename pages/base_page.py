from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until="networkidle")

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")


    def check_current_url(self, expected_url):
        url_pattern = getattr(expected_url, "pattern", expected_url)

        with allure.step(f'Checking that current url matches "{url_pattern}"'):
            expect(self.page).to_have_url(expected_url)
