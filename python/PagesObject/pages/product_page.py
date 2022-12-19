from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import CardPageLocators

pName = "The shellcoder's handbook"

class ProductPage(BasePage): 
    def solve_quiz_and_get_code(self):
        btnAdd = self.browser.find_element(*CardPageLocators.CARD_BtnAdd)
        btnAdd.click()

        pName = self.browser.find_element(*CardPageLocators.CARD_BtnAdd)

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

        btnShowCard = self.browser.find_element(*CardPageLocators.CARD_ShowCard)
        btnShowCard.click()
        assert self.text_to_be_present_in_element(*CardPageLocators.CARD_TitleProduct), "False"


        
        

        
