from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators
import math
import time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert self.browser.current_url.startswith("http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"), "Invalid login link"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET)
        link.click()
        time.sleep(5)
        a = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE)
        assert not self.is_element_present(*BasePageLocators.BASKET_ITEMS), "Items list should not be on the empty basket screen"
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), "No empty basket message"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        time.sleep(2)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



