import subprocess
import sys
from pathlib import Path

TARGET = Path(__file__).with_name("ex04_ruff.py")


def ruff(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "ruff", *args, "--no-cache", str(TARGET)],
        capture_output=True,
        text=True,
    )


def test_ruff_check_is_clean():
    result = ruff("check")
    assert result.returncode == 0, result.stdout


def test_ruff_format_is_clean():
    result = ruff("format", "--check")
    assert result.returncode == 0, result.stdout + result.stderr


def test_no_noqa_shortcuts():
    assert "noqa" not in TARGET.read_text()


def test_behavior_kept_with_pep8_names():
    from exercises.ex04_ruff import TripComputer, to_json

    trip = TripComputer(200, 12)
    assert trip.distance_km == 200
    assert trip.consumption() == 6.0
    assert TripComputer(200, None).consumption() is None
    assert to_json(trip) == '{"km": 200, "litres": 12}'
