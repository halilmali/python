"""
Build the 9618 Paper 4 Python course as a self-contained static website.

Reads the markdown course + solutions + data files from this folder and writes
a fully offline-capable site to ./site (sidebar nav, client-side search,
checkpoint progress in localStorage, code highlighting with copy buttons,
solution viewer, light/dark themes). Works from file:// or any static server.

Run:  python build_site.py
"""

import hashlib
import html as html_mod
import re
import shutil
import sys
from pathlib import Path

import markdown
import paper_links
from pygments import highlight as pyg_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer, get_lexer_by_name

ROOT = Path(__file__).parent
SITE = ROOT / "site"
MD_EXT = ["tables", "fenced_code", "sane_lists", "attr_list"]

# ---------------------------------------------------------------- page plan

# (page_id, sidebar label, source path or None for generated, title)
PAGES = [
    ("index", "Home", "README.md", "Python for Cambridge 9618 Paper 4"),
    ("cheatsheet", "Pseudocode → Python cheatsheet", "pseudocode-cheatsheet.md",
     "Cambridge Pseudocode → Python 3 Cheatsheet"),
    ("module-00", "0 · Exam orientation", "00-exam-orientation/README.md",
     "Module 0 — How Paper 4 works"),
    ("module-01", "1 · Python foundations", "01-python-foundations/README.md",
     "Module 1 — Pseudocode → Python foundations"),
    ("module-02", "2 · Modular programming", "02-modular-programming/README.md",
     "Module 2 — Procedures, functions, parameters and globals"),
    ("module-03", "3 · Arrays & records", "03-arrays-and-records/README.md",
     "Module 3 — 1D arrays, 2D arrays, parallel arrays and records"),
    ("module-04", "4 · Strings & validation", "04-strings-and-validation/README.md",
     "Module 4 — String processing and input validation"),
    ("module-05", "5 · Files & exceptions", "05-files-and-exceptions/README.md",
     "Module 5 — File handling and exception handling"),
    ("module-06", "6 · OOP foundations", "06-oop-foundations/README.md",
     "Module 6 — OOP foundations: classes, constructors, getters, setters"),
    ("module-07", "7 · OOP advanced", "07-oop-inheritance/README.md",
     "Module 7 — OOP advanced: composition, inheritance, overriding"),
    ("module-08", "8 · Stacks & queues", "08-stacks-and-queues/README.md",
     "Module 8 — Stacks and queues (array-based ADTs)"),
    ("module-09", "9 · Lists, trees, hashes", "09-lists-trees-hashes/README.md",
     "Module 9 — Linked lists, binary trees, hash tables"),
    ("module-10", "10 · Searching & sorting", "10-searching-and-sorting/README.md",
     "Module 10 — Searching and sorting (no builtins allowed)"),
    ("module-11", "11 · Recursion", "11-recursion/README.md",
     "Module 11 — Recursion: trace, translate, convert"),
    ("module-12", "12 · Exam technique", "12-exam-technique/README.md",
     "Module 12 — Exam technique: the 150-minute protocol"),
    ("question-bank", "Question bank", "question-bank.md",
     "9618 Paper 4 — Master Question Bank (2021–2026)"),
    ("teacher-guide", "Teacher guide", "teacher-guide.md",
     "Teacher Guide — Running the 9618 Paper 4 Python Course"),
    ("solutions", "Solutions", None,
     "Model Solutions — index"),
]

# ----------------------------------------------------------- link rewriting

def rewrite_href(href: str) -> str:
    """Map a markdown-source link target to its site URL."""
    if re.match(r"^(https?:|mailto:|#|files/)", href):
        return href
    clean = href.split("#")[0].replace("\\", "/").rstrip("/")
    anchor = href[len(href.split("#")[0]):] if "#" in href else ""
    name = clean
    if name.endswith("/README.md") and re.match(r"^\d\d-", name):
        return "module-" + name[:2] + ".html" + anchor
    mapping = {
        "README.md": "index.html",
        "pseudocode-cheatsheet.md": "cheatsheet.html",
        "question-bank.md": "question-bank.html",
        "teacher-guide.md": "teacher-guide.html",
        "solutions": "solutions.html",
        "data-files": "solutions.html",
    }
    if name in mapping:
        return mapping[name] + anchor
    if name.startswith("solutions/") and name.endswith(".py"):
        return name[:-3] + ".html" + anchor
    if name.startswith("data-files/"):
        return "files/" + name + anchor
    return href


def rewrite_links(page_html: str) -> str:
    return re.sub(r'href="([^"]+)"',
                  lambda m: 'href="%s"' % rewrite_href(m.group(1)), page_html)


