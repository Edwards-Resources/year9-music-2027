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
import sys
from datetime import date

import plots

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import shell as S  # noqa: E402  the shared page shell, copied in by music-shell/sync.py
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


def rich(s):
    """Escape first, then allow a two-mark inline vocabulary: **bold** and
    _italic_.

    Everywhere else on this site the data is a label, a title or a single
    sentence, and `e()` is enough. The read blocks are the first sustained prose
    in the build and some of it has to emphasise inside a sentence: the first
    appearance of a word the student is being handed, and the name of a work.
    Escaping before converting means hand-edited data cannot inject markup.

    Unbalanced marks are left alone rather than guessed at, so an apostrophe or
    a stray underscore in a lesson never eats the rest of a paragraph.
    """
    out = e(s)
    for mark, tag in (("**", "strong"), ("_", "em")):
        parts = out.split(mark)
        if len(parts) % 2 == 1:
            out = "".join(p if i % 2 == 0 else f"<{tag}>{p}</{tag}>"
                          for i, p in enumerate(parts))
    return out


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
<link rel="stylesheet" href="{base}/assets/legacy.css">
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
<script src="{base}/assets/legacy.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ the rail


def rail(site, term, current_no, reading_no, reading_bp=None):
    """The input list. Permanent, and it carries every lesson of the term rather
    than a window onto it (comp D, binding).

    Two states that are usually different lessons. `now` is where the class is
    up to and is the one torn tape strip the rail is allowed; `reading` is the
    page you have open and is marked with the 4px painted keyline, because a
    second tape strip in the rail would break the two-strips-a-page rule.

    `reading_bp` is the same keyline, on a blueprint link in the foot rather
    than a channel in the body, for when the page open is one of the four
    sheets rather than a lesson.
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
        built_sheets = [b for b in term["blueprint"] if b.get("built")]
        waiting = [b for b in term["blueprint"] if not b.get("built")]
        items = [(f'<a class="reading" aria-current="page" '
                   f'href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>'
                   if b["slug"] == reading_bp else
                   f'<a href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>')
                 for b in built_sheets]
        # One line for the sheets that are not here yet, not one line each. Four
        # repetitions of the same absence on every page of the term is the
        # absence shouting louder than the sheets would.
        if waiting:
            names = ", ".join(e(b["title"]) for b in waiting)
            items.append(f'<span class="soon">{names}<i>not on the site yet</i></span>')
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


# ------------------------------------------------------ the lesson, on the shell
#
# Lesson pages are built by the shared shell (shell.py). Everything below only
# translates this site's data into the shell's components. The term hubs are on
# the shell too (further down). The home page and the blueprint sheets still use
# the old layout() until they move across.


def is_assessment(lesson):
    """Where the task is done or handed in, not where it is issued or discussed.
    Derived in tools/extract_program.py, which carries the rule."""
    return bool(lesson.get("assessmentEvent"))


def shell_site(site, course):
    """The site dict the shell's page() needs."""
    nav = [("Home", "/", "home")] + [(f"Term {t['n']}", f"/{t['id']}/", t["id"]) for t in TERMS]
    return {"base": site["base"], "title": course["name"], "year": 9, "key": "y9-2027",
            "foot": site["canvasNote"], "nav": nav, "noindex": site.get("noindex")}


def by(track):
    """Who the recording is by, but only where the meta field has not already
    said it. Half the sets locate a track by its artist and half by its era, so
    the two fields overlap on some rows and not others."""
    artist = (track.get("artist") or "").strip()
    meta = (track.get("meta") or "").lower()
    if not artist:
        return ""
    if any(w for w in artist.lower().split() if len(w) > 2 and w in meta):
        return ""
    return artist


def term_schedule(term, current_no):
    """The term's lessons grouped by week, for S.schedule. `now` is where the
    class is up to; an assessment lesson says so in words."""
    groups, order = {}, []
    for l in term["lessons"]:
        if l["week"] not in groups:
            groups[l["week"]] = []
            order.append(l["week"])
        st = None
        if current_no is not None and l["number"] == current_no:
            st = "now"
        elif current_no is not None and l["number"] < current_no:
            st = "done"
        built = bool(l.get("body"))
        groups[l["week"]].append({
            "n": f'{l["number"]:02d}', "title": l["title"], "meta": l["contentCode"], "state": st,
            "at": is_assessment(l), "href": f'/{term["id"]}/{l["number"]:02d}/' if built else None})
    return [(f"Week {w}", groups[w]) for w in order]


def blueprint_card(site, term):
    """The term's blueprint sheets, which are their own pages. Standalone only:
    every one is a link."""
    sheets = term.get("blueprint") or []
    if not sheets:
        return ""
    base = site["base"]
    links = "".join(f'<a class="btn btn-quiet int" href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>'
                    for b in sheets if b.get("built"))
    waiting = [b["title"] for b in sheets if not b.get("built")]
    soon = f'<p class="fine">{e(", ".join(waiting))}: not on the site yet.</p>' if waiting else ""
    return S.section("blueprint", "The blueprint", "plot", None, f'<p class="btns">{links}</p>{soon}')


