import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Sign_Out_Locator.SignOutLocator import SignOutLocator


class SignOutPage:
    def __init__(self, driver):
        self.driver = driver

    def sign_out(self):
        sign_out = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignOutLocator.SIGN_OUT_BUTTON))
        sign_out.click()
        time.sleep(5)