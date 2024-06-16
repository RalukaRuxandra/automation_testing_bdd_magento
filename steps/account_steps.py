from behave import *


@when('I click on the customer menu arrow')
def step_impl(context):
    context.account_page.click_customer_menu_arrow()


@when('I click on my account')
def step_impl(context):
    context.account_page.click_my_account()


@when('I click on edit address under default shipping address')
def step_impl(context):
    context.account_page.click_change_shipping_address()


@when('I put in the required info')
def step_impl(context):
    context.account_page.insert_billing_or_shipping_info()


@when('I click the save address button')
def step_impl(context):
    context.account_page.click_save_address()


@then('The address page loads')
def step_impl(context):
    context.account_page.check_address_url()


@when('I hover the mouse over Women, Tops, Jackets and I click Jackets')
def step_impl(context):
    context.account_page.select_product()


@when('I click the first item')
def step_impl(context):
    context.account_page.click_first_item()


@then('the item page opens')
def step_impl(context):
    context.account_page.check_item_url()


@when('I click the Add to cart button')
def step_impl(context):
    context.account_page.click_add_to_cart()


@then('The error messages "{err_msgs}" are displayed')
def step_impl(context, err_msgs):
    context.account_page.are_error_messages_displayed(err_msgs)


@when('I choose the size "{size}"')
def step_impl(context, size):
    context.account_page.click_size(size)


@when('I click a different colour') #de parametrizat culoarea
def step_impl(context):
    context.account_page.change_colour()


@then('The confirmation message "{confirmation_msg}" is displayed')
def step_impl(context, confirmation_msg):
    context.account_page.is_confirmation_message_displayed(confirmation_msg)


@when('I click the shopping cart')
def step_impl(context):
    context.account_page.click_cart()


@when('I click the Proceed to checkout button')
def step_impl(context):
    context.account_page.click_proceed_to_checkout()


@then('the shipping page loads')
def step_impl(context):
    assert context.account_page.check_shipping_page()


@when('I click the Next button')
def step_impl(context):
    context.account_page.click_next()


@then('The payment page loads')
def step_impl(context):
    context.account_page.check_payment_url()


@when('I confirm the billing address')
def step_impl(context):
    context.account_page.click_same_address()


@when('I click Place order button')
def step_impl(context):
    context.account_page.click_place_order()


@then('the success purchase page loads')
def step_impl(context):
    context.account_page.check_success_url()


@then('The sign in window opens')
def step_impl(context):
    context.account_page.check_sign_in_url()