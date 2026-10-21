from typing import Protocol

HVAC_TEMP_ID = 0x3A0    # CAN message ID for the temperature request


class Bus(Protocol):
    """Anything with a send() method can act as the bus: real hardware, a fake, or a Mock."""

    def send(self, msg_id: int, data: bytes) -> None: ...


class HvacController:
    def __init__(self, bus: Bus) -> None:
        self.bus = bus                     # injected, not created here (DIP)

    def set_temp(self, celsius: int) -> None:
        self.bus.send(HVAC_TEMP_ID, bytes([celsius]))
