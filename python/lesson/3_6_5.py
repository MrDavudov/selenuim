from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

listURL = [
    '236895/step/1',
    '236896/step/1',
    '236897/step/1',
    '236898/step/1',
    '236899/step/1',
    '236903/step/1',
    '236904/step/1',
    '236905/step/1',
]

textFull = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('correct', listURL)
def test_correct(browser, correct):
    link = f"https://stepik.org/lesson/{correct}"

    browser.get(link)

    # Войти на сайт
    button2 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth.navbar__auth_login"))
    )
    button2.click()

    btn1 = browser.find_element(By.CSS_SELECTOR, ".light-tabs__switch:nth-child(1)")
    btn1.click()
    
    btn2 = browser.find_element(By.CSS_SELECTOR, "input#id_login_email")
    btn2.send_keys("arhangel-smert@mail.ru")

    btn3 = browser.find_element(By.CSS_SELECTOR, "input#id_login_password")
    btn3.send_keys("1234qwer")
    
    btn4 = browser.find_element(By.CSS_SELECTOR, "button.button_with-loader")
    btn4.click()

    # Пройти тест
    input_1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    input_1.send_keys(math.log(int(time.time())))

    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()

    correct = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!")
    )

    textFull += correct.text

print(math.log(int(time.time())))

# Correct! Correct! Correct! The owls are not Correct! Correct! what they seem! OvO

