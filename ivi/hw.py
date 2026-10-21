"""Calls that would talk to real hardware. On a laptop there is no Bluetooth chip, so tests mock these."""


def scan_devices() -> list[str]:
    raise RuntimeError("no Bluetooth adapter found")


def signal_strength(device: str) -> int:
    """RSSI in dBm: closer to 0 is stronger, e.g. -40 is better than -70."""
    raise RuntimeError("no Bluetooth adapter found")
