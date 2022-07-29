from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     #    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     #    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     print(link)
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     productName = pageProduct.get_product_name()
#     productPrice = pageProduct.get_product_price()
#
#     pageProduct.add_to_basket()
#     pageProduct.solve_quiz_and_get_code()
#     pageProduct.should_be_add_to_basket_message(productName)
#     pageProduct.should_be_price(productPrice)
#
#
# @pytest.mark.xfail(reason="expected failure by the task")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     pageProduct.add_to_basket()
#     # no success message is_not_element_present
#     pageProduct.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     # no success message is_not_element_present
#     pageProduct.should_not_be_success_message()
#
#
# @pytest.mark.xfail(reason="expected failure by the task")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     pageProduct.add_to_basket()
#     # no success message is_disappeared
#     pageProduct.should_dissappear_success_message()
#
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     pageLogin = LoginPage(browser, link)
#     pageLogin.should_be_login_url()
#     pageLogin.should_be_login_form()
#     pageLogin.should_be_register_form()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        email = str(time.time())+"@fakemail.org"
        password = str(time.time())+str(time.timezone)
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pageProduct = ProductPage(browser, link)
        pageProduct.open()
        pageProduct.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        pageProduct = ProductPage(browser, link)
        pageProduct.open()
        productName = pageProduct.get_product_name()
        productPrice = pageProduct.get_product_price()

        pageProduct.add_to_basket()
        pageProduct.should_be_add_to_basket_message(productName)
        pageProduct.should_be_price(productPrice)
