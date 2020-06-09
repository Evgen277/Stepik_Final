from .pages.product_page import ProductPage
import time
import pytest




def test_guest_can_add_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
     page = ProductPage(browser, link)
     page.open()
     page.should_add_product_to_basket()
     page.solve_quiz_and_get_code()
     page.should_be_equal_price()
     page.should_be_product_added_message()
     page.should_be_equal_name()
     page.should_be_basket_price_message()
     
     time.sleep(10)
     

    
