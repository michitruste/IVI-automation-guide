def test_tune(tuner):                    # gets a fresh, powered-on tuner
    tuner.frequency = 99.5
    assert tuner.frequency == 99.5


def test_set_temp(hvac, can_bus):        # same can_bus object hvac received
    hvac.set_temp(22)
    assert can_bus.last_frame == (0x3A0, bytes([22]))


def test_export_log(tmp_path):
    log = tmp_path / "hvac.log"          # pathlib.Path in a temp folder
    log.write_text("temp=22")
    assert log.read_text() == "temp=22"
