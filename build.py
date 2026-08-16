#!/usr/bin/env python3
"""Build the Year 9 Music teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package
manager, no lockfile, nothing that needs updating in years when nobody is
looking (see PRODUCT.md, Stack).

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets
overwritten.

World: The Plot. The governing composition for the lesson page is
.impeccable/mocks/comp-d-thedesk.html, approved 16 August 2026. The term hub
and the home surface were designed in the build rather than comped; what they
are and what they departed from is in DESIGN-NOTES.md.

The room drawings live in plots.py, which is imported rather than inlined
because four hub-scale plans are more SVG than this file can carry and stay
readable.
"""

import html
import json
import os
import re
import shutil
from datetime import date

import plots

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(ROOT, "assets")


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


def e(s):
    # The programs mix straight and curly apostrophes. Curl only the ones sitting
    # inside a word, so contractions and possessives typeset properly and a
    # straight quotation mark round a word is left alone.
    return re.sub(r"(?<=\w)&#x27;(?=\w)", "’", html.escape(str(s), quote=True))


def write(path_parts, markup):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markup)


DIRECTION = """<!--
THESIS: The year is the room drawn from above, and every lesson is a numbered input on the list. It refuses the course-site default of equal-weight lesson cards in a grid, where week one and week nine look identical, and it refuses the paper ground all three sibling sites share.
OWN-WORLD: Stage-floor black (#111214), chalk white line (#F2F1EC) for everything drawn on the floor, one fluoro gaffer-tape colour per term (#E8FF3A, #FF2D78, #FF6A1F, #3DFF7D) always carrying black ink. Sustained reading happens inside taped white panels laid on the floor, never as long white prose over the black field. Square corners, no shadows, no gradients, two line weights: a 1px chalk hairline and a 4px painted keyline. Tape ends are torn, never cut square.
STORY: A student sees the room, finds their own position in it, reads what they are doing this lesson off a taped panel, and can get back to the blueprint, the progression, the voicings and the rules, without asking for it twice.
FIRST VIEWPORT: The plan view of the room fills the field, positions numbered and drawn in chalk line. Beside it the input list runs as a ruled channel table, one row per lesson, numbered from 01. The current lesson is the only row with a torn strip of the term's tape across it. The term's own tape colour bounds the plate at the head; the other three terms sit under the plan as ghost line at low opacity.
FORM: The Plot, the stage plot and input list a band hands the sound engineer. Candidate 6 of the grounded list, seed key 8d99cc59. Re-rolled once by the user, then pinned back to The Plot by the user, 16 August 2026; a user-pinned direction beats the roll.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->"""


# --------------------------------------------------------------- page shell


def floorbar(site, course, terms, active_id):
    """The class mark, the year, and the four units. One of the three places the
    stencil face is allowed."""
    base = site["base"]
    links = []
    for t in terms:
        on = " class=\"on\"" if t["id"] == active_id else ""
        links.append(f'<a href="{base}/{t["id"]}/"{on}>{t["n"]} {e(t["name"])}</a>')
    return f"""<div class="floorbar">
  <a class="mark" href="{base}/">{e(course['mark'])}</a>
  <span class="yr mono">{e(course['year'])}</span>
  <nav aria-label="Units">{"".join(links)}</nav>
</div>"""


def layout(site, course, terms, title, body, description="", term=None, active_id=None):
    base = site["base"]
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""
    full_title = e(title) if title == site["title"] else e(title) + " | " + e(site["title"])
    tape = f' data-term="{term["id"]}"' if term else ""
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}
<title>{full_title}</title>
<meta name="description" content="{e(description)}">
<link rel="preload" href="{base}/assets/fonts/chivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}/assets/site.css">
</head>
<body{tape}>
{DIRECTION}
<a class="skip" href="#main">Skip to the lesson</a>
{floorbar(site, course, terms, active_id)}
{body}
<footer class="foot">
  <p>{e(site['canvasNote'])}</p>
  <p class="mono">Updated {date.today().strftime('%-d %B %Y')}</p>
