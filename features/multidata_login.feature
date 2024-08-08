Feature: Testing with Multi data for Orange HRM login Page

  Scenario Outline: Login to Orange HRM with Multiple parameters
    Given I Launch the browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:

      | username | password |
      | admin    | admin1   |
      | admin    | admin12  |
      | admin12  | admin    |
      | Admin    | admin123 |


