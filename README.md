**TESTED APPLICATION**
https://magento.softwaretestingboard.com/ 
I chose to check the website of the Luma. The evaluation of the " Sign In" and " Create an Account" pages were my main concern. To make sure that all these functions work properly, we checked functionalities such as: creating an account, sign in to the new account, sign out, validating error messages, using an invalid email address, user or account, etc.
**LANGUAGE, IDE, BOOKSTORES**
I chose to perform the testing using the Python programming language and the PyCharm IDE. I used Selenium, webdriver-manager, behave and behave-html-formatter libraries, facker, time random, unittest to automate the interaction with the Luma website. The "Python Packages" section of PyCharm can be accessed to install these libraries. After adding the name of the desired library in the field, I pressed the "Install" button.
**THE IMPORTANCE OF AUTOMATED TESTING**
Efficiency in software development depends on automated testing. Speed, reproducibility, extended coverage, reusability, ease of integration with agile development practices and early detection of errors are the main benefits. This constantly helps to ensure the quality of the software.
**THE CHOSEN METHODOLOGY**
The software development methodology called BDD (Behavior-Driven Development) focuses on the collaboration of team members and on describing the behavior of the application in a simple language, such as Gherkin. We chose BDD to facilitate communication between developers, testers and other interested parties and to create automated tests that reflect the behavior clearly specified by stakeholders. Benefits include: clear communication, easy-to-understand and up-to-date tests, and alignment between requirements and implementation. BDD encourages teamwork and guarantees that development focuses on developing useful functionalities that meet user expectations.
**USE OF THE PROJECT**
Using the project starts by cloning it from GitHub. Access the project, press the green "Code" button, copy the link, navigate on the computer to the desired folder, open Git Bash, write the command "git clone" followed by the link and press "Enter". The cloned project can be opened in PyCharm. To run tests, use the command "behave -f html -o behave-report.html" in the terminal. To view the generated report, open the "behave-report.html" file in Chrome.
**STRUCTURE OF THE PROJECT**
The project has a structure consisting of a series of files and directories. We find settings for opening Chrome, maximizing the window and a default wait of one seconds in the "browser" file. We have the structure of the pages tested in the "environment". "features", "pages" and "steps" are the three directories that make up the general structure. The test scenarios are written in Gherkin syntax and can be found in the "features" category. We have general methods for actions such as clicking, finding the element, typing, etc. defined in "pages". The other files contain locators and specific methods for the suggested scenarios. The Gherkin syntax defines the functions of the "steps" directory. This structure organizes the code for automated tests.
**SCREENSHOTS WITH THE CODE**
![image](https://github.com/RalukaRuxandra/automation_testing_bdd_magento/assets/130061878/f9c88044-cec7-4fd6-bd62-cbb95dab186c)
![image](https://github.com/RalukaRuxandra/automation_testing_bdd_magento/assets/130061878/a028781b-1ae8-4dfc-8a17-2ebc37ab2ff7)
![image](https://github.com/RalukaRuxandra/automation_testing_bdd_magento/assets/130061878/7380ead7-f6a4-44a1-b040-c3438c89dea7)
![image](https://github.com/RalukaRuxandra/automation_testing_bdd_magento/assets/130061878/487e6890-99f0-4b53-86b7-a21105fb1a28)


**SCENARIOS**
Test scenarios chosen for evaluation include:
•	Check that "This is a required field." message is displayed when the user enters an empty password
•	Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later" message is displayed when the user tries to log in with an unregistered email
•	Check that you cannot login when providing invalid credential
•	I put in the correct username and password and check if the sing in window opens
•	Check that I can register a new user
•	Check if a registered user can logout
•	I register a shipping address
•	Change the color of an item and add the item in the cart
•	Buy a product
These scenarios cover a variety of situations to ensure that the key functionalities of the application are tested exhaustively and that errors can be identified and handled accordingly.

