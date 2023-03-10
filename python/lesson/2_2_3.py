from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, 'num1')
    num1 = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    num2 = num2.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(int(num1)+int(num2)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

