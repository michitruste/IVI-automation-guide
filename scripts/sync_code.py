"""Copy repo files into index.html so the code on the page always matches the repo.

Every <figure class="code" data-src="some/file.py"> gets its <code> body replaced with that file.

    python scripts/sync_code.py           rewrite index.html
    python scripts/sync_code.py --check   exit 1 if the page is out of date
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"


def fill(page: str, root: Path, attr: str = "data-src") -> str:
    figure = re.compile(
        rf'(<figure class="code" {attr}="([^"]+)">.*?<code data-lang="[^"]*">)(.*?)(</code>)',
        re.S,
    )

    def replace(m: re.Match[str]) -> str:
        text = (root / m.group(2)).read_text(encoding="utf-8").rstrip("\n")
        return m.group(1) + html.escape(text, quote=False) + m.group(4)

    return figure.sub(replace, page)


def main() -> int:
    page = PAGE.read_text(encoding="utf-8")
    synced = fill(page, ROOT)
    if "--check" in sys.argv:
        if synced != page:
            print("index.html is out of date: run python scripts/sync_code.py")
            return 1
        print("index.html matches the repo")
        return 0
    PAGE.write_text(synced, encoding="utf-8", newline="\n")
    print("index.html updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
