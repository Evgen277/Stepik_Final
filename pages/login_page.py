from .base_page import BasePage
from .locators import BasePageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        register_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        register_link.click()
        email_send = self.browser.find_element(*BasePageLocators.REGISTER_EMAIL)
        email_send.send_keys(email)
        password_enter = self.browser.find_element(*BasePageLocators.REGISTER_PASSWORD)
        password_enter.send_keys(password)
        password_confirm = self.browser.find_element(*BasePageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm.send_keys(password)
        register_button = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
        register_button.click()
        
        