def linkify_code(page_html: str) -> str:
    """Make <code>solutions/x.py</code> and <code>data-files/...</code> clickable."""
    def sub_solutions(m):
        path = m.group(1)
        return '<a href="%s.html"><code>%s</code></a>' % (path[:-3], path)
    page_html = re.sub(r"<code>(solutions/[A-Za-z0-9_./-]+\.py)</code>", sub_solutions,
                       page_html)
    page_html = re.sub(
        r"<code>(data-files/[A-Za-z0-9_./-]+)</code>",
        r'<a href="files/\1"><code>\1</code></a>', page_html)
    return page_html

# ------------------------------------------------------- markdown post-fixes

def postprocess(page_id: str, html: str) -> str:
    # task-list checkboxes -> interactive checkpoints
    def sub_ckpt(m):
        text = m.group(1)
        plain = re.sub(r"<[^>]+>", "", text)
        cid = hashlib.sha1((page_id + "::" + plain).encode()).hexdigest()[:12]
        return ('<li class="checkpoint"><label><input type="checkbox" '
                'data-ckpt="%s"><span>%s</span></label></li>' % (cid, text))
    html = re.sub(r"<li>\[ \] (.*?)</li>", sub_ckpt, html)
    html = re.sub(r"<li>\[x\] ", "<li class=\"checkpoint done\"><label><input "
                  "type=\"checkbox\" checked disabled><span>", html)
    html = re.sub(r"(</li>\s*)?(?=<li class=\"checkpoint done)", "", html)
    # scrollable tables
    html = html.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>")
    html = html.replace("<table>", "<table>")  # no-op; clarity
    return html


def md_to_html(page_id: str, src: str) -> str:
    body = markdown.markdown(src, extensions=MD_EXT)
    body = postprocess(page_id, body)
    body = linkify_code(body)
    body = rewrite_links(body)
    return body

# ------------------------------------------------------------------ assets

