class InvalidTransition(Exception):
    pass


class MediaPlayer:
    TRANSITIONS = {
        ("STOPPED", "play"): "PLAYING",
        ("PLAYING", "pause"): "PAUSED",
        ("PAUSED", "play"): "PLAYING",
        ("PLAYING", "stop"): "STOPPED",
        ("PAUSED", "stop"): "STOPPED",
    }

    def __init__(self, state: str = "STOPPED") -> None:
        self.state = state

    def _go(self, action: str) -> None:
        key = (self.state, action)
        if key not in self.TRANSITIONS:
            raise InvalidTransition(f"cannot {action} from {self.state}")
        self.state = self.TRANSITIONS[key]

    def play(self) -> None:
        self._go("play")

    def pause(self) -> None:
        self._go("pause")

    def stop(self) -> None:
        self._go("stop")