def lesson_page(site, course, term, lesson, current_no):
    base = site["base"]
    b = lesson["body"]
    n, total = lesson["number"], len(term["lessons"])
    kicker = f'{term["name"]} · Week {lesson["week"]}'
    if n == current_no:
        kicker = "Up to here · " + kicker
    meta = f'Lesson {n} of {total} · {lesson["contentCode"]}'
    if b.get("repertoire"):
        meta += f' · {b["repertoire"]}'
    hd = S.head(lesson["title"], kicker=kicker, num=n, meta=meta,
                chips=[f'Bring: {b["bring"]}'] if b.get("bring") else ())
    it = S.intent(b["lead"], criteria=b.get("criteria") or (), outcomes=lesson.get("outcomes") or ())

    side = ""
    if b.get("plot") == "band":
        side += S.side_card("Stage plot", "plot", plots.small_stage(), cls="plot")
    if b.get("patched"):
        side += S.list_card("You'll need", "kit", [p["text"] for p in b["patched"]])
    secs = [S.steps([(c["kind"], c["text"]) for c in b["clauses"]], title="What we do", side=side)]

    if b.get("listen"):
        secs.append(S.listen([{"title": t["title"], "embed": t.get("embed"), "by": by(t),
                               "meta": t.get("meta", "")} for t in b["listen"]]))
    g = b.get("guide")
    if g:
        secs.append(S.cues([{"title": w["title"], "embed": w["embed"], "meta": w.get("meta", ""),
                             "cues": [(c["at"], c["text"]) for c in w["cues"]]} for w in g["works"]],
                           brief=g.get("brief", "")))
    x = b.get("explain")
    if x:
        secs.append(S.learn(x["body"], title=x["title"]))
    w = b.get("worked")
    if w:
        secs.append(S.worked(question=w["question"], marks=w.get("marks"), lead=w.get("brief"),
                             model=w["model"], rungs=[(r["move"], r["text"]) for r in w.get("rungs") or []],
                             zero=(w["zero"]["answer"], w["zero"]["why"]), title="Two takes",
                             labels=("The one that works", "The one that doesn’t")))
    end = [S.keep(lesson["enduring"])] if lesson.get("enduring") else []

    ls = term["lessons"]
    idx = next(i for i, l in enumerate(ls) if l["number"] == n)
    prev_l = next((l for l in reversed(ls[:idx]) if l.get("body")), None)
    next_l = next((l for l in ls[idx + 1:] if l.get("body")), None)
    pn = (("Previous", prev_l["title"], f'/{term["id"]}/{prev_l["number"]:02d}/') if prev_l else None,
          ("Next", next_l["title"], f'/{term["id"]}/{next_l["number"]:02d}/') if next_l else None)

    extras = S.fold(f'This term: {term["name"]}, {total} lessons',
                    S.schedule(term_schedule(term, current_no), base=base, label="This term",
                               title=term["name"]))
    extras += blueprint_card(site, term)
    return S.page(shell_site(site, course), title=f"{n:02d} {lesson['title']}",
                  body=S.lesson(hd, it, secs, end), description=b["lead"],
                  crumbs=[("Home", "/"), (term["name"], f'/{term["id"]}/'), (f"Lesson {n}", None)],
                  nav_current=term["id"], prevnext=pn, extras=extras)


# ------------------------------------------------------------- the term hub