CSS = r"""
:root {
  --bg: #f6f7fb; --surface: #ffffff; --surface2: #eef0f7;
  --text: #1c2333; --muted: #5b6478; --border: #dde1ee;
  --accent: #2757d6; --accent-soft: #e7edfd; --accent2: #b7791f;
  --ok: #1c7c4c; --ok-soft: #e2f4ea;
  --shadow: 0 1px 3px rgba(20, 30, 60, .08), 0 8px 24px rgba(20, 30, 60, .06);
  --code-bg: #f0f2f8; --mono: ui-monospace, "Cascadia Code", Consolas, Menlo, monospace;
}
[data-theme="dark"] {
  --bg: #12151d; --surface: #1a1f2b; --surface2: #212836;
  --text: #e4e8f2; --muted: #9aa3b8; --border: #2c3446;
  --accent: #7da2ff; --accent-soft: #1d2a4a; --accent2: #e0b45f;
  --ok: #5bd398; --ok-soft: #17352a;
  --shadow: 0 1px 3px rgba(0, 0, 0, .4), 0 8px 24px rgba(0, 0, 0, .3);
  --code-bg: #141926;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.65 -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
.layout { display: flex; min-height: 100vh; }

/* ---------------- sidebar ---------------- */
.sidebar {
  width: 288px; flex: 0 0 288px; background: var(--surface);
  border-right: 1px solid var(--border); padding: 20px 16px;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
}
.brand { display: block; padding: 4px 10px 14px; text-decoration: none; }
.brand .t1 { font-weight: 800; font-size: 17px; color: var(--text); line-height: 1.25; }
.brand .t2 { font-size: 12.5px; color: var(--muted); margin-top: 3px; }
.navgroup { margin: 14px 0 4px; padding: 0 10px; font-size: 11px; font-weight: 700;
  letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }
.sidebar a.navlink {
  display: flex; justify-content: space-between; align-items: center; gap: 8px;
  padding: 7px 10px; margin: 1px 0; border-radius: 8px;
  color: var(--text); text-decoration: none; font-size: 14px;
}
.sidebar a.navlink:hover { background: var(--surface2); }
.sidebar a.navlink.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.navprog { font-size: 10.5px; color: var(--muted); font-variant-numeric: tabular-nums; }
.overall { margin: 10px 10px 4px; }
.overall .bar { height: 6px; border-radius: 4px; background: var(--surface2); overflow: hidden; }
.overall .fill { height: 100%; background: var(--ok); width: 0%; transition: width .3s; }
.overall .lbl { font-size: 11.5px; color: var(--muted); margin-bottom: 4px; }

/* ---------------- main ---------------- */
.main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.topbar {
  position: sticky; top: 0; z-index: 30; display: flex; align-items: center; gap: 12px;
  padding: 10px 22px; background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(8px); border-bottom: 1px solid var(--border);
}
.hamburger { display: none; background: none; border: 1px solid var(--border);
  border-radius: 8px; padding: 6px 10px; cursor: pointer; color: var(--text); font-size: 16px; }
.searchbox { position: relative; flex: 1; max-width: 460px; }
.searchbox input {
  width: 100%; padding: 8px 12px 8px 34px; border: 1px solid var(--border);
  border-radius: 10px; background: var(--surface); color: var(--text); font-size: 14px;
}
.searchbox input:focus { outline: 2px solid var(--accent); outline-offset: -1px; }
.searchbox .mag { position: absolute; left: 11px; top: 8px; color: var(--muted); font-size: 14px; }
.search-results {
  position: absolute; top: 42px; left: 0; right: 0; background: var(--surface);
  border: 1px solid var(--border); border-radius: 10px; box-shadow: var(--shadow);
  max-height: 60vh; overflow-y: auto; display: none; padding: 6px;
}
.search-results.open { display: block; }
.search-results a { display: block; padding: 8px 10px; border-radius: 8px;
  text-decoration: none; color: var(--text); }
.search-results a:hover, .search-results a.sel { background: var(--accent-soft); }
.search-results .rt { font-weight: 600; font-size: 14px; }
.search-results .rs { font-size: 12.5px; color: var(--muted);
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.search-results .none { padding: 10px; color: var(--muted); font-size: 14px; }
.topbar .spacer { flex: 1; }
.tbtn { background: var(--surface); border: 1px solid var(--border); color: var(--text);
  border-radius: 10px; padding: 7px 12px; cursor: pointer; font-size: 13.5px; }
.tbtn:hover { border-color: var(--accent); }

.content { max-width: 920px; width: 100%; margin: 0 auto; padding: 30px 26px 80px; }
.crumbs { font-size: 12.5px; color: var(--muted); margin-bottom: 6px; }
.crumbs a { color: var(--accent); text-decoration: none; }
h1 { font-size: 30px; line-height: 1.25; margin: 4px 0 8px; letter-spacing: -.01em; }
h2 { font-size: 22px; margin: 34px 0 10px; padding-top: 14px; letter-spacing: -.01em; }
h3 { font-size: 17.5px; margin: 26px 0 8px; }
p, li { color: var(--text); }
a { color: var(--accent); }
a.textlink { color: var(--accent); text-decoration: none; }
a.textlink:hover { text-decoration: underline; }
hr { border: 0; border-top: 1px solid var(--border); margin: 30px 0; }
code {
  font-family: var(--mono); font-size: .88em; background: var(--code-bg);
  padding: .15em .4em; border-radius: 6px; border: 1px solid var(--border);
}
pre { margin: 0; }
.codeblock { margin: 16px 0; border: 1px solid var(--border); border-radius: 12px;
  overflow: hidden; background: var(--code-bg); box-shadow: var(--shadow); }
.codeblock .cbhead { display: flex; justify-content: space-between; align-items: center;
  padding: 6px 12px; background: var(--surface2); border-bottom: 1px solid var(--border);
  font-size: 11.5px; color: var(--muted); font-family: var(--mono); }
.codeblock .copy { background: none; border: 1px solid var(--border); color: var(--muted);
  border-radius: 6px; font-size: 11px; padding: 2px 8px; cursor: pointer; }
.codeblock .copy:hover { color: var(--accent); border-color: var(--accent); }
.codeblock .codehilite { padding: 12px 14px; overflow-x: auto; background: transparent; }
.codeblock pre { margin: 0; font-family: var(--mono); font-size: 13.2px; line-height: 1.55; }
.codehilite { border-radius: 0; }

/* tables */
.table-wrap { overflow-x: auto; margin: 16px 0; border: 1px solid var(--border);
  border-radius: 12px; box-shadow: var(--shadow); }
table { border-collapse: collapse; width: 100%; font-size: 14px; background: var(--surface); }
th, td { text-align: left; padding: 9px 12px; border-bottom: 1px solid var(--border);
  vertical-align: top; }
th { background: var(--surface2); font-size: 12.5px; letter-spacing: .03em;
  text-transform: uppercase; color: var(--muted); }
tr:last-child td { border-bottom: 0; }

/* checkpoints */
ul { padding-left: 24px; }
li.checkpoint { list-style: none; margin: 4px 0; }
li.checkpoint label { display: flex; gap: 9px; align-items: baseline; cursor: pointer; }
li.checkpoint input { accent-color: var(--ok); transform: translateY(2px); }
li.checkpoint input:checked + span { color: var(--muted); text-decoration: line-through;
  text-decoration-color: var(--ok); }
.progresswrap { margin: 18px 0; padding: 12px 16px; background: var(--surface);
  border: 1px solid var(--border); border-radius: 12px; box-shadow: var(--shadow); }
.progresswrap .bar { height: 8px; border-radius: 6px; background: var(--surface2); overflow: hidden; }
.progresswrap .fill { height: 100%; background: var(--ok); width: 0%; transition: width .3s; }
.progresswrap .lbl { font-size: 13px; color: var(--muted); margin-bottom: 6px; }

/* pager */
.pager { display: flex; justify-content: space-between; gap: 14px; margin-top: 44px; }
.pager a { flex: 1; text-decoration: none; border: 1px solid var(--border); background: var(--surface);
  padding: 12px 16px; border-radius: 12px; box-shadow: var(--shadow); }
.pager a:hover { border-color: var(--accent); }
.pager .dir { font-size: 11.5px; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
.pager .pt { font-weight: 600; color: var(--text); font-size: 14.5px; }
.pager .next { text-align: right; }

/* question reference links */
.qref { text-decoration: none; }
.qref:hover { text-decoration: underline; }
.mswrap { margin-left: 6px; white-space: nowrap; }
.msref {
  color: var(--accent2); border: 1px solid var(--border); border-radius: 6px;
  padding: 1px 6px; font-size: .82em; text-decoration: none;
  background: var(--surface);
}
.msref:hover { border-color: var(--accent2); text-decoration: none; }

/* solution index cards */
.solgrid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; margin: 18px 0; }
.solcard { border: 1px solid var(--border); background: var(--surface); border-radius: 12px;
  padding: 14px 16px; box-shadow: var(--shadow); }
.solcard .fn { font-family: var(--mono); font-size: 13px; color: var(--accent); font-weight: 600; }
.solcard .desc { font-size: 13.5px; color: var(--muted); margin: 6px 0 8px; }
.solcard a.runlink { font-size: 12.5px; text-decoration: none; }

@media (max-width: 960px) {
  .sidebar { position: fixed; left: 0; top: 0; bottom: 0; z-index: 50;
    transform: translateX(-105%); transition: transform .25s; box-shadow: var(--shadow); }
  body.nav-open .sidebar { transform: none; }
  .hamburger { display: block; }
  .content { padding: 22px 16px 70px; }
  h1 { font-size: 25px; }
}
@media print {
  .sidebar, .topbar, .pager, .tbtn, .copy { display: none !important; }
  body { background: #fff; }
  .content { max-width: none; }
}
"""

