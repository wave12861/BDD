# language: en
Feature: Add item to cart

  As an online shop user
  I want to add an item to the cart
  So that I can place an order

  Scenario: Successful add to cart
    Given I am on the main page
    When I add the item "Телефон" to the cart
    Then the item "Телефон" should appear in the cart 