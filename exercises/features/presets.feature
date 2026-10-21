# Exercise 10: write the scenarios below, then the one missing step in steps/preset_steps.py.
#   Run:  behave exercises/features
#   Undefined steps are listed with a code snippet you can paste and fill in.
Feature: Radio presets

  Background:
    Given the infotainment system is powered on
    And the radio is on

  # 10.1  Scenario: selecting preset 2 shows "101.1 FM".
  #       It needs a new step:  When I select preset 2

  # 10.2  Scenario Outline: presets 1, 2 and 3 show "89.3 FM", "101.1 FM" and "104.5 FM".

  # 10.3  Tag one scenario @wip and leave it out with:
  #       behave exercises/features --tags="not @wip"