PYG_LIGHT = "friendly"
PYG_DARK = "monokai"


def pygments_css() -> str:
    light = HtmlFormatter(style=PYG_LIGHT).get_style_defs(".codehilite")
    dark = HtmlFormatter(style=PYG_DARK).get_style_defs(".codehilite")
    dark = dark.replace(".codehilite", '[data-theme="dark"] .codehilite')
    return light + "\n" + dark + "\n"


APP_JS = r"""
(function () {
  "use strict";
  var body = document.body;

  /* ---------- safe storage (localStorage can be blocked on file:// or embedded) ---------- */
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- theme ---------- */
  var themeBtn = document.getElementById("themeBtn");
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    store.set("p4-theme", t);
    if (themeBtn) themeBtn.textContent = t === "dark" ? "Light" : "Dark";
  }
  var saved = store.get("p4-theme");
  if (saved) applyTheme(saved);
  else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches)
    applyTheme("dark");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  /* ---------- mobile nav ---------- */
  var burger = document.getElementById("hamburger");
  if (burger) burger.addEventListener("click", function () {
    body.classList.toggle("nav-open");
  });

  /* ---------- checkpoints & progress ---------- */
  var ALL = window.P4_CHECKPOINTS || {};
  var ids = Object.keys(ALL);
  function checkedCount() {
    var n = 0;
    for (var i = 0; i < ids.length; i++)
      if (store.get("p4-ck-" + ids[i]) === "1") n++;
    return n;
  }
  function paintOverall() {
    var total = ids.length;
    var done = checkedCount();
    var pct = total ? Math.round(100 * done / total) : 0;
    document.querySelectorAll(".js-overall-fill").forEach(function (el) {
      el.style.width = pct + "%";
    });
    document.querySelectorAll(".js-overall-lbl").forEach(function (el) {
      el.textContent = done + " / " + total + " checkpoints (" + pct + "%)";
    });
  }
  var boxes = Array.prototype.slice.call(document.querySelectorAll("input[data-ckpt]"));
  boxes.forEach(function (box) {
    var id = box.getAttribute("data-ckpt");
    box.checked = store.get("p4-ck-" + id) === "1";
    box.addEventListener("change", function () {
      store.set("p4-ck-" + id, box.checked ? "1" : "0");
      paintOverall(); paintPage();
    });
  });
  function paintPage() {
    if (!boxes.length) {
      var w = document.querySelector(".progresswrap");
      if (w) w.style.display = "none";
      return;
    }
    var done = boxes.filter(function (b) { return b.checked; }).length;
    var pct = Math.round(100 * done / boxes.length);
    var fill = document.querySelector(".progresswrap .fill");
    var lbl = document.querySelector(".progresswrap .lbl");
    if (fill) fill.style.width = pct + "%";
    if (lbl) lbl.textContent = "Module checkpoints: " + done + " / " + boxes.length +
      " (" + pct + "%)";
  }
  paintOverall(); paintPage();

  /* ---------- copy buttons ---------- */
  function copyText(text, btn) {
    function done(ok) {
      var old = btn.textContent;
      btn.textContent = ok ? "Copied!" : "Select & copy";
      setTimeout(function () { btn.textContent = old; }, 1400);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { done(true); },
        function () { fallback(); });
    } else fallback();
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta); done(ok);
    }
  }
  document.querySelectorAll(".codeblock .copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var pre = btn.closest(".codeblock").querySelector("pre");
      copyText(pre.innerText, btn);
    });
  });

  /* ---------- search ---------- */
  var idx = window.P4_SEARCH || [];
  var input = document.getElementById("searchInput");
  var box = document.getElementById("searchResults");
  var items = [], sel = -1;
  function snippet(text, q) {
    var lower = text.toLowerCase(), qi = lower.indexOf(q);
    if (qi < 0) return text.slice(0, 90);
    var start = Math.max(0, qi - 34);
    return (start > 0 ? "\u2026" : "") + text.slice(start, qi + 60) + "\u2026";
  }
  function runSearch(q) {
    q = q.trim().toLowerCase();
    if (q.length < 2) { box.classList.remove("open"); box.innerHTML = ""; return; }
    var scored = [];
    for (var i = 0; i < idx.length; i++) {
      var it = idx[i];
      var t = it.t.toLowerCase(), x = it.x.toLowerCase();
      var score = -1;
      if (t.indexOf(q) === 0) score = 100;
      else if (t.indexOf(q) >= 0) score = 60;
      else {
        var count = 0, pos = 0;
        while ((pos = x.indexOf(q, pos)) >= 0 && count < 6) { count++; pos += q.length; }
        if (count) score = 10 + count;
      }
      if (score >= 0) scored.push({ s: score, t: it.t, u: it.u, x: it.x });
    }
    scored.sort(function (a, b) { return b.s - a.s; });
    var top = scored.slice(0, 12);
    if (!top.length) {
      box.innerHTML = '<div class="none">No results for "' +
        q.replace(/</g, "&lt;") + '"</div>';
    } else {
      box.innerHTML = top.map(function (r) {
        return '<a href="' + r.u + '"><div class="rt">' + r.t +
          '</div><div class="rs">' + snippet(r.x, q) + "</div></a>";
      }).join("");
    }
    box.classList.add("open"); sel = -1;
  }
  if (input && box) {
    input.addEventListener("input", function () { runSearch(input.value); });
    input.addEventListener("focus", function () { if (input.value.trim().length >= 2)
      box.classList.add("open"); });
    document.addEventListener("click", function (e) {
      if (!box.contains(e.target) && e.target !== input) box.classList.remove("open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && document.activeElement !== input) {
        e.preventDefault(); input.focus();
      } else if (e.key === "Escape") { box.classList.remove("open"); input.blur(); }
      else if (box.classList.contains("open") && (e.key === "ArrowDown" || e.key === "ArrowUp")) {
        e.preventDefault();
        var links = box.querySelectorAll("a");
        if (!links.length) return;
        sel = e.key === "ArrowDown" ? Math.min(sel + 1, links.length - 1)
                                    : Math.max(sel - 1, 0);
        links.forEach(function (l) { l.classList.remove("sel"); });
        links[sel].classList.add("sel"); links[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && sel >= 0) {
        var links2 = box.querySelectorAll("a");
        if (links2[sel]) links2[sel].click();
      }
    });
    // navigate on click then clear
    box.addEventListener("click", function () { box.classList.remove("open"); });
  }
})();
"""

