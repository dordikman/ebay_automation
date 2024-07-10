import pytest
from playwright.sync_api import Playwright, sync_playwright


def setup_playwright(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    return browser,context,page

def run_tests()->None:
    browser,context,page=setup_playwright(playwright)
    try:
        page.goto("https://www.ebay.com/")
    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run_tests()




