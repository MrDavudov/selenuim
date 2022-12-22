from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    TITLE_OF_THE_ITEM = (By.CSS_SELECTOR, 'h1')
    PRICE_ITEM = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')

class LoginPageLocators():
    LOGIN_Url = "http://selenium1py.pythonanywhere.com/"
    LOGIN_Username = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_Password = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_Btn = (By.CSS_SELECTOR, '.btn[value="Log In"]')
    
    REG_Email = (By.CSS_SELECTOR, "#id_registration-email")
    REG_Password = (By.CSS_SELECTOR, "#id_registration-password")
    REG_Password2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_Btn = (By.CSS_SELECTOR, '.btn[value="Register"]')

class CartPageLocators(object):
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, '#content_inner')
    
