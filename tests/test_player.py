import pytest

from ivi.player import InvalidTransition, MediaPlayer


def test_playing_state(player):
    player.play()
    assert player.state == "PLAYING"


@pytest.mark.parametrize("freq", [87.4, 108.1, 200])
def test_frequencies(tuner, freq):
    with pytest.raises(ValueError):
        tuner.frequency = freq
    

@pytest.mark.parametrize("freq", [87.5, 99.9, 108.0])
def test_valid_frequency(tuner, freq):          # fixture + parameter together
    tuner.frequency = freq
    assert tuner.frequency == freq


@pytest.mark.parametrize("freq", [87.4, 108.1, 0, -1])
def test_invalid_frequency(tuner, freq):
    with pytest.raises(ValueError):
        tuner.frequency = freq


@pytest.mark.parametrize(
    "start, action, expected",
    [
        ("STOPPED", "play", "PLAYING"),
        ("PLAYING", "pause", "PAUSED"),
        ("PAUSED", "play", "PLAYING"),
        ("PLAYING", "stop", "STOPPED"),
    ],
    ids=["stop-play", "play-pause", "pause-play", "play-stop"],
)
def test_valid_transition(start, action, expected):
    player = MediaPlayer(state=start)
    getattr(player, action)()                   # e.g. player.play()
    assert player.state == expected


@pytest.mark.parametrize(
    "start, action",
    [
        ("STOPPED", "pause"),
        ("STOPPED", "stop"),
        pytest.param("PAUSED", "pause", id="double-pause"),
    ],
)
def test_invalid_transition(start, action):
    player = MediaPlayer(state=start)
    with pytest.raises(InvalidTransition):
        getattr(player, action)()
    assert player.state == start                # state is unchanged


@pytest.mark.parametrize("volume", [0, 50])
@pytest.mark.parametrize("source", ["usb", "bt", "fm"])
def test_mute_all_sources(source, volume):      # 2 × 3 = 6 tests
    ...