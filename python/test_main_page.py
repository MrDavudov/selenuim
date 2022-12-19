import math
import time
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

answer = math.log(int(time.time()))
answer2 = math.log(abs((12 * math.sin(float(750)))))
print(answer2)