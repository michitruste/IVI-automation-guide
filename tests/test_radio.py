import pytest

from ivi.radio import RadioTuner


def test_default_frequency():
    assert RadioTuner().frequency == 87.5


def test_rejects_out_of_band():
    tuner = RadioTuner()
    with pytest.raises(ValueError, match="out of FM band"):
        tuner.frequency = 200


def test_preset_two():
    tuner = RadioTuner.from_preset(2)
    assert tuner.frequency == pytest.approx(101.1)


class TestPower:                 # grouping; no __init__ allowed
    def test_starts_off(self):
        assert not RadioTuner().is_on

    def test_power_on(self):
        tuner = RadioTuner()
        tuner.power_on()
        assert tuner.is_on