# ----------------------------------------------------------------- builders

def make_codeblock(code_html: str, lang: str) -> str:
    head = lang if lang else "text"
    return ('<div class="codeblock"><div class="cbhead"><span>%s</span>'
            '<button class="copy" type="button">Copy</button></div>'
            '<div class="codehilite">%s</div></div>'
            % (head, code_html))


def highlight_fences(html: str) -> str:
    """Re-render fenced code via pygments, wrap in styled block with copy button."""
    def repl(m):
        lang, code = m.group(1) or "text", m.group(2)
        code = html_mod.unescape(code)
        try:
            lexer = PythonLexer() if lang in ("python", "py") else get_lexer_by_name(
                lang, stripall=False)
        except Exception:
            lexer = None
        if lang in ("text", "", "bash", "shell", "console"):
            inner = '<pre>%s</pre>' % html_mod.escape(code)
        elif lexer is None:
            inner = '<pre>%s</pre>' % html_mod.escape(code)
        else:
            fmt = HtmlFormatter(nowrap=True)
            inner = '<pre>%s</pre>' % pyg_highlight(code, lexer, fmt)
        return make_codeblock(inner, lang)
    # fenced blocks already converted by `fenced_code` into <div class="codehilite"><pre>...
    # easier: run on raw pattern produced by python-markdown
    pattern = re.compile(
        r'<pre>(?:<span></span>)?<code(?: class="language-([\w+-]+)")?>(.*?)</code></pre>',
        re.S)
    return pattern.sub(repl, html)


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = html_mod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def rebase_urls(page_html: str, base: str) -> str:
    """Prefix internal href/src with a base ('../' for pages inside subfolders)."""
    if not base:
        return page_html
    def sub(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|data:)", url):
            return m.group(0)
        return '%s="%s%s"' % (attr, base, url)
    return re.sub(r'(href|src)="([^"]+)"', sub, page_html)


