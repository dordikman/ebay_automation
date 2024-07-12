import pytest
from pages.search import EbaySearchPage
from pages.search_results import EbayResultsPage
from playwright.sync_api import Page

"this file uses pytest fixture to pass a page object and inject it to the test files"
@pytest.fixture
def ebay_results_page(page:Page)-> EbayResultsPage:
    return EbayResultsPage(page)

@pytest.fixture
def ebay_search_page(page:Page)-> EbaySearchPage:
    return EbaySearchPage(page)







