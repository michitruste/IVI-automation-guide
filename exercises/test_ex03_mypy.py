from pathlib import Path

import pytest
from mypy import api

from exercises.ex03_mypy import average_temp, parse_volume, station_label

STATIONS = {101.1: "Jazz FM", 104.5: "Rock 104"}


def test_mypy_strict_is_clean():
    path = Path(__file__).with_name("ex03_mypy.py")
    stdout, stderr, exit_code = api.run(["--strict", "--no-incremental", str(path)])
    assert exit_code == 0, stdout


def test_average_temp():
    assert average_temp([20.0, 22.0]) == 21.0


def test_station_label_found():
    assert station_label(STATIONS, "Rock 104") == "104.5 FM"


def test_station_label_missing():
    assert station_label(STATIONS, "Talk Radio") == "No signal"


def test_parse_volume():
    assert parse_volume("12") == 12


def test_parse_volume_rejects_text():
    with pytest.raises(ValueError):
        parse_volume("loud")
