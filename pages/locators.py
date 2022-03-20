from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form [type='submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_PRICE_LOCATOR = (By.XPATH, "//div[contains(@class,'product_main')]//p[contains(text(), '£')]")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class,'product_main')]//h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")
    ADDED_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']//p//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")


class BasketPageLocators:
    NOTION_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p ")
    PRODUCT_LIST_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")