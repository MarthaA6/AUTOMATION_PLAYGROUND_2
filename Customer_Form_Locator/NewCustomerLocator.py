from selenium.webdriver.common.by import By


class NewCustomerLocator:
    EMAIL_ADDRESS = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.CSS_SELECTOR, "#City")
    STATE = (By.CSS_SELECTOR, "#StateOrRegion")
    GENDER = (By.CSS_SELECTOR, "#loginform > div > div > div > div > form > div:nth-child(6) > input[type=radio]:nth-child(3)")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#loginform > div > div > div > div > form > button")

