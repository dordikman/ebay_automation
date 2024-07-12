from playwright.sync_api import Page
from typing import List

class EbayResultsPage:
    def __init__(self,page:Page)->None:
        self.page = page
        self.links=page.locator('.s-item__title')


    def search_results_title(self)->List[str]:
        "this method returns requested search results"
        self.links.nth(9).wait_for()
        return self.links.all_text_contents()


    def results_contain_search_phrase(self,search_phrase:str,num_of_titles:int=10)->bool:
        "num_of_titles is set to min number 10 as requested"
        titles=self.search_results_title()
        matches_count=[title for title in titles if search_phrase.lower() in title.lower()]
        return len(matches_count) >= num_of_titles


















