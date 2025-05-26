# language: en
Feature: Google Search

  As an internet user
  I want to search information on Google
  So that I can find the data I need

  Scenario: Successful Google search
    Given I am on the Google page
    When I search for "Python BDD testing"
    Then I see search results
    And the first result contains "Python" 