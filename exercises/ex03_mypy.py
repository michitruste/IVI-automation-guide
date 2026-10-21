"""Exercise 03: type hints and mypy.

3.1  Add type hints to every function so this passes with no errors:
         mypy --strict exercises/ex03_mypy.py
     No `Any` and no `# type: ignore`.
3.2  Fix the bugs. mypy finds one of them once the hints are in; the tests find the other.

Check your work:  pytest exercises/test_ex03_mypy.py -v
"""


def average_temp(readings):
    return sum(readings) / len(readings)


def find_station(stations, name):
    for freq, station in stations.items():
        if station == name:
            return freq
    return None


def station_label(stations, name):
    freq = find_station(stations, name)
    return f"{freq} FM"                 # should be "No signal" when the station isn't found


def parse_volume(text):
    if not text.isdigit():
        return "invalid"                # callers expect an int, or a ValueError
    return int(text)
