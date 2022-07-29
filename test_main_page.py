from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

# MainPage link
link = "http://selenium1py.pythonanywhere.com/"

# Product Page
linkProduct = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        pageLogin = LoginPage(browser, link)
        pageLogin.should_be_login_url()
        pageLogin.should_be_login_form()
        pageLogin.should_be_register_form()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basketPage = BasketPage(browser, link)
    basketPage.should_not_be_items_in_basket()
    basketPage.should_be_empty_basket_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, linkProduct)
    page.open()
    page.go_to_basket_page()
    basketPage = BasketPage(browser, linkProduct)
    basketPage.should_not_be_items_in_basket()
    basketPage.should_be_empty_basket_message()
