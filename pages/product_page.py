from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

import time

class ProductPage(BasePage):
        
    def should_add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        add_product.click()
        


    def should_be_equal_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        a = product_price.text
        product_price_at_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AT_BASKET)
        b = product_price_at_basket.text
        c = b[b.find(":") + 1:b.find(".")+4]
        assert a in c, " The Price is not equal"

    def should_be_product_added_message(self):   
        added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET)
        p = added_message.text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), " No product added message or message is wrong"

    def should_be_equal_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_at_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AT_BASKET)
        assert product_name.text == product_name_at_basket.text, "Wrong product name"
       
    def should_be_basket_price_message(self):
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        f = basket_price_message.text
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Wrong basket price message"
        
    def should_not_be_success_message(self):
        added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET)
        p = added_message.text
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), \
       "Success message is presented, but should not be"

        
