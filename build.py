#!/usr/bin/env python3
"""Build the Year 9 Music teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package
manager, no lockfile, nothing that needs updating in years when nobody is
looking (see PRODUCT.md, Stack).

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets
overwritten.

Every page is built by the shared music shell (shell.py, copied in from
Sites/music-shell by its sync.py): direction B, Stage Card, chosen 19 October
2026. This file only turns the site's data into the shell's pieces. The Plot
world it replaced is recorded in DESIGN.md and DESIGN-NOTES.md.

The drawings (the unit plans, the small stage plot, the blueprint sheets)
live in plots.py, which is imported rather than inlined because they are more
SVG than this file can carry and stay readable.
"""

import json
import os
import shutil
import sys

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


# ------------------------------------------------------ the lesson, on the shell
#
# Lesson pages are built by the shared shell (shell.py). Everything below only
# translates this site's data into the shell's components. Every page is on the
# shell since 19 October 2026.


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
    links = "".join(f'<a class="btn btn-quiet int" href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{S.e(b["title"])}</a>'
                    for b in sheets if b.get("built"))
    waiting = [b["title"] for b in sheets if not b.get("built")]
    soon = f'<p class="fine">{S.e(", ".join(waiting))}: not on the site yet.</p>' if waiting else ""
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
    """One blueprint sheet, on the shell. A student can get back to the
    progression, the voicings, the pattern or the rules without asking twice,
    so each sheet is a page with its own address rather than a drawing that
    only exists inside a lesson. A blueprint is not a lesson: no week, no
    content code, no intention. What it has is the drawing and the rules
    under it."""
    base = site["base"]
    hd = S.head(sheet["title"], kicker=f'The blueprint · {term["name"]}')
    drawing = S.section("bp", "The sheet", "plot", None,
                        f'<div class="plan-scroll bp-scroll">{plots.blueprint(sheet["slug"])}</div>')
    how = S.learn([sheet["deck"], sheet["rules"]], label="How it works")

    built = [b for b in term["blueprint"] if b.get("built")]
    i = next(k for k, b in enumerate(built) if b["slug"] == sheet["slug"])
    def pn(k, word):
        if 0 <= k < len(built):
            return (word, built[k]["title"], f'/{term["id"]}/blueprint/{built[k]["slug"]}/')
        return None

    extras = S.fold(f'This term: {term["name"]}, {len(term["lessons"])} lessons',
                    S.schedule(term_schedule(term, current_no), base=base, label="This term",
                               title=term["name"]))
    extras += blueprint_card(site, term)
    return S.page(shell_site(site, course), title=sheet["title"], body=hd + drawing + how,
                  description=sheet["deck"],
                  crumbs=[("Home", "/"), (term["name"], f'/{term["id"]}/'), (sheet["title"], None)],
                  nav_current=term["id"], prevnext=(pn(i - 1, "Previous sheet"), pn(i + 1, "Next sheet")),
                  extras=extras)


# ---------------------------------------------------------- the home surface


def home_page(site, course, terms, current_term, current_no):
    """The front door, on the shell. Two jobs, in this order: put the class on
    the lesson it is actually on, then show the year as four units, down the
    page in teaching order, with the one being taught open. The multicore
    strip that used to run under the open unit retired with the shell; the
    open unit's hub has every lesson, one press away."""
    base = site["base"]
    total = sum(len(t["lessons"]) for t in terms)
    hd = S.head(course["name"], kicker=course["syllabus"], meta=f"Four units · {total} lessons")

    n_cur = len(current_term["lessons"])
    hub = (f"All {n_cur} lessons", f'/{current_term["id"]}/')
    cur = next((l for l in current_term["lessons"] if l["number"] == current_no), None)
    if cur and cur.get("body"):
        up = S.upto(cur["title"], base=base, href=f'/{current_term["id"]}/{cur["number"]:02d}/',
                    kicker=f'Term {current_term["n"]}, {current_term["name"]} · Lesson {cur["number"]:02d} '
                           f'of {n_cur} · Week {cur["week"]}',
                    lead=cur["body"]["lead"], links=[hub])
    else:
        # Honest rather than empty: name the position, admit there is no page.
        where = f"lesson {current_no:02d}" if current_no else "the start of the unit"
        up = S.upto(current_term["name"], base=base, href=None, kicker=f'Term {current_term["n"]}',
                    lead=f"The class is on {where}. That lesson has no page on the site yet, "
                         "so the unit's lesson list is the way in.", links=[hub])

    cards = []
    for t in terms:
        a = t["assessment"]
        live = t["id"] == current_term["id"]
        if live:
            word = f"Now, on lesson {current_no:02d}" if current_no else "Now"
        else:
            word = "Taught" if t["n"] < current_term["n"] else "Ahead"
        cards.append({"title": t["name"], "href": f'/{t["id"]}/', "open": live,
                      "kicker": f'Term {t["n"]} · {word}', "text": t["focus"],
                      "meta": f'{len(t["lessons"])} lessons · {a["type"]} · {a["weighting"]}'})
    return S.page(shell_site(site, course), title=course["name"], body=hd + up + S.card_grid(cards, base=base),
                  description=f"Year 9 Music {course['year']}, unit by unit and lesson by lesson.",
                  nav_current="home")


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
