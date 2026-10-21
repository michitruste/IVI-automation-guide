import pytest

from exercises.ex01_classes import Playlist, VolumeControl


def test_default_level():
    assert VolumeControl().level == 10


def test_set_level():
    vol = VolumeControl()
    vol.level = 25
    assert vol.level == 25


@pytest.mark.parametrize("bad", [-1, 31])
def test_rejects_out_of_range(bad):
    with pytest.raises(ValueError):
        VolumeControl().level = bad
    with pytest.raises(ValueError):
        VolumeControl(bad)


def test_up_and_down_stop_at_limits():
    vol = VolumeControl(30)
    vol.up()
    assert vol.level == 30
    vol = VolumeControl(0)
    vol.down()
    assert vol.level == 0


def test_mute_and_unmute():
    vol = VolumeControl(18)
    vol.mute()
    assert vol.level == 0
    vol.unmute()
    assert vol.level == 18


def test_repr():
    assert repr(VolumeControl(12)) == "VolumeControl(level=12)"


def test_playlists_do_not_share_songs():
    a = Playlist()
    b = Playlist()
    a.add("Take On Me")
    assert b.songs == []
