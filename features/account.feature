#Feature: Test the functionality of the account page
#
#  Background:
#    Given I am on the main page
#
#  Scenario: I register a shipping address
#    When I click on sign in button
#    Then The sign in window opens
#    When I insert "ralukaruxandra@gmail.com" in the email input
#    When I insert "Password1" in the password input
#    When I click on the Login button
#    Then The account page loads
##    When I click on the customer menu arrow
##    When I click on my account
##    When I click on edit billing address
#
##    When I insert the requested info
##    When I save the address
#
#  Scenario: Change the color of an item, add the item in the cart and buy the item
#    When I hover the mouse over Women, Tops, Jackets and I click Jackets
#    When I click the first item
#    Then the item page opens
#    Then the item name is displayed   >>>NU ESTE NEAPARAT NEVOIE
#    When I click the Add to cart button
#    Then the error messages are displayed  >>> DE PUS IMPREUNA CU 27
#    Then the messages read "This is a required field."
#    When I choose the size "M"
#    When I click a different colour
##    Then the item colour matches the chosen colour >> NU ESTE NECESARA
#    When I click the Add to cart button
#    Then a confirmation message is displayed >>> SCENARIU PANA AICI
#    Then the message reads "You added Olivia 1/4 Zip Light Jacket to your shopping cart." >> NOU SCENARIU
#    Then the number of items in the shopping cart is 1
#    When I click the shopping cart
#    When I click the Proceed to checkout button
#    Then the shipping page loads
#    When I click on the Ship here button
#    When I click the Next button
#    Then the payment page loads
#    When I check the billing address
#    When I click Place order button
#    Then the success purchase page loads
