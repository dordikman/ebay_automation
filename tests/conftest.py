import pytest
from playwright.sync_api import Playwright, sync_playwright
from tests.test_ebay_search import TestEbaySearch
from tests.test_home_page import TestHomePage


def playwright_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        activate_test_home_page()
        activate_test_ebay_search()
        yield browser


def activate_test_home_page(test_home_page:TestHomePage):
    test_home_page.test_fill_search_bar()
    test_home_page.test_navigate_to_url()
    test_home_page.test_click_search_bar()
    test_home_page.test_click_search_button()

def activate_test_ebay_search(test_ebay_search:TestEbaySearch):
    test_ebay_search.test_searched_item_result_visiable()
    test_ebay_search.test_find_10_items()