def wrap_page(page_id: str, title: str, content_html: str, nav_links: str,
              crumb: str, prev_page, next_page, base: str = "") -> str:
    pager = ""
    if prev_page or next_page:
        prev_html = ('<a class="prev" href="%s"><div class="dir">\u2190 Previous</div>'
                     '<div class="pt">%s</div></a>' % prev_page[1:]) if prev_page else "<span></span>"
        next_html = ('<a class="next" href="%s"><div class="dir">Next \u2192</div>'
                     '<div class="pt">%s</div></a>' % next_page[1:]) if next_page else "<span></span>"
        pager = '<div class="pager">%s%s</div>' % (prev_html, next_html)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_mod.escape(title)} — 9618 Paper 4 Python Course</title>
<link rel="stylesheet" href="assets/style.css">
<script src="assets/checkpoints.js"></script>
<script src="assets/search-index.js"></script>
<script src="assets/app.js" defer></script>
</head>
<body>
<div class="layout">
  <aside class="sidebar" id="sidebar">
    <a class="brand" href="index.html">
      <div class="t1">Python for 9618 Paper 4</div>
      <div class="t2">A Level Computer Science · Practical exam course</div>
    </a>
    <div class="overall">
      <div class="lbl js-overall-lbl">0 / 0 checkpoints (0%)</div>
      <div class="bar"><div class="fill js-overall-fill"></div></div>
    </div>
    {nav_links}
  </aside>
  <div class="main">
    <div class="topbar">
      <button class="hamburger" id="hamburger" aria-label="Menu">\u2630</button>
      <div class="searchbox">
        <span class="mag">\U0001F50D</span>
        <input id="searchInput" type="search" placeholder="Search the course…  (press /)"
               autocomplete="off">
        <div class="search-results" id="searchResults"></div>
      </div>
      <div class="spacer"></div>
      <button class="tbtn" id="themeBtn" type="button">Dark</button>
    </div>
    <main class="content">
      <div class="crumbs">{crumb}</div>
      <div class="progresswrap">
        <div class="lbl">Module checkpoints</div>
        <div class="bar"><div class="fill"></div></div>
      </div>
      {content_html}
      {pager}
    </main>
  </div>