</footer>
</body>
</html>
"""


# ------------------------------------------------------------------ the rail


def rail(site, term, current_no, reading_no):
    """The input list. Permanent, and it carries every lesson of the term rather
    than a window onto it (comp D, binding).

    Two states that are usually different lessons. `now` is where the class is
    up to and is the one torn tape strip the rail is allowed; `reading` is the
    page you have open and is marked with the 4px painted keyline, because a
    second tape strip in the rail would break the two-strips-a-page rule.
    """
    base = site["base"]
    rows, week = [], None
    for l in term["lessons"]:
        if l["week"] != week:
            week = l["week"]
            rows.append(f'<div class="wk">Week {week}</div>')
        cls = ["ch"]
        if l["number"] == current_no:
            cls.append("now")
        elif current_no is not None and l["number"] < current_no:
            cls.append("done")
        if l["number"] == reading_no:
            cls.append("reading")
        if is_assessment(l):
            cls.append("at")
        built = bool(l.get("body"))
        state = ""
        if l["number"] == current_no:
            state = '<span class="vh"> (where the class is up to)</span>'
        elif current_no is not None and l["number"] < current_no:
            state = '<span class="vh"> (already taught)</span>'
        if not built:
            cls.append("nopage")
        inner = (f'<span class="n mono">{l["number"]:02d}</span>'
                 f'<span class="t">{e(l["title"])}{state}</span>')
        if built:
            cur = ' aria-current="page"' if l["number"] == reading_no else ""
            rows.append(f'<a class="{" ".join(cls)}" href="{base}/{term["id"]}/{l["number"]:02d}/"{cur}>{inner}</a>')
        else:
            rows.append(f'<span class="{" ".join(cls)}">{inner}</span>')

    foot = ""
    if term.get("blueprint"):
        items = []
        for b in term["blueprint"]:
            if b.get("built"):
                items.append(f'<a href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>')
            else:
                items.append(f'<span class="soon">{e(b["title"])}<i>not on the site yet</i></span>')
        foot = f'<div class="railfoot"><b>The blueprint</b>{"".join(items)}</div>'

    # A <details>, not a scripted toggle: on a phone the list closes so the
    # lesson is what you land on, and with scripting off it still opens.
    # At desktop width the CSS keeps it open and takes the summary out of reach.
    return f"""<nav class="rail" aria-label="{e(term['name'])} input list">
  <details open>
    <summary class="railhead"><b>Input list</b><i class="mono">{len(term['lessons'])} CH</i></summary>
    <div class="railbody">{"".join(rows)}{foot}</div>
  </details>
</nav>"""


# --------------------------------------------------------------- the drawing
# The lesson page's small drawing. plots.py carries it, same as the hub's.


PLOTS = {"band": plots.small_stage}



# --------------------------------------------------------------- the lesson


def is_assessment(lesson):
    """Where the task is done or handed in, not where it is issued or discussed.
    Derived in tools/extract_program.py, which carries the rule."""
    return bool(lesson.get("assessmentEvent"))


def lesson_page(site, course, term, lesson, current_no):
    """comp D. The plate is the reading surface and long prose never sits on the
    black floor."""
    base = site["base"]
    b = lesson["body"]
    n, total = lesson["number"], len(term["lessons"])

    if lesson["number"] == current_no:
        standing = "on the desk"
    elif current_no is not None and lesson["number"] < current_no:
        standing = "taught"
    else:
        standing = "coming up"

    meta = [("Unit", term["name"]), ("Week", str(lesson["week"])),
            ("Content", lesson["contentCode"])]
    if b.get("repertoire"):
        meta.append(("Repertoire", b["repertoire"]))
    if b.get("bring"):
        meta.append(("Bring", b["bring"]))
    fields = "".join(f"<div><dt>{e(k)}</dt><dd class=\"mono\">{e(v)}</dd></div>" for k, v in meta)

    clauses = []
    for i, c in enumerate(b["clauses"]):
        clauses.append(f'<div class="cl"><span class="n mono">{i+1:02d}</span>'
                       f'<div><h3>{e(c["kind"])}</h3><p>{e(c["text"])}</p></div></div>')
    if b.get("criteria"):
        items = "".join(f"<li>{e(c)}</li>" for c in b["criteria"])
        clauses.append(f'<div class="cl"><span class="n mono">{len(b["clauses"])+1:02d}</span>'
                       f'<div><h3>You can do it when</h3><ul class="sc">{items}</ul></div></div>')

    spec = []
    if b.get("plot") in PLOTS:
        spec.append(f'<div class="plot"><h4>Stage plot</h4>{PLOTS[b["plot"]]()}</div>')
    if b.get("listen"):
        tracks = "".join(f'<div class="tr"><b>{e(t["title"])}</b><span class="mono">{e(t["meta"])}</span></div>'
                         for t in b["listen"])
        spec.append(f'<div class="blk"><h4>Listen</h4><div class="listen">{tracks}</div></div>')
    if b.get("patched"):
        rows = "".join(f'<div class="row"><span class="n mono">{e(p["n"])}</span><span>{e(p["text"])}</span></div>'
                       for p in b["patched"])
        spec.append(f'<div class="blk"><h4>Patched in</h4>{rows}</div>')
    if lesson.get("outcomes"):
        codes = "".join(f'<span class="mono">{e(c)}</span>' for c in lesson["outcomes"])
        spec.append(f'<div class="blk"><h4>Outcomes</h4><div class="codes">{codes}</div></div>')

    keep = ""
    if lesson.get("enduring"):
        keep = f'<div class="keep"><b>Worth keeping</b>{e(lesson["enduring"])}</div>'

    # Under the plate, back on the floor.
    idx = next(i for i, l in enumerate(term["lessons"]) if l["number"] == n)
    nxt = next((l for l in term["lessons"][idx+1:] if l.get("body")), None)
    under = []
    if nxt:
        under.append('<span class="lbl">Next</span>'
                     f'<a href="{base}/{term["id"]}/{nxt["number"]:02d}/">'
                     f'{nxt["number"]:02d} &middot; {e(nxt["title"])}</a>')
    under.append('<span class="lbl">Term</span>'
                 f'<a href="{base}/{term["id"]}/">All {total} inputs</a>')

    body = f"""<div class="wrap">
{rail(site, term, current_no, n)}
  <main class="stagearea" id="main">
    <div class="plate-wrap">
      <span class="tapestrip tl" aria-hidden="true"></span>
      <span class="tapestrip tr" aria-hidden="true"></span>
      <article class="plate">
        <div class="titleblock">
          <p class="of mono">Input {n:02d} of {total} &middot; {standing}</p>
          <h1>{e(lesson['title'])}</h1>
          <dl class="tbgrid">{fields}</dl>
        </div>
        <div class="rider">
          <div class="clauses">
            <p class="lead">{e(b['lead'])}</p>
            {"".join(clauses)}
          </div>
          <div class="spec">{"".join(spec)}</div>
        </div>
        {keep}
      </article>
    </div>
    <div class="underplate">{"".join(under)}</div>
  </main>
