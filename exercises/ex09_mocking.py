"""Exercise 09: code under test. Don't change this file; write tests in test_ex09_mocking.py.

scan_devices() needs a Bluetooth chip and time.sleep() makes tests slow, so mock both.
"""
import time

from ivi.hw import scan_devices


class PhoneConnector:
    def __init__(self, known_phones: list[str], retries: int = 3) -> None:
        self.known_phones = known_phones
        self.retries = retries

    def connect(self) -> str | None:
        for _ in range(self.retries):
            try:
                found = scan_devices()
            except TimeoutError:
                time.sleep(1)             # wait before scanning again
                continue
            for phone in self.known_phones:
                if phone in found:
                    return phone
            return None
        raise ConnectionError("Bluetooth scan kept timing out")
