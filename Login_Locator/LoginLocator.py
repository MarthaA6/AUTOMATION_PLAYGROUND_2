from selenium.webdriver.common.by import By


class LoginLocator:
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#email-id")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-id")

