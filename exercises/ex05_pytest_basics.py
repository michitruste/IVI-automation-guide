"""Exercise 05: code under test. Don't change this file; write tests in test_ex05_pytest_basics.py."""


class FuelGauge:
    TANK_LITRES = 50.0
    WARNING_PERCENT = 10.0

    def __init__(self, litres: float = 0.0) -> None:
        self.litres = litres

    def refuel(self, litres: float) -> None:
        if litres <= 0:
            raise ValueError("refuel amount must be positive")
        if self.litres + litres > self.TANK_LITRES:
            raise ValueError("tank overflow")
        self.litres += litres

    def consume(self, litres: float) -> None:
        self.litres = max(0.0, self.litres - litres)

    @property
    def percent(self) -> float:
        return self.litres / self.TANK_LITRES * 100

    @property
    def warning(self) -> bool:
        return self.percent < self.WARNING_PERCENT
