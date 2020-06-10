from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import ProductPageLocators
import time

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE)
        assert not self.is_element_present(*BasePageLocators.BASKET_ITEMS), "Items list should not be on the empty basket screen"
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), "No empty basket message"
    
