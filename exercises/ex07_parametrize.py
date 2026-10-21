"""Exercise 07: code under test. Don't change this file; write tests in test_ex07_parametrize.py."""


class InvalidShiftError(Exception):
    pass


class Transmission:
    ALLOWED = {
        "P": {"R", "N"},
        "R": {"P", "N"},
        "N": {"P", "R", "D"},
        "D": {"N"},
    }

    def __init__(self, gear: str = "P") -> None:
        self.gear = gear

    def shift(self, target: str, speed_kmh: float = 0) -> None:
        if target not in self.ALLOWED[self.gear]:
            raise InvalidShiftError(f"cannot shift {self.gear} -> {target}")
        if target in {"P", "R"} and speed_kmh > 0:
            raise InvalidShiftError(f"cannot select {target} while moving")
        self.gear = target
