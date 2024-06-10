from behave import *


@when('I hover the mouse over Women, Tops, Jackets and I click Jackets')
def step_impl(context):
    context.account_page.select_product()


@when('I click the first item')
def step_impl(context):
    context.account_page.click_first_item()


@then('the item page opens')
def step_impl(context):
    assert context.account_page.check_item_url()


@then('the item name is displayed')
def step_impl(context):
    assert context.account_page.is_item_name_displayed()


@when('I click the Add to cart button')
def step_impl(context):
    context.account_page.click_add_to_cart()


@then('the error messages are displayed') #pas general pentru eroare, care sa fie parametrizat
def step_impl(context):
    assert context.account_page.are_error_messages_displayed()


@then('the messages read "{err}"')
def step_impl(context, err):
    assert context.account_page.check_error_messages(err)


@when('I choose the size "M"') #de parametrizat marimea
def step_impl(context):
    context.account_page.click_size()


@when('I click a different colour') #de parametrizat culoarea
def step_impl(context):
    context.account_page.change_colour()


@then('the item colour matches the chosen colour') #de parametrizat culoarea ((((mai bine scoasa :D))
def step_impl(context):
    assert context.account_page.check_if_colour_match()


@then('a confirmation message is displayed')
def step_impl(context):
    assert context.account_page.is_confirmation_message_displayed()


@then('the message reads "{confirmation}"')
def step_impl(context, confirmation):
    assert context.account_page.check_confirmation_message(confirmation)
#cei 2 pasi de mai sus = impreuna

@then('the number of items in the shopping cart is 1')# de parametrizat nr de produse
def step_impl(context):
    assert context.account_page.check_number_of_items()


@when('I click the shopping cart')
def step_impl(context):
    context.account_page.click_cart()


@when('I click the Proceed to checkout button')
def step_impl(context):
    context.account_page.click_proceed_to_checkout()

#nu are rost sa verif daca s-a incarcat pagina:
# @then('the shipping page loads')
# def step_impl(context):
#     assert context.account_page.check_shipping_page()


@when('I click on New address button')
def step_impl(context):
    context.account_page.click_new_address()


@when('I insert the requested info') #de facut pasi pentru fiecare field in parte
def step_impl(context):
    context.account_page.insert_shipping_info()


@when('I save the address')
def step_impl(context):
    context.account_page.click_save_address()


@when('I click on the Ship here button')
def step_impl(context):
    context.account_page.click_ship_here()


@when('I click the Next button')
def step_impl(context):
    context.account_page.click_next()


@then('the payment page loads')
def step_impl(context):
    assert context.account_page.check_payment_url()


@when('I check the billing address')
def step_impl(context):
    context.account_page.click_same_address()


@when('I click Place order button')
def step_impl(context):
    context.account_page.click_place_order()


@then('the success purchase page loads')
def step_impl(context):
    assert context.account_page.check_success_url()


# DE MODIFICAT = DE PUS ASSERT-UL IN PAGES