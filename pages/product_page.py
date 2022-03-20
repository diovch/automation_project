from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        if self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON):
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_name_should_be_same(self):
        product_name = self.get_product_name()
        added_product_name = self.get_added_product_name()
        assert product_name == added_product_name, \
            "Product names in product page and in basket are not the same"

    def get_added_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME).text

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_LOCATOR).text

    def product_price_should_be_same(self):
        product_price = self.get_product_price()
        added_product_price = self.get_added_product_price()
        assert product_price == added_product_price, \
            "Product prices in product page and in basket are not the same"

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_LOCATOR).text

    def get_added_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
