import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Customer_Form_Locator.NewCustomerLocator import NewCustomerLocator


class NewCustomerPageForm:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.EMAIL_ADDRESS))
        enter_email.send_keys(email)
        time.sleep(5)

    def enter_first_name(self, first):
        enter_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.FIRST_NAME))
        enter_first_name.send_keys(first)
        time.sleep(5)

    def enter_last_name(self, last):
        enter_last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.LAST_NAME))
        enter_last_name.send_keys(last)
        time.sleep(5)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CITY))
        enter_city.send_keys(city)
        time.sleep(5)

    def enter_state(self, state):
        enter_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.STATE))
        enter_state.send_keys(state)
        time.sleep(5)

    def click_gender_check_box(self):
        click_gender_check_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.GENDER))
        click_gender_check_box.click()
        time.sleep(5)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(5)
