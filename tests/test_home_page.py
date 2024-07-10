from idlelib import browser

import pytest

from pages.home_page import HomePage


class TestHomePage():

    def test_navigate_to_url(self,home_page:HomePage):
        home_page.navigate_to_url()
        assert home_page.page.url=="https://www.ebay.com/"

    def test_click_search_bar(self,home_page:HomePage):
        search_bar=home_page.click_search_bar()
        assert search_bar.is_visible(),"search bar is not visible"

    def test_fill_search_bar(self,home_page:HomePage):
        assert home_page.fill_search_bar()==True,"laptop"

    def test_click_search_button(self,home_page:HomePage):
        if self.test_fill_search_bar(home_page):
           home_page.click_search_button()
           assert home_page.page.url=="/laptop"
























