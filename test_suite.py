import pytest
from selenium import webdriver

from Login_Page.LoginPage import LoginPage
from Customer_Form_Page.NewCustomerPage import NewCustomerPageForm
from New_Customer_Button_Page.NewCustomerButtonPage import NewCustomerButtonPage
from Sign_Out_Page.SignOutPage import SignOutPage
from config.config import Config, ConfigNewCustomerForm


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(Config.BaseUrl)
    return login_page


def test_login_page_automation_playground(login):
    login.email(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.submit()


def test_new_customer_button_on_automation_playground(login):
    new_customer_button = NewCustomerButtonPage(login.driver)
    new_customer_button.new_customer_button()


def test_new_customer_form_page_on_automation_playground(login):
    new_customer_form = NewCustomerPageForm(login.driver)
    new_customer_form.enter_email_address(ConfigNewCustomerForm.EMAIL_ADDRESS)
    new_customer_form.enter_first_name(ConfigNewCustomerForm.FIRST_NAME)
    new_customer_form.enter_last_name(ConfigNewCustomerForm.LAST_NAME)
    new_customer_form.enter_city(ConfigNewCustomerForm.CITY)
    new_customer_form.enter_state(ConfigNewCustomerForm.STATE)
    new_customer_form.click_gender_check_box()
    new_customer_form.click_submit_button()


def test_sign_out_on_automation_playground(login):
    sign_out = SignOutPage(login.driver)
    sign_out.sign_out()
