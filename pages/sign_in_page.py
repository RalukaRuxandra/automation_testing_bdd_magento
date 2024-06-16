import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SignInPage(BasePage):

    SIGN_IN = (By.XPATH, '//a[contains(text(), "Sign In ")]')
    CONSENT = (By.XPATH, '//p[contains(text(), "Consent")]')
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, '//button[@class="action login primary"]')
    INVALID_EMAIL = (By.XPATH, '//div[@id="email-error"]')
    INVALID_PASSWORD = (By.XPATH, '//div[@id="pass-error"]')
    INVALID_ACCOUNT = (By.XPATH, '//div[@class="message-error error message"]/div')
    ACCOUNT_URL = 'https://magento.softwaretestingboard.com/'
    WELCOME_MSG = (By.XPATH, '(//span[@class = "logged-in"])[1]')

    def main_page(self):
        self.get_page(self.URL)

    def signin_page(self):
        self.get_page(self.SIGN_IN_URL)

    def sign_in_button(self):
        self.click_elem(self.SIGN_IN)

    def sign_in_url(self):
        assert self.actual_url() == self.SIGN_IN_URL

    def set_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EMAIL))
        if email == "space":
            email = chr(32)
        else:
            self.send_text(self.EMAIL, email)

    def set_password(self, password):
        self.send_text(self.PASSWORD, password)

    def click_login_button(self):
        self.click_elem(self.LOGIN_BUTTON)
        time.sleep(2)

    def invalid_email(self):
        assert self.is_displayed(self.INVALID_EMAIL)

    def verify_email_error(self, error_message):
        assert error_message in self.get_text(self.INVALID_EMAIL)

    def verify_password_error(self, password_err):
        assert self.is_displayed(self.INVALID_PASSWORD), password_err in self.get_text(self.INVALID_PASSWORD)

    def verify_account_error(self, account_err):
        assert self.is_displayed(self.INVALID_ACCOUNT), account_err in self.get_text(self.INVALID_ACCOUNT)

    def account_url(self):
        return self.actual_url() == self.ACCOUNT_URL

    def welcome(self):
        assert self.is_displayed(self.WELCOME_MSG)
