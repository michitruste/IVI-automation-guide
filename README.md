# IVI Automation Guide

A hands-on guide to Python test automation, taught with one small simulated car infotainment (IVI) system.

**Read it here: https://michitruste.github.io/IVI-automation-guide/**

Each topic has notes, real code from this repo, common mistakes, exercises with tests and solutions, and a short quiz. Progress is saved in your browser.

| # | Topic | Level |
|---|---|---|
| 00 | Setup & project tour | |
| 01 | Python classes & OOP | Beginner |
| 02 | Inheritance & polymorphism | Beginner |
| 03 | Type hints + mypy | Beginner |
| 04 | Ruff + PEP 8 | Beginner |
| 05 | Pytest basics | Intermediate |
| 06 | Fixtures | Intermediate |
| 07 | Parametrized tests | Intermediate |
| 08 | SOLID principles | Intermediate |
| 09 | Mocking with unittest.mock | Advanced |
| 10 | BDD with Gherkin and Behave | Advanced |

## Setup

Python 3.11 or newer.

```bash
git clone https://github.com/michitruste/IVI-automation-guide.git
cd IVI-automation-guide
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

Check that everything works:

```bash
pytest          # example tests in tests/
mypy ivi/       # type-check the example package
ruff check .    # lint
behave          # BDD scenarios in features/
```

## Layout

- `ivi/` – the code under test: a simulated head unit (radio, media sources, player, HVAC, Bluetooth)
- `tests/` – pytest examples
- `features/` – Behave feature file, step definitions and hooks
- `examples/` – deliberately broken code for the mypy and Ruff topics
- `exercises/` – a starter file and a test file per topic
- `index.html` – the guide itself (served by GitHub Pages)

## Exercises

Every topic has an exercise file in `exercises/` and tests that fail until you finish it:

```bash
pytest exercises/test_ex01_classes.py -v
behave exercises/features              # topic 10
```

Plain `pytest` only runs `tests/`, so unfinished exercises don't break the main suite. Hints and solutions are on the page.

## Editing the guide

The code blocks in `index.html` marked `data-src="path"` are copied from the repo files. After changing a file under `ivi/`, `tests/`, `features/`, `examples/` or `exercises/`, run:

```bash
python scripts/sync_code.py           # update the page
python scripts/sync_code.py --check   # fail if the page is out of date
```
