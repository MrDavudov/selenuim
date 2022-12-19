from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_Url = "http://selenium1py.pythonanywhere.com/"
    LOGIN_Username = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_Password = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_Btn = (By.CSS_SELECTOR, '.btn[value="Log In"]')
    
    REG_Email = (By.CSS_SELECTOR, "#id_registration-email")
    REG_Password = (By.CSS_SELECTOR, "#id_registration-password")
    REG_Password2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_Btn = (By.CSS_SELECTOR, '.btn[value="Register"]')