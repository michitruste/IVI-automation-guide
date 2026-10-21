from abc import ABC, abstractmethod


class MediaSource:
    def __init__(self, name: str) -> None:
        self.name = name
        self.playing = False

    def play(self) -> str:
        self.playing = True
        return f"{self.name}: playing"


class BluetoothAudio(MediaSource):
    def __init__(self, device: str) -> None:
        super().__init__("Bluetooth")    # run the parent's setup first
        self.device = device

    def play(self) -> str:               # override
        base = super().play()            # reuse the parent's logic
        return f"{base} from {self.device}"


class USBAudio(MediaSource):
    def __init__(self) -> None:
        super().__init__("USB")          # play() is inherited unchanged


def start_all(sources: list[MediaSource]) -> list[str]:
    return [s.play() for s in sources]   # same call, different behavior


class Display(ABC):                      # an interface every screen must follow
    @abstractmethod
    def render(self, text: str) -> None: ...


class ClusterDisplay(Display):
    def render(self, text: str) -> None:
        print(f"[cluster] {text}")


if __name__ == "__main__":      # python -m ivi.media
    print(start_all([BluetoothAudio("Pixel 8"), USBAudio()]))
    # ['Bluetooth: playing from Pixel 8', 'USB: playing']
    ClusterDisplay().render("Now playing")   # [cluster] Now playing
    # Display()   # TypeError: Can't instantiate abstract class Display ...
