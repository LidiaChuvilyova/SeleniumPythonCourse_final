from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    pageProduct = ProductPage(browser, link)
    pageProduct.open()
    productName = pageProduct.get_product_name()
    productPrice = pageProduct.get_product_price()

    pageProduct.add_to_basket()
    pageProduct.solve_quiz_and_get_code()
    pageProduct.should_be_add_to_basket_message(productName)
    pageProduct.should_be_price(productPrice)