</div>"""
    return layout(site, course, TERMS, f"{n:02d} {lesson['title']}", body,
                  b["lead"], term=term, active_id=term["id"])


# ------------------------------------------------------------- the term hub


def multicore(site, term, current_no, live):
    """Thirty inputs as a single line along the downstage edge, held from comp B
    and built here for the first time.

    The strip is plugged into the room: it sits directly under the drawing's
    downstage edge, with no gap, so the channels read as running out of the
    room rather than as a row of boxes beneath a picture. Every channel is the
    same width, which on this surface is the point rather than the failing the
    thesis complains about; on a multicore the channels *are* equal, and what
    separates them is what is patched into each.
    """
    base = site["base"]
    cells = []
    for l in term["lessons"]:
        cls = ["cell"]
        if live and l["number"] == current_no:
            cls.append("now")
        elif live and current_no is not None and l["number"] < current_no:
            cls.append("done")
        if is_assessment(l):
            cls.append("at")
        n = f'<span class="n mono">{l["number"]:02d}</span>'
        # The number alone is not a name. The title rides with it, unseen, so
        # the strip is usable without the drawing.
        name = f'<span class="vh">{e(l["title"])}</span>'
        if l.get("body"):
            cells.append(f'<a class="{" ".join(cls)}" '
                         f'href="{base}/{term["id"]}/{l["number"]:02d}/">{n}{name}</a>')
        else:
            cells.append(f'<span class="{" ".join(cls)}">{n}{name}</span>')

    # The week ruler. Each week is flexed by how many inputs it holds, so its
    # boundaries fall exactly where the channels change week.
    weeks, order = {}, []
    for l in term["lessons"]:
        if l["week"] not in weeks:
            weeks[l["week"]] = 0
            order.append(l["week"])
        weeks[l["week"]] += 1
    ruler = "".join(f'<span style="flex:{weeks[w]} 1 0">{w}</span>' for w in order)

    return f"""<nav class="core-wrap" aria-label="{e(term['name'])} input strip">
  <div class="core">{"".join(cells)}</div>
  <div class="ruler">{ruler}</div>
  <span class="rlbl" aria-hidden="true">Week</span>
</nav>"""


def term_page(site, course, term, current_no, reading_term):
    """The term hub. The room is large here and nowhere else, the multicore runs
    out of its downstage edge, and the full input list sits under both."""
    a = term["assessment"]
    live = term["id"] == reading_term
    rows, week = [], None
    for l in term["lessons"]:
        if l["week"] != week:
            week = l["week"]
            rows.append(f'<tr class="wkrow"><th colspan="4" scope="rowgroup">Week {week}</th></tr>')
        cls = []
        if live and l["number"] == current_no:
            cls.append("now")
        elif live and current_no is not None and l["number"] < current_no:
            cls.append("done")
        if is_assessment(l):
            cls.append("at")
        # The rows that have a page are the exception at the moment, so the page
        # says how many once at the top rather than tagging the other 29.
        title = e(l["title"])
        if l.get("body"):
            title = f'<a href="{site["base"]}/{term["id"]}/{l["number"]:02d}/">{title}</a>'
        rows.append(f'<tr class="{" ".join(cls)}">'
                    f'<td class="n mono">{l["number"]:02d}</td>'
                    f'<td class="ti">{title}</td>'
                    f'<td class="cd mono">{e(l["contentCode"])}</td>'
                    f'<td class="oc mono">{e(" ".join(l["outcomes"]))}</td></tr>')

    built = sum(1 for l in term["lessons"] if l.get("body"))
    if built == 0:
        state = "No input has a page on the site yet."
    elif built == len(term["lessons"]):
        state = "Every input has a page."
    elif built == 1:
        state = "One input has a page so far."
    else:
        state = f"{built} inputs have a page so far."

    # Where the class is, stated in words as well as marked on the strip.
    if live and current_no is not None:
        cur = next((l for l in term["lessons"] if l["number"] == current_no), None)
        standing = (f'<p class="standing"><span class="strip">On the desk</span>'
                    f'<span class="mono">Input {current_no:02d}</span>'
                    f'<span>{e(cur["title"])}</span></p>') if cur else ""
    else:
        standing = ('<p class="standing"><span class="mono">Not the current unit</span>'
                    f'<span>{state}</span></p>')

    blueprint = ""
    if term.get("blueprint"):
        items = "".join(
            (f'<a href="{site["base"]}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>'
             if b.get("built") else
             f'<span class="soon">{e(b["title"])}<i>not on the site yet</i></span>')
            for b in term["blueprint"])
        blueprint = f'<div class="bpbar"><b>The blueprint</b><div>{items}</div></div>'

    body = f"""<main class="termpage" id="main">
  <div class="termhead">
    <p class="of mono">Unit {term['n']} of 4 &middot; {len(term['lessons'])} inputs &middot; {e(term['focus'])}</p>
    <h1>{e(term['name'])}</h1>
    {standing}
  </div>

  <div class="plan">
    <div class="planinner">
      <div class="sheet">{plots.large(term["n"])}</div>
      {multicore(site, term, current_no, live)}
    </div>
  </div>

  <div class="atbar">
    <span class="lbl">{e(a['name'])}</span>
    <span>{e(a['type'])}</span>
    <span class="mono">Issued {e(a['issued'])} &middot; due {e(a['due'])} &middot; {e(a['weighting'])}</span>
    <span>Task and rubric in Canvas</span>
  </div>
  {blueprint}

  <h2 class="listhead">Every input<i class="mono">{state}</i></h2>
  <table class="inputs">
    <thead><tr><th>CH</th><th>Input</th><th>Content</th><th>Outcomes</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table>
</main>"""
    return layout(site, course, TERMS, term["name"], body,
                  f"{term['name']}, input by input.", term=term, active_id=term["id"])


# ---------------------------------------------------------- the home surface


def home_page(site, course, terms, current_term, current_no):
    """The front door.

    Two jobs, in this order. Put the class on the lesson it is actually on,
    because that is the one thing home certainly has to do and it is what the
    board is opened for at the start of a period. Then show the whole year as
    four units, because this world's argument is that the student is standing
    on all of it and only one set of lines is live.

    No plan drawing here. The room is large on the term hub and small on a
    lesson page; a fifth, year-sized room would be a third scale of the same
    device and would say nothing the four unit blocks do not already say.
    """
    base = site["base"]
    total = sum(len(t["lessons"]) for t in terms)

    # On the desk. The lead is a sentence, so it reads on a taped panel and
    # never on the black floor. This is the page's one torn strip.
    cur = next((l for l in current_term["lessons"]
                if l["number"] == current_no), None)
    if cur and cur.get("body"):
        href = f'{base}/{current_term["id"]}/{cur["number"]:02d}/'
        desk = f"""<div class="deskplate">
      <span class="tapestrip tl" aria-hidden="true"></span>
      <article class="plate">
        <div class="titleblock">
          <p class="of mono">On the desk &middot; {e(current_term['name'])} &middot; input {cur['number']:02d} of {len(current_term['lessons'])}</p>
          <h2><a href="{href}">{e(cur['title'])}</a></h2>
        </div>
        <p class="desklead">{e(cur['body']['lead'])}</p>
        <p class="deskgo"><a href="{href}">Open input {cur['number']:02d}</a>
          <a class="alt" href="{base}/{current_term['id']}/">All {len(current_term['lessons'])} inputs</a></p>
      </article>
    </div>"""
    else:
        # Honest rather than empty: name the position, admit there is no page.
        where = f"input {current_no:02d}" if current_no else "the start of the unit"
        desk = f"""<div class="deskplate">
      <span class="tapestrip tl" aria-hidden="true"></span>
      <article class="plate">
        <div class="titleblock">
          <p class="of mono">On the desk &middot; {e(current_term['name'])}</p>
          <h2>{e(current_term['name'])}</h2>
        </div>
        <p class="desklead">The class is on {where}. That input has no page on
          the site yet, so the unit's input list is the way in.</p>
        <p class="deskgo"><a href="{base}/{current_term['id']}/">All {len(current_term['lessons'])} inputs</a></p>
      </article>
    </div>"""

    units = []
    for t in terms:
        n_l = len(t["lessons"])
        live = t["id"] == current_term["id"]
        built = sum(1 for l in t["lessons"] if l.get("body"))
        if live and current_no is not None:
            pos = f"On input {current_no:02d}"
        elif t["n"] < current_term["n"]:
            pos = "Taught"
        else:
            pos = "Ahead"
        pages = ("no pages yet" if built == 0
                 else "1 page" if built == 1 else f"{built} pages")
        units.append(f"""<a class="unit{' live' if live else ''}" href="{base}/{t['id']}/"
      data-term="{t['id']}">
      <span class="un mono">{t['n']}</span>
      <span class="uname">{e(t['name'])}</span>
      <span class="ufocus">{e(t['focus'])}</span>
      <span class="umeta mono">{n_l} inputs &middot; {e(t['assessment']['type'])} &middot; {e(t['assessment']['weighting'])}</span>
      <span class="upos mono">{pos} &middot; {pages}</span>
    </a>""")

    body = f"""<main class="home" id="main">
  <div class="homehead">
    <h1>Year 9 Music</h1>
    <p class="of mono">{e(course['syllabus'])} &middot; four units &middot; {total} inputs</p>
  </div>

  {desk}

  <h2 class="yearhead">The year</h2>
  <div class="units">{"".join(units)}</div>
</main>"""
    return layout(site, course, terms, site["title"], body,
                  f"Year 9 Music {course['year']}, unit by unit and input by input.",
                  term=current_term)


# --------------------------------------------------------------------- main


TERMS = []


def main():
    global TERMS
    site = load("site.json")
    course = load("course", "course.json")
    TERMS = [load("course", t, "term.json") for t in course["terms"]]

    reading_term = course.get("currentTerm") or TERMS[0]["id"]
    current_term = next(t for t in TERMS if t["id"] == reading_term)
    current_no = course.get("currentLesson")

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages, lessons = 0, 0
    for term in TERMS:
        write([term["id"], "index.html"], term_page(site, course, term, current_no, reading_term))
        pages += 1
        for lesson in term["lessons"]:
            if not lesson.get("body"):
                continue  # No page until the lesson is authored. See NEXT-SESSION.md.
            write([term["id"], f"{lesson['number']:02d}", "index.html"],
                  lesson_page(site, course, term, lesson,
                              current_no if term["id"] == reading_term else None))
            pages += 1
            lessons += 1

    write(["index.html"], home_page(site, course, TERMS, current_term, current_no))
    pages += 1

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    total = sum(len(t["lessons"]) for t in TERMS)
    print(f"built {pages} pages into docs/")
    print(f"  position: {current_term['name']}, input {current_no}")
    print(f"  {lessons} of {total} inputs have an authored body and a page")


if __name__ == "__main__":
    main()
