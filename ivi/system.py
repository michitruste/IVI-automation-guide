from pathlib import Path

from ivi.radio import RadioTuner


class Display:
    def __init__(self) -> None:
        self.text = ""
        self.error: str | None = None

    def show(self, text: str) -> None:
        self.text = text
        self.error = None


class RadioApp:
    """The radio screen: drives a RadioTuner and reports what happened on the display."""

    def __init__(self, tuner: RadioTuner, display: Display) -> None:
        self.tuner = tuner
        self.display = display

    def power_on(self) -> None:
        self.tuner.power_on()
        self._show_frequency()

    def tune(self, freq: float) -> None:
        try:
            self.tuner.frequency = freq
        except ValueError:
            self.display.error = "Out of band"    # keep the old station on screen
            return
        self._show_frequency()

    def select_preset(self, preset: int) -> None:
        self.tune(RadioTuner.from_preset(preset).frequency)

    def _show_frequency(self) -> None:
        self.display.show(f"{self.tuner.frequency} FM")


class InfotainmentSystem:
    def __init__(self, simulated: bool = True) -> None:
        if not simulated:
            raise NotImplementedError("only the simulator is available")
        self.display = Display()
        self.radio = RadioApp(RadioTuner(), self.display)
        self.booted = False

    def boot(self) -> None:
        self.booted = True
        self.display.show("Welcome")

    def save_screenshot(self, path: str) -> None:
        """The simulator has no screen, so the 'screenshot' is a text dump of the display."""
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"text={self.display.text}\nerror={self.display.error}\n")

    def shutdown(self) -> None:
        self.radio.tuner.power_off()
        self.booted = False