# The strip retired from the hub with the shell. It stays here only for the old
# home page, and goes when the home moves across (increment 5).
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
    """The term hub, on the shell: head card, where the class is up to, the
    unit's own drawing at full size, the assessment, then every lesson grouped
    by week. The multicore strip retired with the shell; the schedule says
    the same thing in words. The blueprint sheets follow, standalone, as on
    every lesson page."""
    base = site["base"]
    a = term["assessment"]
    ls = term["lessons"]
    live = term["id"] == reading_term
    hd = S.head(term["name"], kicker=f'Term {term["n"]} · Unit {term["n"]} of 4',
                meta=f'{term["focus"]} · {len(ls)} lessons')

    # Where the class is up to, said on every hub. A hub for another term says
    # that it is not this one and points across.
    cur_t = next(t for t in TERMS if t["id"] == reading_term)
    cur = next((l for l in cur_t["lessons"] if l["number"] == current_no), None)
    up = ""
    if cur:
        k = f'Lesson {current_no:02d} of {len(cur_t["lessons"])} · Week {cur["week"]}'
        lead = ""
        if not live:
            k = f'Term {cur_t["n"]}, {cur_t["name"]} · {k}'
            lead = (f'{term["name"]} is done. The class has moved on to Term {cur_t["n"]}.'
                    if term["n"] < cur_t["n"] else
                    f'{term["name"]} has not started yet. The class is in Term {cur_t["n"]}.')
        up = S.upto(cur["title"], base=base, kicker=k, lead=lead,
                    href=f'/{cur_t["id"]}/{current_no:02d}/' if cur.get("body") else None)

    plan = S.section("plan", plots.SHEET_NAME[term["n"]].capitalize(), "plot", None,
                     f'<div class="plan-scroll">{plots.large(term["n"])}</div>')
    at = S.assessment(a["name"], kind=a["type"], issued=a["issued"], due=a["due"],
                      weighting=a["weighting"])

    built = sum(1 for l in ls if l.get("body"))
    note = "" if built == len(ls) else f"{built} of {len(ls)} lessons have a page so far."
    sched = S.schedule(term_schedule(term, current_no if live else None), base=base,
                       label="Every lesson", note=note)
    return S.page(shell_site(site, course), title=term["name"], body=hd + up + plan + at + sched,
                  description=f"{term['name']}, lesson by lesson.",
                  crumbs=[("Home", "/"), (term["name"], None)], nav_current=term["id"],
                  extras=blueprint_card(site, term))


# --------------------------------------------------------- the blueprint sheet


def blueprint_page(site, course, terms, term, sheet, current_no):
    """The blueprint, on its own plate. What STORY promises: a student can get
    back to the progression, the voicings, the pattern or the rules without
    asking twice, so each sheet is a real page with its own address rather
    than a drawing that only exists inside a lesson.

    Same plate the lesson page reads on, because this is still a document read
    on the sheet rather than done on the floor, and the same rail beside it so
    the input list does not disappear the moment a student leaves a lesson.
    There is no rider and no meta row: a blueprint is not a lesson and has no
    week, no content code, nothing patched in. What it has is the drawing and
    the rules under it, so the plate goes straight from the title block to the
    read.
    """
    base = site["base"]
    others = [b for b in term["blueprint"]
              if b["slug"] != sheet["slug"] and b.get("built")]
    other_links = "".join(
        f'<a href="{base}/{term["id"]}/blueprint/{o["slug"]}/">{e(o["title"])}</a>'
        for o in others)
    rules = "".join(f"<li>{rich(r)}</li>" for r in sheet["rules"])

    body = f"""<div class="wrap">
{rail(site, term, current_no, None, reading_bp=sheet["slug"])}
  <main class="stagearea" id="main">
    <div class="plate-wrap">
      <span class="tapestrip tl" aria-hidden="true"></span>
      <span class="tapestrip tr" aria-hidden="true"></span>
      <article class="plate">
        <div class="titleblock bp">
          <p class="of mono">The blueprint &middot; {e(term['name'])}</p>
          <h1>{e(sheet['title'])}</h1>
        </div>
        <div class="bpsheet">{plots.blueprint(sheet['slug'])}</div>
        <section class="read bprules">
          <h2>How it works</h2>
          <p>{rich(sheet['deck'])}</p>
          <ul>{rules}</ul>
        </section>
      </article>
    </div>
    <div class="underplate">
      <span class="lbl">Blueprint</span>{other_links}
      <span class="lbl">Unit</span>
      <a href="{base}/{term['id']}/">All {len(term['lessons'])} inputs</a>
    </div>
  </main>
</div>"""
    return layout(site, course, terms, sheet["title"], body,
                  sheet["deck"], term=term, active_id=term["id"])


# ---------------------------------------------------------- the home surface


