"""Exercise 01: classes and object state.

Check your work:  pytest exercises/test_ex01_classes.py -v
"""


# 1.1  Finish VolumeControl. Replace every `raise NotImplementedError`.
class VolumeControl:
    MAX = 30

    def __init__(self, level: int = 10) -> None:
        raise NotImplementedError   # store the level (validate it the same way the setter does)

    @property
    def level(self) -> int:
        raise NotImplementedError

    @level.setter
    def level(self, value: int) -> None:
        raise NotImplementedError   # ValueError if value is outside 0..MAX

    def up(self) -> None:
        raise NotImplementedError   # +1, but never above MAX (no error)

    def down(self) -> None:
        raise NotImplementedError   # -1, but never below 0 (no error)

    def mute(self) -> None:
        raise NotImplementedError   # remember the current level, then go to 0

    def unmute(self) -> None:
        raise NotImplementedError   # go back to the level saved by mute()

    def __repr__(self) -> str:
        raise NotImplementedError   # "VolumeControl(level=12)"


# 1.2  This class has a bug: two playlists created without arguments share songs. Fix it.
class Playlist:
    def __init__(self, songs=[]):
        self.songs = songs

    def add(self, song: str) -> None:
        self.songs.append(song)
