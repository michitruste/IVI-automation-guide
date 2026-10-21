"""Exercise 06: the tests are written. They ask for fixtures that don't exist yet; write them.

Run:  pytest exercises/test_ex06_fixtures.py -v
Until a fixture exists, its tests show as E (error in setup), not F.
"""
import pytest  # noqa: F401  (you'll use it)

from exercises.ex05_pytest_basics import FuelGauge  # noqa: F401
from exercises.ex06_fixtures import TripLog  # noqa: F401

# 6.1  A fixture named `half_tank` that returns FuelGauge(25.0).

# 6.2  A fixture named `trip_log` that returns a TripLog writing to a file
#      inside pytest's built-in `tmp_path` folder.

# 6.3  A yield fixture named `open_log` that uses `trip_log`, yields it,
#      and calls .close() on it afterwards (teardown).


def test_half_tank_percent(half_tank):
    assert half_tank.percent == 50


def test_half_tank_is_fresh_each_time(half_tank):
    half_tank.consume(25)           # if the fixture were shared, the next test would break
    assert half_tank.litres == 0


def test_half_tank_still_half(half_tank):
    assert half_tank.litres == 25


def test_empty_log(trip_log):
    assert trip_log.total() == 0


def test_log_adds_up(trip_log):
    trip_log.add(12.5)
    trip_log.add(7.5)
    assert trip_log.total() == 20


def test_log_file_is_in_tmp_path(trip_log, tmp_path):
    assert trip_log.path.parent == tmp_path


def test_open_log_is_open(open_log):
    open_log.add(3)
    assert not open_log.closed
