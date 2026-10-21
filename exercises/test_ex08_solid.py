import json

from exercises import ex08_solid as ex


class FakeMailer:
    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, to: str, body: str) -> None:
        self.sent.append((to, body))


class XmlFormatter:                       # a new format, added without editing ex08_solid.py
    def format(self, km: float, litres: float, l_per_100km: float) -> str:
        return f"<trip km='{km}' litres='{litres}' l_per_100km='{l_per_100km}'/>"


def test_csv():
    report = ex.TripReport(ex.CsvFormatter(), FakeMailer())
    assert report.build(200, 12) == "km,litres,l_per_100km\n200,12,6.0"


def test_json():
    report = ex.TripReport(ex.JsonFormatter(), FakeMailer())
    assert json.loads(report.build(200, 12)) == {"km": 200, "litres": 12, "l_per_100km": 6.0}


def test_new_format_without_editing_the_module():
    report = ex.TripReport(XmlFormatter(), FakeMailer())
    assert report.build(100, 5) == "<trip km='100' litres='5' l_per_100km='5.0'/>"


def test_send_uses_injected_mailer():
    mailer = FakeMailer()
    ex.TripReport(ex.CsvFormatter(), mailer).send("fleet@example.com", 200, 12)
    assert mailer.sent == [("fleet@example.com", "km,litres,l_per_100km\n200,12,6.0")]
