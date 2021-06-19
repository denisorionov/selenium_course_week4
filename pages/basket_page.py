from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.browser.find_element(
            *BasketPageLocators.BASKET_CONTENT).text == "Ваша корзина пуста Продолжить покупки"
