from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)


    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла