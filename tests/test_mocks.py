from unittest.mock import MagicMock, Mock, call, patch

import pytest

from ivi.bluetooth import BluetoothManager
from ivi.hvac import Bus, HvacController


def test_hvac_sends_frame():
    bus = Mock(spec=Bus)                   # stands in for the CAN adapter
    HvacController(bus).set_temp(22)
    bus.send.assert_called_once_with(0x3A0, bytes([22]))


def test_hvac_propagates_timeout():
    bus = Mock(spec=Bus)
    bus.send.side_effect = TimeoutError("no ACK")   # simulate a dead ECU
    with pytest.raises(TimeoutError):
        HvacController(bus).set_temp(22)


def test_sequence_of_reads():
    sensor = Mock()
    sensor.read.side_effect = [21, 22, 23]          # one value per call
    assert [sensor.read() for _ in range(3)] == [21, 22, 23]


def test_ramp_sends_each_step():
    bus = Mock(spec=Bus)
    hvac = HvacController(bus)
    hvac.set_temp(20)
    hvac.set_temp(21)
    assert bus.send.call_args_list == [
        call(0x3A0, bytes([20])),
        call(0x3A0, bytes([21])),
    ]


# ivi/bluetooth.py contains:  from ivi.hw import scan_devices
@patch("ivi.bluetooth.scan_devices")     # patch where it is USED
def test_pair_first_device(mock_scan):
    mock_scan.return_value = ["Pixel 8", "iPhone 15"]
    assert BluetoothManager().pair_first() == "Pixel 8"
    mock_scan.assert_called_once()


def test_context_manager_style():
    with patch("ivi.bluetooth.scan_devices", return_value=[]) as mock_scan:
        assert BluetoothManager().pair_first() is None
    mock_scan.assert_called_once()


@patch("ivi.bluetooth.signal_strength")  # outer → second argument
@patch("ivi.bluetooth.scan_devices")     # inner → first argument
def test_strongest_device(mock_scan, mock_rssi):
    mock_scan.return_value = ["Pixel 8", "iPhone 15"]
    mock_rssi.side_effect = {"Pixel 8": -70, "iPhone 15": -40}.get   # a function: called with each device
    assert BluetoothManager().strongest() == "iPhone 15"


def test_magic_methods():
    playlist = MagicMock()
    playlist.__len__.return_value = 12     # Mock() would not support len()
    assert len(playlist) == 12
