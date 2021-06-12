from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in  strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info strong")
