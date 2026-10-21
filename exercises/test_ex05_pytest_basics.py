"""Exercise 05: write the tests. Replace each pytest.fail() with a real test body.

Run:  pytest exercises/test_ex05_pytest_basics.py -v
"""
import pytest

from exercises.ex05_pytest_basics import FuelGauge  # noqa: F401  (you'll use it)


# 5.1  Plain asserts
def test_starts_empty():
    pytest.fail("TODO: a new FuelGauge() has 0 litres")


def test_refuel_adds_litres():
    pytest.fail("TODO: refuel 20 litres into an empty gauge, check litres is 20")


def test_consume_never_goes_below_zero():
    pytest.fail("TODO: FuelGauge(5) consumes 8 litres, litres is 0")


# 5.2  Floats and exceptions
def test_percent_one_third():
    pytest.fail("TODO: 50 / 3 litres is 33.33...%, compare with pytest.approx")


def test_refuel_negative_raises():
    pytest.fail('TODO: refuel(-5) raises ValueError whose message contains "positive"')


def test_refuel_overflow_raises():
    pytest.fail('TODO: FuelGauge(45).refuel(10) raises ValueError matching "overflow"')


# 5.3  Group the warning tests in a class (pytest collects classes named Test*)
def test_warning_below_ten_percent():
    pytest.fail("TODO: move into class TestWarning; 4 litres (8%) means warning is True")


def test_no_warning_at_ten_percent():
    pytest.fail("TODO: move into class TestWarning; 5 litres (exactly 10%) means warning is False")
