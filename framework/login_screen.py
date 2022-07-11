import time
from framework.BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_SIGNIN_BUTTON = (By.CLASS_NAME, "header_user_info")
    LOCATOR_EMAIL_FIELD = (By.ID, "email")
    LOCATOR_PASSWORD_FIELD = (By.ID, "passwd")
    LOCATOR_SUBMIT_LOGIN = (By.ID, "SubmitLogin")


class LoginHelper(BasePage):

    def sign_in_button(self):
        search_signin_button = self.find_element(Locators.LOCATOR_SIGNIN_BUTTON)
        search_signin_button.click()
        return search_signin_button


    def enter_email(self):
        search_email_field = self.find_element(Locators.LOCATOR_EMAIL_FIELD)
        search_email_field.send_keys("evgeniya.ro.spam@gmail.com")
        time.sleep(1.0)
        return search_email_field


    def enter_password(self):
        search_password_field = self.find_element(Locators.LOCATOR_PASSWORD_FIELD)
        search_password_field.send_keys("Mp2524483")
        time.sleep(1.0)
        return search_password_field

    def submit_login(self):
        search_login_button = self.find_element(Locators.LOCATOR_SUBMIT_LOGIN)
        search_login_button.click()
        return search_login_button




