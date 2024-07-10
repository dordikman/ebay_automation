from playwright.sync_api import Page


class HomePage:
    def __init(self,page:Page)->None:
        self.page = page

    def navigate_to_url(self):
        self.page.goto("https://www.ebay.com/")


    def click_ebay_logo(self)->None:
        self.page.get_by_role("link", name="eBay Home").click()


    def click_shop_by_category(self)->None:
        self.page.get_by_role("button", name="Shop by category").click()


    def click_search_bar(self)->None:
        self.page.get_by_placeholder("Search for anything").click()


    def fill_search_bar(self)->None:
        self.page.get_by_placeholder("Search for anything").fill("laptop")


    def click_choose_category(self)->None:
        self.click_all_categories.click()


    def click_all_categories(self)->None:
        self.page.get_by_label("Select a category for search")


    def click_search_button(self)->None:
        self.page.get_by_role("button", name="Search").click()





















