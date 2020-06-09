from .pages.base_page import BasePage
import time


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
     link = "http://selenium1py.pythonanywhere.com/"
     page = BasePage(browser, link)
     page.open()
     page.go_to_basket()
     time.sleep(2)

     




#def test_guest_should_see_login_link(browser):
     #link = "http://selenium1py.pythonanywhere.com/"
     #page = MainPage(browser, link)
     #page.open()
     #page.should_be_login_link()

#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"

    #page = MainPage(browser, link)
    #page.open()
    #page.go_to_login_page()
    #browser.get(link)
     #login_link = browser.find_element_by_css_selector("#login_link")
     #login_link.click()
    
