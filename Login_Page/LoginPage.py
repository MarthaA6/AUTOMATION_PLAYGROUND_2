import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Login_Locator.LoginLocator import LoginLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def email(self, martha):
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_ADDRESS))
        email.send_keys(martha)
        time.sleep(5)

    def password(self, pass_code):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        password.send_keys(pass_code)
        time.sleep(5)

    def submit(self):
        submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.SUBMIT_BUTTON))
        submit.click()
        time.sleep(5)
