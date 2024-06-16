from behave import *


@given("I am on the main page")
def step_impl(context):
    context.sign_in_page.main_page()


@when("I click on sign in button")
def step_impl(context):
    context.sign_in_page.sign_in_button()




@when('I insert "{email}" in the email input')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@when('I insert "{password}" in the password input')
def step_impl(context, password):
    context.sign_in_page.set_password(password)


@when("I click on the Login button")
def step_impl(context):
    context.sign_in_page.click_login_button()


@when('i insert username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.sign_in_page.set_email(username)
    context.sign_in_page.set_password(password)


@then('i cannot login into the application and i receive "{error_message}" error')
def step_impl(context, error_message):
    context.sign_in_page.verify_email_error(error_message)


@then('The account error message "{account_err}" is displayed')
def step_impl(context, account_err):
    context.sign_in_page.verify_account_error(account_err)


@then('The password error message "{password_err}" is displayed')
def step_impl(context, password_err):
    context.sign_in_page.verify_password_error(password_err)


@then('The welcome message is displayed')
def step_impl(context):
    context.sign_in_page.welcome()


@then('The account page loads')
def step_impl(context):
    context.sign_in_page.account_url()
