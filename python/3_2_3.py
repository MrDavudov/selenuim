from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
        input1.send_keys("Ivan")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
        input5.send_keys("Victor")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
        input2.send_keys("test@mail.ru")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.first')
        input3.send_keys("8928")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.second')
        input4.send_keys("Russia")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()
    
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
        input1.send_keys("Ivan")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
        input5.send_keys("Victor")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
        input2.send_keys("test@mail.ru")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.first')
        input3.send_keys("8928")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.second')
        input4.send_keys("Russia")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

if __name__ == "__main__":
    unittest.main()