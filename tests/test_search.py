from pages.search import EbaySearchPage
from pages.search_results import  EbayResultsPage
from playwright.sync_api import Page,expect

def test_search(
    page:Page,
    ebay_results_page: EbayResultsPage,
    ebay_search_page:EbaySearchPage)->None:

    ebay_search_page.navigate()

    "#making sure home page loads"
    assert page.url == 'https://www.ebay.com/'

    ebay_search_page.fill_search_bar('laptop')

    "check if input is currect"
    expect(ebay_search_page.search_bar_input).to_have_value('laptop')

    ebay_search_page.click_search_button()

    "making sure results page loads"
    assert 'laptop' in page.url

    assert ebay_results_page.results_contain_search_phrase('laptop')
























