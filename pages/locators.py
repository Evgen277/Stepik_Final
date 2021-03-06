from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_PRICE_AT_BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, 'div#messages>:nth-child(1)')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_NAME_AT_BASKET = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div#messages>:nth-child(3) > div.alertinner > p:nth-child(1)' )


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, 'span.btn-group>:nth-child(1)')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner>:nth-child(1)')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password2"]' )
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
