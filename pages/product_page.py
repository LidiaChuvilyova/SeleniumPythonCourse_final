from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

    def get_product_name(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return text.text

    def get_product_price(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return text.text

    def should_be_add_to_basket_message(self, expectedProductName):
        # get alert inner messages (supposedly 2 items)
        alertInnerMessages = self.get_all_elements(*ProductPageLocators.ALERT_INNER_STRONG)
        # check that in alert message text contains expected product name
        found = self.is_element_presented_in_list_by_text(alertInnerMessages, expectedProductName)
        assert found, f"There is no message that Product {expectedProductName} is added to the basket"

    def should_be_price(self, expectedProductPrice):
        price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_TOTAL)
        assert expectedProductPrice == price.text, f"Basket total should be {expectedProductPrice}/nCurrent value: {price.text}"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
