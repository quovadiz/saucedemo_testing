import pytest
from playwright.sync_api import Playwright, Page
from config import settings
from pages.authentication.login_page import LoginPage
from tools.pages import initialize_playwright_page


@pytest.fixture(scope="session", autouse=True)
def set_playwright_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page: # type: ignore
    yield from initialize_playwright_page(playwright) # type: ignore


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    login_page = LoginPage(page=page)
    login_page.visit(settings.base_url)
    login_page.login_form.fill(
        username=settings.standard_user,
        password=settings.password
    )
    login_page.click_login_button()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture
def chromium_page_with_state(
        initialize_browser_state, playwright: Playwright
) -> Page: # type: ignore
    yield from initialize_playwright_page(playwright,storage_state=settings.browser_state_file)

