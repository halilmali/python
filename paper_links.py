"""
Resolve course question references (e.g. "Nov 2021 P41 Q1(a)", "J22/42 Q1(c)",
"June 2023 Paper 42") to exact pages of the original question paper / mark scheme
PDFs, and copy the referenced PDFs into the site.

Page finding works on the pdftotext -layout extracts in ..\\paper4-extract
(one file per paper, pages separated by form feeds); any missing extract is
generated on the fly. Browsers honor "#page=N" fragments on PDF links.

Used by build_site.py; running it directly prints a coverage report.
"""

import re
import shutil
import subprocess
from pathlib import Path

COURSE = Path(__file__).parent
PAPERS_ROOT = COURSE.parent / "9626-topical-questions"
EXTRACT = COURSE.parent / "paper4-extract"

# ------------------------------------------------------------ file map

def paper_files():
    """(series, year, variant) -> {qp: Path, ms: Path} for every Paper 4 PDF."""
    out = {}
    if not PAPERS_ROOT.exists():
        return out
    for f in PAPERS_ROOT.rglob("*.pdf"):
        m = re.search(r"9618 Computer Science (June|November) 20(\d{2}) "
                      r"(Question [Pp]aper|Mark Scheme)\s+(\d\d)\.pdf$", f.name)
        if not m or not m.group(4).startswith("4"):
            continue
        key = (m.group(1), 2000 + int(m.group(2)), m.group(4))
        out.setdefault(key, {})[
            "qp" if m.group(3).lower().startswith("question") else "ms"] = f
    return out


def extract_pages(series, year, variant, kind, files):
    """Pages (list[str]) of the question paper ('qp') or mark scheme ('ms')."""
    slug = f"{series} {year} {kind.upper()} {variant}.txt"
    txt = EXTRACT / slug
    if not txt.exists():
        src = files.get(kind)
        if src is None:
            return []
        EXTRACT.mkdir(exist_ok=True)
        subprocess.run(["pdftotext", "-layout", str(src), str(txt)], check=True)
    try:
        text = txt.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = txt.read_bytes().decode("latin-1")
    return text.split("\f")

# ------------------------------------------------------------ page finders

def qp_question_page(pages, q):
    """1-based PDF page on which question <q> starts in the question paper."""
    # [ \t] so a bare page-number footer line cannot match across the newline
    pat = re.compile(rf"^\s*{q}[ \t]+[A-Z]", re.M)
    for i, page in enumerate(pages[1:], start=2):          # skip the cover
        if pat.search(page):
            return i
    return None


def qp_part_page(pages, q, part, q_page):
    """1-based page of a main part letter inside the question's page range."""
    ends = [qp_question_page(pages, n) for n in range(q + 1, 4)]
    end = min((b for b in ends if b), default=len(pages) + 1)
    pat = re.compile(rf"^\s*\({part}\)[ \t]", re.M)
    for i in range(q_page, end):
        if pat.search(pages[i - 1]):
            return i
    return q_page


def ms_question_page(pages, q):
    """1-based page where the mark scheme for question <q> starts."""
    pat = re.compile(rf"^\s*{q}\([a-z]", re.M)
    for i, page in enumerate(pages[2:], start=3):          # skip cover + principles
        if pat.search(page):
            return i
    return None


def ms_part_page(pages, q, part, q_start):
    """1-based page containing the scheme rows for a specific part."""
    if part and part != "a":
        pat = re.compile(rf"^\s*{q}\({part}\)", re.M)
        for i, page in enumerate(pages[2:], start=3):
            if pat.search(page):
                return i
    return q_start

# ------------------------------------------------------------ references

# "Jun 2022 P42 Q1(c)" / "June 2022 Paper 42 Q1" / "June 2023 P42" (whole paper)
REF_A = re.compile(
    r"\b(Jun|Nov|June|November) 20(\d{2}) (?:P|Paper )4([123])"
    r"(?: Q(\d)((?:\([a-z]\))*)?)?", re.I)
# "J22/42 Q1(c)" / "J21/41" (also matches the first variant of "J21/41·42·43")
REF_B = re.compile(
    r"\b(J|N)(\d{2})/4([123])(?: Q(\d)((?:\([a-z]\))*)?)?")


def parse_a(m):
    mon = {"Jun": "June", "Nov": "November"}.get(m.group(1), m.group(1))
    return (mon, 2000 + int(m.group(2)), "4" + m.group(3),
            int(m.group(4)) if m.group(4) else None,
            _first_part(m.group(5)))


