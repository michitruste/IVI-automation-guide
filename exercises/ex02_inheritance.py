"""Exercise 02: inheritance, super() and abstract classes.

Check your work:  pytest exercises/test_ex02_inheritance.py -v
"""
from abc import ABC, abstractmethod

from ivi.media import MediaSource


# 2.1  Write CarPlayAudio, a MediaSource subclass:
#      - CarPlayAudio("iPhone 15") has name "CarPlay" and a .phone attribute
#      - play() returns "CarPlay: playing via iPhone 15", reusing MediaSource.play()
#        (so .playing becomes True)


# 2.2  Notification is an abstract base class. Write two subclasses:
#      - LowFuelWarning(km_left): level "WARNING", message "Low fuel: 42 km left"
#      - IncomingCall(caller):    level "INFO",    message "Call from Alex"
#      render() must work for both without being overridden.
class Notification(ABC):
    level = "INFO"

    @abstractmethod
    def message(self) -> str: ...

    def render(self) -> str:
        return f"[{self.level}] {self.message()}"