</div>
</body>
</html>
"""
    return rebase_urls(page, base)


def build_nav(current_id: str) -> str:
    groups = [("Start", ["index", "cheatsheet"]),
              ("Modules", ["module-%02d" % i for i in range(13)]),
              ("Reference", ["question-bank", "teacher-guide", "solutions"])]
    label_of = {p[0]: p[1] for p in PAGES}
    url_of = {p[0]: p[0] + ".html" for p in PAGES}
    out = []
    for gname, ids in groups:
        out.append('<div class="navgroup">%s</div>' % gname)
        for pid in ids:
            cls = "navlink active" if pid == current_id else "navlink"
            out.append('<a class="%s" href="%s"><span>%s</span></a>'
                       % (cls, url_of[pid], html_mod.escape(label_of[pid])))
    return "\n".join(out)


def pager_pair(page_id: str):
    ids = [p[0] for p in PAGES]
    i = ids.index(page_id)
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i < len(PAGES) - 1 else None
    return ((prev[0], prev[0] + ".html", prev[3]) if prev else None,
            (nxt[0], nxt[0] + ".html", nxt[3]) if nxt else None)


# --------------------------------------------------------- solution pages

def load_solutions():
    sol_dir = ROOT / "solutions"
    out = []
    for py in sorted(sol_dir.glob("m*.py")):
        text = py.read_text(encoding="utf-8")
        first = ""
        m = re.search(r'"""(.*?)"""', text, re.S)
        if m:
            lines = [l.strip() for l in m.group(1).strip().splitlines()]
            first = next((l for l in lines if l), "")
        module_no = int(re.match(r"m(\d+)", py.stem).group(1))
        out.append({"name": py.name, "stem": py.stem, "text": text,
                    "desc": first, "module": module_no})
    return out


def build_solution_page(sol, nav_links, prev_page, next_page):
    lexer = PythonLexer()
    code_html = '<pre>%s</pre>' % pyg_highlight(sol["text"], lexer, HtmlFormatter(nowrap=True))
    block = make_codeblock(code_html, "python")
    run_cmd = ""
    m = re.search(r"Run(?: with[^:]*| from the .solutions. folder)?:(.*)", sol["text"])
    if m:
        run_cmd = m.group(1).strip().lstrip(" ").rstrip("`")
    run_html = ""
    if run_cmd:
        run_html = ('<div class="codeblock"><div class="cbhead"><span>run</span></div>'
                    '<div class="codehilite"><pre>%s</pre></div></div>'
                    % html_mod.escape(run_cmd))
    content = f"""<h1>{html_mod.escape(sol['name'])}</h1>
