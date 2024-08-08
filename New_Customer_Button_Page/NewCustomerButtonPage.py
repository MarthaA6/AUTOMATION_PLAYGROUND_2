import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from New_Customer_Button_Locator.NewCustomerButtonLocator import NewCustomerButtonLocator


class NewCustomerButtonPage:
    def __init__(self, driver):
        self.driver = driver

    def new_customer_button(self):
        new_customer_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerButtonLocator.NEW_CUSTOMER_BUTTON))
        new_customer_button.click()
        time.sleep(5)