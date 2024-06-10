@sign_in_page
Feature:Test the functionality of the Sign In Page

  Background:
    Given I am on the main page
    When I click on sign in button

#>>>SCENARIU DE LOG OUT
  @password_required
  Scenario: Check that "This is a required field." message is displayed when the user enters an empty password
    When I insert "ralukaruxandra@gmail.com" in the email input
    When I insert " " in the password input
    When I click on the Login button
    Then The password error message "This is a required field." is displayed


  @no_account
  Scenario: Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later" message is displayed when the user tries to log in with an unregistered email
    When I insert "maria.mariana@gmail.com" in the email input
    When I insert "Password1" in the password input
    When I click on the Login button
    Then The account error message "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later" is displayed

 @invalid_login
 Scenario Outline: check that you cannot login when providing invalid credential
   When i insert username "<username>" and password "<password>"
   When I click on the Login button
   Then i cannot login into the application and i receive "<error_message>" error
   Examples:
     | username | password  | error_message                                               |
     | abcd     | Password1 | Please enter a valid email address (Ex: johndoe@domain.com) |
     | space    | Password1 | This is a required field.                                   |

  @valid_login
  Scenario: I put in the correct username and password and check if the sing in window opens
    When I insert "ralukaruxandra@gmail.com" in the email input
    When I insert "Password1" in the password input
    When I click on the Login button
    Then The account page loads
    Then The welcome message is displayed
