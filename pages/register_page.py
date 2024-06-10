import random
import time
from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    CREATE_ACCOUNT_URL = 'https://magento.softwaretestingboard.com/customer/account/create/'
    CREATE_ACCOUNT_LINK = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/customer/account/create/"]')
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    NEW_EMAIL = (By.ID, 'email_address')
    NEW_PASSWORD = (By.ID, 'password')
    CONFIRM_NEW_PASSWORD = (By.ID, 'password-confirmation')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@title="Create an Account"]')
    ACCOUNT_URL = 'https://magento.softwaretestingboard.com/customer/account/'
    DROPDOWN_ARROW = (By.XPATH, '//button[@class="action switch"]')
    SIGN_OUT_LINK = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/customer/account/logout/"]')
    SIGN_OUT_URL = 'https://magento.softwaretestingboard.com/customer/account/logoutSuccess/'
    faker = Faker()

    #TOATE METODELE DE INPUT TRB MODFICATE PENTRU A PUTEA PRIMI UN ARGUMENT

    def click_create_account_link(self):
        self.click(self.CREATE_ACCOUNT_LINK)

    def check_create_account_url(self):
        return self.actual_url() == self.CREATE_ACCOUNT_URL

    def set_first_name(self):
        self.send_text(self.FIRST_NAME, 'Miao')

    def set_last_name(self):
        self.send_text(self.LAST_NAME, 'Hhhhhhh')

    def set_new_email(self):
        email = self.faker.email()
        self.send_text(self.NEW_EMAIL, email)

    def set_new_password(self, new_password):
        self.send_text(self.NEW_PASSWORD, new_password)
        self.send_text(self.CONFIRM_NEW_PASSWORD, new_password)

    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def check_account_url(self):
        return self.actual_url() == self.ACCOUNT_URL

    def click_dropdown_arrow(self):
        self.click(self.DROPDOWN_ARROW)

    def click_sign_out(self):
        self.click(self.SIGN_OUT_LINK)

    def check_logout_url(self):
        return self.actual_url() == self.SIGN_OUT_URL
