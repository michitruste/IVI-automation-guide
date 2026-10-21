import pytest

from ivi.hvac import HvacController
from ivi.radio import RadioTuner
from ivi.player import MediaPlayer
from tests.fakes import FakeCanBus


@pytest.fixture
def tuner():
    t = RadioTuner()
    t.power_on()
    yield t              # the test runs here
    t.power_off()        # teardown: runs even if the test failed


@pytest.fixture(scope="session")
def can_bus():
    bus = FakeCanBus()   # expensive: created once for the whole run
    yield bus
    bus.shutdown()


@pytest.fixture
def hvac(can_bus):       # a fixture that uses another fixture
    return HvacController(can_bus)

@pytest.fixture
def player():
    return MediaPlayer()