def parse_b(m):
    mon = "June" if m.group(1) == "J" else "November"
    return (mon, 2000 + int(m.group(2)), "4" + m.group(3),
            int(m.group(4)) if m.group(4) else None,
            _first_part(m.group(5)))


def _first_part(parts):
    if parts:
        m = re.search(r"\(([a-z])\)", parts)
        if m:
            return m.group(1)
    return None


class Resolver:
    def __init__(self):
        self.files = paper_files()
        self._pages = {}
        self.copied = set()
        self.site_papers = COURSE / "site" / "files" / "papers"
        self.report = {"resolved": 0, "unresolved": []}

    def pages(self, mon, year, var, kind):
        key = (mon, year, var, kind)
        if key not in self._pages:
            files = self.files.get((mon, year, var), {})
            self._pages[key] = extract_pages(mon, year, var, kind, files)
        return self._pages[key]

    def resolve(self, mon, year, var, q, part):
        """-> dict(qp_page, ms_page, qp_href, ms_href) or None."""
        entry = self.files.get((mon, year, var))
        if not entry or "qp" not in entry or "ms" not in entry:
            return None
        yy = str(year)[2:]
        session = f"{mon[0]}{yy}-P{var}"             # e.g. "J22-P42"
        if q is None:
            qp_page = ms_page = 1
        else:
            qp_pages = self.pages(mon, year, var, "qp")
            ms_pages = self.pages(mon, year, var, "ms")
            qp_page = qp_question_page(qp_pages, q)
            ms_page = ms_question_page(ms_pages, q)
            if qp_page is None or ms_page is None:
                return None
            if part:
                qp_page = qp_part_page(qp_pages, q, part, qp_page)
                ms_page = ms_part_page(ms_pages, q, part, ms_page)
        for kind, page in (("QP", qp_page), ("MS", ms_page)):
            dest = self.site_papers / f"{session}-{kind}.pdf"
            if (mon, year, var) not in self.copied:
                self.site_papers.mkdir(parents=True, exist_ok=True)
                shutil.copy2(entry[kind.lower()], dest)
        self.copied.add((mon, year, var))
        return {"qp_page": qp_page, "ms_page": ms_page, "session": session,
                "qp_href": f"files/papers/{session}-QP.pdf#page={qp_page}",
                "ms_href": f"files/papers/{session}-MS.pdf#page={ms_page}"}

    def make_link(self, parsed, text):
        mon, year, var, q, part = parsed
        r = self.resolve(mon, year, var, q, part)
        if r is None:
            self.report["unresolved"].append(text)
            return text
        self.report["resolved"] += 1
        qp_link = (f'<a class="qref" href="{r["qp_href"]}" '
                   f'title="Open the question paper at page {r["qp_page"]}">{text}</a>')
        ms_link = (f'<a class="msref" href="{r["ms_href"]}" '
                   f'title="Open the mark scheme at page {r["ms_page"]}">'
                   f'MS&nbsp;p.{r["ms_page"]}</a>')
        return f'{qp_link} <span class="mswrap">{ms_link}</span>'

# ---------------------------------------------------------------- linkify

def linkify(html, resolver):
    """Replace recognized references in `html` (outside <pre>) with PDF links."""
    parts = re.split(r"(<pre>.*?</pre>)", html, flags=re.S)
    for i, seg in enumerate(parts):
        if seg.startswith("<pre>"):
            continue
        seg = REF_A.sub(lambda m: resolver.make_link(parse_a(m), m.group(0)), seg)
        seg = REF_B.sub(lambda m: resolver.make_link(parse_b(m), m.group(0)), seg)
        parts[i] = seg
    return "".join(parts)

# ------------------------------------------------------------ report mode

def main():
    import markdown as md_lib
    resolver = Resolver()
    md_files = sorted(COURSE.glob("0*-*/README.md")) + [
        COURSE / "README.md", COURSE / "question-bank.md", COURSE / "teacher-guide.md"]
    for f in md_files:
        body = md_lib.markdown(f.read_text(encoding="utf-8"),
                               extensions=["tables", "fenced_code"])
        linkify(body, resolver)
    print("resolved refs:", resolver.report["resolved"])
    print("unresolved:", resolver.report["unresolved"] or "none")
    missing = [k for k, v in resolver.files.items() if "qp" not in v or "ms" not in v]
    print("papers known:", len(resolver.files), "| missing qp/ms:", missing or "none")
    print("pdfs copied so far:", len(resolver.copied))


if __name__ == "__main__":
    main()
