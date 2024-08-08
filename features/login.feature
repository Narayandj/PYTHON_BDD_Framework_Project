Feature: Login functionality of the main page

  Scenario: Login with valid username and password
    Given Launch the browser
    When enter the valid username "admin" and password "admin123"
    And click on login button
    Then verify home page

