from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_notion_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.NOTION_ABOUT_EMPTY_BASKET), \
            "Notion about empty basket is not present"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_LIST_IN_BASKET), \
            "There should not be any products in basket"