def home_page(site, course, terms, current_term, current_no):
    """The front door.

    Two jobs, in this order. Put the class on the lesson it is actually on,
    because that is the one thing home certainly has to do and it is what the
    board is opened for at the start of a period. Then show the whole year as
    four units, because this world's argument is that the student is standing
    on all of it and only one set of lines is live.

    The year runs down the page in order and the four units are not equal. The
    three that are not live fold to a line each; the live one opens in place
    and carries its own thirty inputs on the multicore. That is the THESIS's
    own refusal made structural: week one and week nine cannot look identical
    if only one of them is open. It was built as four equal blocks in a row
    until 18 August 2026, which was the arrangement the THESIS names.

    No plan drawing here. The room is large on the term hub and small on a
    lesson page; a fifth, year-sized room would be a third scale of the same
    device and would say nothing the open unit does not already say. The
    multicore is a different object, not the room at a fourth size: a stage box
    is a real thing on its own and does not need the plot drawn above it.
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
        a = t["assessment"]
        href = f'{base}/{t["id"]}/'
        # How much of the unit is on the site. Silent once every input has a
        # page, because then the count is not news; loud while it is short.
        if built == n_l:
            pages = ""
        elif built == 0:
            pages = " &middot; no pages yet"
        elif built == 1:
            pages = f" &middot; 1 of {n_l} pages"
        else:
            pages = f" &middot; {built} of {n_l} pages"

        if live:
            # The open unit. It gets the space because it is the one being
            # taught, so the block moves down the page as the year runs rather
            # than sitting where it was drawn. Position is stated in words here
            # and drawn on the strip below, never on the keyline alone.
            pos = (f"On input {current_no:02d} of {n_l}" if current_no is not None
                   else f"The current unit &middot; {n_l} inputs")
            units.append(f"""<section class="unit open" data-term="{t['id']}"
      aria-label="{e(t['name'])}, the current unit">
      <div class="uhead">
        <span class="un mono">{t['n']}</span>
        <h3 class="uname"><a href="{href}">{e(t['name'])}</a></h3>
        <p class="upos mono">{pos}{pages}</p>
        <p class="ufocus">{e(t['focus'])}</p>
      </div>
      <div class="urun">
        <div class="uruninner">{multicore(site, t, current_no, True)}</div>
      </div>
      <p class="umeta mono">{e(a['name'])} &middot; {e(a['type'])}
        &middot; due {e(a['due'])} &middot; {e(a['weighting'])}</p>
    </section>""")
        else:
            # Folded. One line, and the whole line is the link to the unit.
            pos = "Taught" if t["n"] < current_term["n"] else "Ahead"
            units.append(f"""<a class="unit fold" href="{href}" data-term="{t['id']}">
      <span class="un mono">{t['n']}</span>
      <span class="uname">{e(t['name'])}</span>
      <span class="ufocus">{e(t['focus'])}</span>
      <span class="umeta mono">{n_l} inputs &middot; {e(a['type'])} &middot; {e(a['weighting'])}</span>
      <span class="upos mono">{pos}{pages}</span>
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


def assert_no_doubled_work(terms):
    """A work walked through in the cue sheet is not also a row in the listen
    block on the same page.

    All four guide inputs already carry a listen block holding exactly the works
    the guide walks, so the default outcome of authoring a guide is the same
    three names printed twice on one plate, once as a list and once as a cue
    sheet. The guide is the fuller of the two, so it takes the works and the
    listen block keeps whatever is left. Where nothing is left, the author drops
    the listen block, which is what the four guide inputs will do.

    Held by the build rather than by review because it is the one new rule here
    that an author would break by adding rather than by forgetting.
    """
    for term in terms:
        for lesson in term["lessons"]:
            b = lesson.get("body") or {}
            if not b.get("guide"):
                continue
            walked = {w["title"].strip().lower() for w in b["guide"]["works"]}
            listed = {t["title"].strip().lower() for t in b.get("listen") or []}
            both = walked & listed
            if both:
                raise SystemExit(
                    f"{term['id']} input {lesson['number']:02d}: "
                    f"{', '.join(sorted(both))} is in both the cue sheet and the "
                    "listen block. The cue sheet keeps it; take it out of listen.")


def assert_worked_complete(terms):
    """A worked block has both takes.

    The block is a comparison and there is nothing else in it. One answer with
    its reasoning shown is an explain with a quotation in it, and it would print
    under a heading saying two takes with one take under it. Held by the build
    rather than by review because the failing take is the half an author is
    tempted to leave for later, and the half the three inputs were given this
    block for.
    """
    for term in terms:
        for lesson in term["lessons"]:
            w = (lesson.get("body") or {}).get("worked")
            if not w:
                continue
            missing = [k for k in ("question", "model") if not w.get(k)]
            zero = w.get("zero") or {}
            missing += [f"zero.{k}" for k in ("answer", "why") if not zero.get(k)]
            if missing:
                raise SystemExit(
                    f"{term['id']} input {lesson['number']:02d}: the worked block "
                    f"is missing {', '.join(missing)}. Two takes means two.")


def main():
    global TERMS
    site = load("site.json")
    course = load("course", "course.json")
    TERMS = [load("course", t, "term.json") for t in course["terms"]]
    assert_no_doubled_work(TERMS)
    assert_worked_complete(TERMS)

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
        term_current = current_no if term["id"] == reading_term else None
        for lesson in term["lessons"]:
            if not lesson.get("body"):
                continue  # No page until the lesson is authored. See NEXT-SESSION.md.
            write([term["id"], f"{lesson['number']:02d}", "index.html"],
                  lesson_page(site, course, term, lesson, term_current))
            pages += 1
            lessons += 1
        for sheet in term.get("blueprint", []):
            if not sheet.get("built"):
                continue  # No page until the sheet is drawn. See NEXT-SESSION.md.
            write([term["id"], "blueprint", sheet["slug"], "index.html"],
                  blueprint_page(site, course, TERMS, term, sheet, term_current))
            pages += 1

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
