# language: en
Feature: Login Form

  As a user
  I want to log in to the website
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "tomsmith" and password "SuperSecretPassword!"
    And I click the login button
    Then I should see the success message
    And I should be logged in successfully 