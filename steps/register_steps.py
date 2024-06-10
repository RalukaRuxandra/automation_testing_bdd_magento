from behave import *


@when('I click on the create an account link')
def step_impl(context):
    context.register_page.click_create_account_link()


# @then('The create account page loads')
# def step_impl(context):
#     assert context.register_page.check_create_account_url()


@when('I insert the first name') #de parametrizat
def step_impl(context):
    context.register_page.set_first_name()


@when('I insert the last name') #de parametrizat
def step_impl(context):
    context.register_page.set_last_name()


@when('I insert the new email') #de parametrizat
def step_impl(context):
    context.register_page.set_new_email()


@when('I insert "{new_password}" in the password box')
def step_impl(context, new_password):
    context.register_page.set_new_password(new_password)


@when('I click on the create an account button')
def step_impl(context):
    context.register_page.click_create_account_button()


@then('The new user is logged in')
def step_impl(context):
    assert context.register_page.check_account_url()


@when('I click on the dropdown arrow')
def step_impl(context):
    context.register_page.click_dropdown_arrow()


@when('I click on the sign out link')
def step_impl(context):
    context.register_page.click_sign_out()


@then('The logout page loads')
def step_impl(context):
    assert context.register_page.check_logout_url() # de transformat in metoda generala
