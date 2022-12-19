from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url(*LoginPageLocators.LOGIN_Url), "Url false"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        input1 = self.browser.find_element(*LoginPageLocators.LOGIN_Username)
        input1.send_keys("")
        input2 = self.browser.find_element(*LoginPageLocators.LOGIN_Password)
        input2.send_keys("")

        btn = self.browser.find_element(*LoginPageLocators.LOGIN_Btn)
        btn.click()
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        input1 = self.browser.find_element(*LoginPageLocators.REG_Email)
        input1.send_keys("")
        input2 = self.browser.find_element(*LoginPageLocators.REG_Password)
        input2.send_keys("")
        input3 = self.browser.find_element(*LoginPageLocators.REG_Password2)
        input3.send_keys("")

        btn = self.browser.find_element(*LoginPageLocators.REG_Btn)
        btn.click()
        assert True