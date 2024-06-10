from driver import Driver
from pages.account_page import AccountPage
from pages.register_page import RegisterPage
from pages.sign_in_page import SignInPage


def before_all(context):
    context.browser = Driver()
    context.sign_in_page = SignInPage()
    context.register_page = RegisterPage()
    context.account_page = AccountPage()


def alter_all(context):
    context.browser.close()
