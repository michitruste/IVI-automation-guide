"""Exercise 07: turn each stub into a parametrized test.

Run:  pytest exercises/test_ex07_parametrize.py -v
Each case should show up as its own line, e.g. test_valid_shift[P-R].
"""
import pytest

from exercises.ex07_parametrize import InvalidShiftError, Transmission  # noqa: F401


# 7.1  Valid shifts at 0 km/h. Parametrize over (start, target) with at least 5 cases,
#      and give each case a readable id like "P-R".
def test_valid_shift():
    pytest.fail("TODO")


# 7.2  Invalid shifts. Parametrize over (start, target) pairs that aren't allowed
#      (e.g. P -> D, D -> R). Expect InvalidShiftError and check the gear didn't change.
def test_invalid_shift():
    pytest.fail("TODO")


# 7.3  Selecting P while moving must fail. Stack two parametrize decorators:
#      start gear in ["N", "R"], speed in [5, 50, 120]. That's 6 tests.
def test_park_while_moving_fails():
    pytest.fail("TODO")
