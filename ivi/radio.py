class RadioTuner:
    MIN_FREQ = 87.5    # class attributes: shared by all tuners
    MAX_FREQ = 108.0

    def __init__(self, frequency: float = 87.5) -> None:
        self._frequency = frequency    # instance state, "internal" by convention
        self._is_on = False

    @classmethod
    def from_preset(cls, preset: int) -> "RadioTuner":
        presets = {1: 89.3, 2: 101.1, 3: 104.5}
        return cls(presets[preset])    # alternate constructor

    @property
    def frequency(self) -> float:     # read: tuner.frequency
        return self._frequency

    @frequency.setter
    def frequency(self, value: float) -> None:   # write: tuner.frequency = 99.5
        if not self.MIN_FREQ <= value <= self.MAX_FREQ:
            raise ValueError(f"{value} MHz out of FM band")
        self._frequency = value

    @property
    def is_on(self) -> bool:          # read-only: no setter defined
        return self._is_on

    def power_on(self) -> None:
        self._is_on = True

    def power_off(self) -> None:
        self._is_on = False

    def __repr__(self) -> str:
        return f"RadioTuner(frequency={self._frequency})"


tuner = RadioTuner()
print(tuner.is_on)
print(tuner.frequency)
tuner.power_on()
print(tuner.is_on)
print(tuner.frequency)
tuner.frequency = 101.1     # runs the setter, passes validation
print(tuner.is_on)
print(tuner.frequency)
# tuner.frequency = 200       # ValueError: 200 MHz out of FM band
# tuner.is_on = False         # AttributeError: property has no setter