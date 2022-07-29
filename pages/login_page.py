from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        emailTextBox = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        emailTextBox.send_keys(email)
        passwordTextBox = self.browser.find_element(*LoginPageLocators.PASSWORD)
        passwordTextBox.send_keys(password)
        confirmPasswordTextBox = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirmPasswordTextBox.send_keys(password)
        registerButton = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registerButton.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


