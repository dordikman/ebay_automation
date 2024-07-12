from playwright.sync_api import Page


class EbaySearchPage():

    URL='https://www.ebay.com'
    def __init__(self,page:Page)->None:
        self.page = page
        self.search_bar_input=page.locator('id=gh-ac')
        self.search_button=page.locator('id=gh-btn')


    def navigate(self)->None:
        self.page.goto(self.URL)

    def fill_search_bar(self,search_phrase:str)->None:
        self.search_bar_input.fill(search_phrase)

    def click_search_button(self)->None:
        self.search_button.click()





















