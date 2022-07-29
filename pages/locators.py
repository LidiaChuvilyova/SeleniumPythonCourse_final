from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>p.price_color")
    ALERT_INNER_STRONG = (By.XPATH, "//div[contains(@class,'alertinner')]/strong")
    BASKET_PRICE_TOTAL = (By.CSS_SELECTOR, ".alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//a[contains(@class,'btn-default') and contains(text(), 'View basket')]")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[contains(text(), 'basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")