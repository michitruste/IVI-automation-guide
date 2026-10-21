class FakeCanBus:
    """Stands in for the CAN adapter. Remembers what was sent instead of sending it."""

    def __init__(self) -> None:
        self.frames: list[tuple[int, bytes]] = []

    def send(self, msg_id: int, data: bytes) -> None:
        self.frames.append((msg_id, data))

    @property
    def last_frame(self) -> tuple[int, bytes] | None:
        return self.frames[-1] if self.frames else None

    def shutdown(self) -> None:
        self.frames.clear()