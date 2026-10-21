"""Exercise 09: write these tests with unittest.mock. No test may touch real hardware or really sleep.

Run:  pytest exercises/test_ex09_mocking.py -v
Tip: ex09_mocking.py did `from ivi.hw import scan_devices`. Where must you patch it?
"""
from unittest.mock import patch  # noqa: F401  (you'll use it)

import pytest

from exercises.ex09_mocking import PhoneConnector  # noqa: F401


# 9.1  scan_devices returns ["Galaxy S24", "Pixel 8"]; known phones are ["Pixel 8"].
#      connect() returns "Pixel 8" and scan_devices was called exactly once.
def test_connects_to_known_phone():
    pytest.fail("TODO")


# 9.2  No known phone nearby: connect() returns None.
def test_no_known_phone():
    pytest.fail("TODO")


# 9.3  The first scan times out, the second finds the phone. Use side_effect with a list.
#      Also patch time.sleep: check it was called once with 1, and that scan ran twice.
def test_retries_after_timeout():
    pytest.fail("TODO")


# 9.4  Every scan times out: connect() raises ConnectionError after 3 scans and 3 sleeps.
def test_gives_up_after_retries():
    pytest.fail("TODO")
