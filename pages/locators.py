from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_PRICE_LOCATOR = (By.XPATH, "//div[contains(@class,'product_main')]//p[contains(text(), '£')]")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class,'product_main')]//h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")
    ADDED_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']//p//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")