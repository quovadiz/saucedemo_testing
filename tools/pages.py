from playwright.sync_api import Playwright, Page

from config import settings


def initialize_playwright_page(
        playwright: Playwright,
        storage_state: str | None = None
) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.base_url,
        storage_state=storage_state,
    )
    page = context.new_page()

    yield page # type: ignore

    browser.close()

