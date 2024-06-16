Feature: Test the functionality of the account page

  Background:
    Given I am on the main page
    When I click on sign in button
    Then The sign in window opens
    When I insert "ralukaruxandra@gmail.com" in the email input
    When I insert "Password1" in the password input
    When I click on the Login button
    Then The account page loads

  @change_shipping_address
  Scenario: I register a shipping address

    When I click on the customer menu arrow
    When I click on my account
    When I click on edit address under default shipping address
    When I put in the required info
#    When I click the save address button
    Then The address page loads
    When I click on the dropdown arrow
    When I click on the sign out link

  @add_item_in_cart
  Scenario: Change the color of an item and add the item in the cart
    When I hover the mouse over Women, Tops, Jackets and I click Jackets
    When I click the first item
    Then the item page opens
    When I click the Add to cart button
    Then The error messages "This is a required field." are displayed
    When I choose the size "M"
    When I click a different colour
    When I click the Add to cart button
    Then The confirmation message "You added Olivia 1/4 Zip Light Jacket to your shopping cart." is displayed
    When I click on the dropdown arrow
    When I click on the sign out link

    @buy
    Scenario: Buy a product
    When I click the shopping cart
    When I click the Proceed to checkout button
    Then The shipping page loads
    When I click the Next button
    Then The payment page loads
    When I confirm the billing address
    When I click Place order button
    Then the success purchase page loads
    When I click on the dropdown arrow
    When I click on the sign out link
