"""Exercise 06: code under test. Don't change this file; write fixtures in test_ex06_fixtures.py."""
from pathlib import Path


class TripLog:
    """Appends one trip distance per line to a text file."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.closed = False

    def add(self, km: float) -> None:
        if self.closed:
            raise RuntimeError("log is closed")
        with self.path.open("a") as f:
            f.write(f"{km}\n")

    def total(self) -> float:
        if not self.path.exists():
            return 0.0
        return sum(float(line) for line in self.path.read_text().splitlines())

    def close(self) -> None:
        self.closed = True
