from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import time

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE)
        assert not self.is_element_present(*BasePageLocators.BASKET_ITEMS), "Items list should not be on the empty basket screen"
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), "No empty basket message"
    
    def def test_guest_cant_see_success_message_after_adding_product_to_basket():
        add_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_product.click()
        added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET)
        p = added_message.text
        
