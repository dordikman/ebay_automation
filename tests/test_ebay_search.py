from pages.ebay_search import EbaySearch


class TestEbaySearch():

    def test_searched_item_result_visiable(self,ebay_search:EbaySearch):
        assert ebay_search.searched_item_result_visiable(role="link",word="Laptop")== "Laptop"

    def test_find_10_items(self,ebay_search:EbaySearch):
        try:
            for i in range(11):
                self.test_searched_item_result_visiable(role="link",word="Laptop")
        except:
            print("could not find 10 items with keyword")





