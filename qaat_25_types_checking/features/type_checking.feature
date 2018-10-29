# Created by yan at 25.10.18
Feature: validation api/v3/pages/library

  Scenario: Validate showcase and item types
    Given token authorization
    When send request
    Then validation response schema
    Then get all showcases types
    Then validation types showcases and items