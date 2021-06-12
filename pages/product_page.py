from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert book_name == book_name_in_basket

    def should_be_book_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_book == price_in_basket
