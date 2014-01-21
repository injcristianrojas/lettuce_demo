Feature: Meetup

  Scenario: Check Meetup Data
    When I go to "http://www.meetup.com/"
    And I fill in "C_globalSearchInput" with "Meetup Python"
    And I press "C_globalSearchBtn"
    I should see "Pythoneros"
