from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import MainPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is empty message s not presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "Basket items are presented, but should not be"
