Feature: Test the functionality of the Register page

  Background:
    Given I am on the main page

  Scenario: Check that I can register a new user
    When I click on the create an account link
    Then The create account page loads
    When I insert the first name
    When I insert the last name
    When I insert the new email
    When I insert "Password1" in the password box
    When I click on the create an account button
    Then The new user is logged in >>>> PANA AICI SCENARIU 1
    When I click on the dropdown arrow >>> DE AICI SCENARIU 2
    When I click on the sign out link
    Then The logout page loads