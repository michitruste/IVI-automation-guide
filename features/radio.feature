@radio
Feature: FM radio tuning
  As a driver
  I want to tune the radio
  So that I can listen to my station

  Background:
    Given the infotainment system is powered on

  @smoke
  Scenario: Tune to a valid station
    Given the radio is on
    When I tune to 101.1 MHz
    Then the display shows "101.1 FM"

  Scenario Outline: Reject frequencies outside the FM band
    Given the radio is on
    When I tune to <freq> MHz
    Then I see the error "Out of band"
    And the display shows "87.5 FM"

    Examples:
      | freq  |
      | 87.4  |
      | 108.1 |
      | 0     |
