@register_feature
Feature: Test the functionality of the Register page

  Background:
    Given I am on the main page

  Scenario: Check that I can register a new user
    When I click on the create an account link
    Then The create account page loads
    When I insert "Miao" as first name
    When I insert "Hhhhhh" as last name
    When I insert the new email
    When I insert "Password1" in the password box
    When I click on the create an account button
    Then The new user is logged in

    Scenario: Check if a registered user can logout
    When I click on the dropdown arrow
    When I click on the sign out link
    Then The logout page loads