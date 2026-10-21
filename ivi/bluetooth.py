# This import copies the names into THIS module, so tests patch ivi.bluetooth.<name>, not ivi.hw.<name>.
from ivi.hw import scan_devices, signal_strength


class BluetoothManager:
    def __init__(self) -> None:
        self.paired: str | None = None

    def pair_first(self) -> str | None:
        devices = scan_devices()           # looked up here → patch "ivi.bluetooth.scan_devices"
        if not devices:
            return None
        self.paired = devices[0]
        return self.paired

    def strongest(self) -> str | None:
        devices = scan_devices()
        if not devices:
            return None
        return max(devices, key=signal_strength)