<p><strong>Source question:</strong> {html_mod.escape(sol['desc'])}</p>
<p><a class="textlink" href="files/solutions/{sol['name']}">Download raw file \u2197</a></p>
{run_html}
{block}
<p><em>Work the question yourself from the original paper before reading this model
answer. Then diff your version against it mark-point by mark-point.</em></p>"""
    return wrap_page("solutions-" + sol["stem"], sol["name"], content, nav_links,
                     '<a href="solutions.html">Solutions</a> / ' + sol["name"],
                     prev_page, next_page, base="../")


# -------------------------------------------------------------------- main

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    (SITE / "files" / "solutions").mkdir(parents=True)
    (SITE / "files" / "data-files").mkdir(parents=True)

    solutions = load_solutions()

    # copy assets
    for py in solutions:
        shutil.copy2(ROOT / "solutions" / py["name"], SITE / "files" / "solutions" / py["name"])
    data_root = ROOT / "data-files"
    for f in data_root.rglob("*"):
        if f.is_file():
            rel = f.relative_to(data_root)
            dest = SITE / "files" / "data-files" / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)

    # checkpoints registry + search index
    checkpoints = {}
    search_index = []

    rendered = {}
    resolver = paper_links.Resolver()
    for pid, label, src, title in PAGES:
        if src is None:
            continue
        text = (ROOT / src).read_text(encoding="utf-8")
        body = highlight_fences(md_to_html(pid, text))
        body = paper_links.linkify(body, resolver)
        for cid in re.findall(r'data-ckpt="([0-9a-f]+)"', body):
            checkpoints[cid] = title
        rendered[pid] = body
    print("paper links: %d resolved, %d unresolved; %d papers copied" %
          (resolver.report["resolved"], len(resolver.report["unresolved"]),
           len(resolver.copied)))
    if resolver.report["unresolved"]:
        print("  unresolved refs:", resolver.report["unresolved"][:10])

    # nav links (shared; active class differs per page)
    nav_cache = {}

    # solution pages
    sol_pages = []
    for i, sol in enumerate(solutions):
        sol_pages.append(("solutions-" + sol["stem"], sol["name"], None, sol["name"]))

    # page order for pager: main pages then solutions
    order = PAGES + sol_pages

    # write main pages
    for pid, label, src, title in PAGES:
        if pid == "solutions":
            continue
        nav = build_nav(pid) if pid not in nav_cache else nav_cache[pid]
        prev, nxt = pager_pair(pid)
        crumb = "Course home" if pid == "index" else \
            '<a href="index.html">Course home</a> / ' + html_mod.escape(label)
        page = wrap_page(pid, title, rendered[pid], nav, crumb, prev, nxt)
        (SITE / (pid + ".html")).write_text(page, encoding="utf-8")
        search_index.append({"t": title, "u": pid + ".html",
                             "x": strip_tags(rendered[pid])[:24000]})

    # solutions index page (generated)
    groups = {}
    for sol in solutions:
        groups.setdefault(sol["module"], []).append(sol)
    sections = []
    for mod in sorted(groups):
        mod_title = dict((p[0], p[3]) for p in PAGES).get("module-%02d" % mod,
                                                         "Module %d" % mod)
        cards = "".join(
            '<div class="solcard"><div class="fn"><a href="solutions/%s.html">%s</a></div>'
            '<div class="desc">%s</div>'
            '<a class="runlink" href="solutions/%s.html">View highlighted code \u2192</a></div>'
            % (s["stem"], s["name"], html_mod.escape(s["desc"]), s["stem"])
            for s in groups[mod])
        sections.append("<h2>%s</h2><div class=\"solgrid\">%s</div>"
                        % (html_mod.escape(mod_title), cards))
    data_files = sorted((SITE / "files" / "data-files").rglob("*"))
    data_list = "".join('<a class="textlink" href="files/data-files/%s" style="display:block;'
                        'font-family:var(--mono);font-size:13px;padding:2px 0;">%s</a>'
                        % (f.relative_to(SITE / "files" / "data-files").as_posix(),
                           f.relative_to(SITE / "files" / "data-files").as_posix())
                        for f in data_files if f.is_file())
    intro = ("<p>Each solution answers a cited past-paper question and was verified to run "
             "against the paper's own test data. Attempt the question from the original PDF "
             "first — the model answer is for marking yourself against, mark point by mark "
             "point.</p><h2>Sample data files (recreated formats)</h2>" + data_list)
    sol_body = highlight_fences("<h1>Model Solutions</h1>" + intro + "".join(sections))
    nav = build_nav("solutions")
    prev, nxt = pager_pair("solutions")
    (SITE / "solutions.html").write_text(
        wrap_page("solutions", "Model Solutions — index", sol_body, nav,
                  '<a href="index.html">Course home</a> / Solutions', prev, nxt),
        encoding="utf-8")
    search_index.append({"t": "Model Solutions — index", "u": "solutions.html",
                         "x": strip_tags(sol_body)[:24000]})

    # individual solution pages
    for i, sol in enumerate(solutions):
        pid = "solutions-" + sol["stem"]
        nav = build_nav(pid)
        idx_prev = None if i == 0 else ("solutions-%s" % solutions[i - 1]["stem"],
                                        "solutions/%s.html" % solutions[i - 1]["stem"],
                                        solutions[i - 1]["name"])
        idx_next = None if i == len(solutions) - 1 else (
            "solutions-%s" % solutions[i + 1]["stem"],
            "solutions/%s.html" % solutions[i + 1]["stem"], solutions[i + 1]["name"])
        page = build_solution_page(sol, nav, idx_prev, idx_next)
        (SITE / "solutions" / (sol["stem"] + ".html")).parent.mkdir(exist_ok=True)
        (SITE / "solutions" / (sol["stem"] + ".html")).write_text(page, encoding="utf-8")
        search_index.append({"t": sol["name"] + " — solution", "u": "solutions/" + sol["stem"] + ".html",
                             "x": strip_tags(sol["text"])[:8000]})

    # assets
    (SITE / "assets" / "style.css").write_text(CSS + "\n" + pygments_css(), encoding="utf-8")
    (SITE / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")
    (SITE / "assets" / "checkpoints.js").write_text(
        "window.P4_CHECKPOINTS = %s;\n" % __import__("json").dumps(checkpoints),
        encoding="utf-8")
    (SITE / "assets" / "search-index.js").write_text(
        "window.P4_SEARCH = %s;\n" % __import__("json").dumps(search_index),
        encoding="utf-8")

    print("Built %d pages (%d solutions) into %s" %
          (len(PAGES) + len(solutions), len(solutions), SITE))


if __name__ == "__main__":
    sys.exit(main())
