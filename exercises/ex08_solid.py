"""Exercise 08: refactor this class with SOLID in mind.

TripReport has three jobs and is hard to test:
  * it creates its own SmtpMailer (try sending: it raises ConnectionError)
  * adding a new format means editing the if/elif chain in build()

8.1  Name the principles that are broken (write them in a comment).
8.2  Refactor to this design so the tests in test_ex08_solid.py pass:
       * a Formatter Protocol with  format(self, km: float, litres: float, l_per_100km: float) -> str
       * CsvFormatter and JsonFormatter classes that produce the same text build() does now
       * a Mailer Protocol with  send(self, to: str, body: str) -> None
       * TripReport(formatter, mailer) with
             build(km, litres) -> str      and      send(to, km, litres) -> None
     The tests add an XML formatter without touching this file. That's the point.
"""
import json


class SmtpMailer:
    def send(self, to: str, body: str) -> None:
        raise ConnectionError("no SMTP server on this machine")


class TripReport:
    def __init__(self) -> None:
        self.mailer = SmtpMailer()

    def build(self, km: float, litres: float, fmt: str) -> str:
        l_per_100km = round(litres / km * 100, 1)
        if fmt == "csv":
            return f"km,litres,l_per_100km\n{km},{litres},{l_per_100km}"
        elif fmt == "json":
            return json.dumps({"km": km, "litres": litres, "l_per_100km": l_per_100km})
        raise ValueError(f"unknown format {fmt}")

    def send(self, to: str, km: float, litres: float, fmt: str) -> None:
        self.mailer.send(to, self.build(km, litres, fmt))
