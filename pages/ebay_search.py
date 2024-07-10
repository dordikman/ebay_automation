from playwright.sync_api import Page

class EbaySearch:
    def __init__(self,page:Page,searched_item:str)->None:
        self.page = page
        self.searched_item=searched_item

    def searched_item_result_visiable(self,role:str,keyword:str)->bool:
        return self.page.locator(f'[role="{role}"][name*="{keyword}"]').is_visible()

    def click_searched_item_result(self,role:str,keyword:str)->None:
        self.page.locator(f'[role="{role}"][name*="{keyword}]').click()












