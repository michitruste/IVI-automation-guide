import pytest

from exercises import ex02_inheritance as ex
from ivi.media import MediaSource, start_all


def test_carplay_is_a_media_source():
    carplay = ex.CarPlayAudio("iPhone 15")
    assert isinstance(carplay, MediaSource)
    assert carplay.name == "CarPlay"
    assert carplay.phone == "iPhone 15"


def test_carplay_play_reuses_parent():
    carplay = ex.CarPlayAudio("iPhone 15")
    assert carplay.play() == "CarPlay: playing via iPhone 15"
    assert carplay.playing is True


def test_carplay_works_with_start_all():
    assert start_all([ex.CarPlayAudio("Pixel 8")]) == ["CarPlay: playing via Pixel 8"]


def test_notification_is_abstract():
    with pytest.raises(TypeError):
        ex.Notification()


def test_low_fuel_warning():
    assert ex.LowFuelWarning(42).render() == "[WARNING] Low fuel: 42 km left"


def test_incoming_call():
    assert ex.IncomingCall("Alex").render() == "[INFO] Call from Alex"


def test_render_is_inherited():
    assert "render" not in vars(ex.LowFuelWarning)
    assert "render" not in vars(ex.IncomingCall)
