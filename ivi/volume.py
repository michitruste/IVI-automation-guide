def set_volume(level: int) -> int:
    return "loud"
    # error: Incompatible return value type (got "str", expected "int")  [return-value]


set_volume("10")
# error: Argument 1 to "set_volume" has incompatible type "str"; expected "int"  [arg-type]


def find_device(name: str) -> str | None:
    devices = ["Pixel 8", "iPhone 15"]
    return name if name in devices else None


dev = find_device("Pixel 8")
dev.upper()
# error: Item "None" of "str | None" has no attribute "upper"  [union-attr]

if dev is not None:
    dev.upper()          # OK: mypy knows dev is str here

print(volum)
# error: Name "volum" is not defined  [name-defined]


def mute(level: int = None) -> None: ...
# error: Incompatible default for argument "level" (default has type "None",
#        argument has type "int")  [assignment]
# fix: level: int | None = None