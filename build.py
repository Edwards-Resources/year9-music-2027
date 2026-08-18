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


def mmss(sec):
    """A cue time. Minutes are not padded and seconds always are, which is how a
    player writes it and so how a student will read it back off the screen."""
    sec = int(sec)
    return f"{sec // 60}:{sec % 60:02d}"


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
<script src="{base}/assets/site.js" defer></script>
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
        built_sheets = [b for b in term["blueprint"] if b.get("built")]
        waiting = [b for b in term["blueprint"] if not b.get("built")]
        items = [f'<a href="{base}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>'
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


# --------------------------------------------------------------- the drawing
# The lesson page's small drawing. plots.py carries it, same as the hub's.


PLOTS = {"band": plots.small_stage}



# --------------------------------------------------------------- the lesson


def is_assessment(lesson):
    """Where the task is done or handed in, not where it is issued or discussed.
    Derived in tools/extract_program.py, which carries the rule."""
    return bool(lesson.get("assessmentEvent"))


def by(track):
    """Who the recording is by, on its own line, but only where the meta field
    has not already said it. Half the sets locate a track by its artist and half
    by its era, so the two fields overlap on some rows and not others. A student
    finding the right recording at home needs the name; a student reading
    "The Beatles &middot; The Beatles" needs it once."""
    artist = (track.get("artist") or "").strip()
    meta = (track.get("meta") or "").lower()
    if not artist:
        return ""
    if any(w for w in artist.lower().split() if len(w) > 2 and w in meta):
        return ""
    return f'<i>{e(artist)}</i>'


def play_link(vid, title):
    """The name of a work, as the control that plays it.

    Written once and used by both blocks that name a recording. The listen block
    established the ruling on 17 August 2026 and the guide inherits it rather
    than inventing a second way to start a player: a student who has learned
    that a work's name is pressable on one block should not have to learn a
    button on the next.

    Both marks ride in the link and the CSS shows one. Swapping the shape in the
    stylesheet keeps the state in one place, and site.js only ever has to set
    aria-expanded. With scripting off this is what the markup says it is, a link
    to the recording.
    """
    marks = ('<svg class="mark go" viewBox="0 0 10 12" aria-hidden="true">'
             '<path d="M0 0 10 6 0 12Z"/></svg>'
             '<svg class="mark stop" viewBox="0 0 10 12" aria-hidden="true">'
             '<path d="M0 1H10V11H0Z"/></svg>')
    return (f'<a class="play" href="https://www.youtube.com/watch?v={vid}"'
            f' data-yt="{vid}" data-work="{title}">'
            f'{marks}<span class="vh">Play </span>{title}</a>')


def track_row(track):
    """One row of the listen block, with its player folded away.

    The row keeps the documented block shape: work, artist under it where the
    meta field has not said it, locating fact in mono at the right. What is new
    is that **the name of the work is the control**, marked with a triangle and
    playing the recording inside the row.

    The control is the name rather than a button in its own column because the
    column is 300px and the block sits inside it at 240. A 24px control column
    took 34px off the work name and put three of Term 4 input 08's three titles
    onto two lines each; a mark inside the name costs one line's indent and
    nothing on the rest. It also makes the whole title the target, which is
    what a tracklist does everywhere else a student has met one.

    Not three permanent iframes either. Term 3 input 01 and Term 4 input 08
    both carry three works; embedded outright that is 500px of another
    company's chrome sitting on the sheet and the block stops being a list.
    Folded away, the block is unchanged until a student asks for a track, and
    nothing is requested from the host until they do.

    With scripting off the control is what the markup says it is: a link to the
    recording. site.js upgrades it into a player in place.
    """
    title, meta = e(track["title"]), f'<span class="mono">{e(track["meta"])}</span>'
    if not track.get("embed"):
        # A track with no verified id keeps its row and is simply not playable.
        # The register's rule is that nothing is written into a lesson before it
        # is verified, so this is the shape of a pick still going through that.
        return f'<div class="tr"><span class="w"><b>{title}</b>{by(track)}</span>{meta}</div>'
    play = play_link(e(track["embed"]), title)
    return f'<div class="tr"><span class="w"><b>{play}</b>{by(track)}</span>{meta}</div>'


def guide_block(g):
    """The cue sheet: a work, and the times in it worth stopping at.

    A guide exists where the teacher would stop the recording and talk over it,
    which the depth triage found four times in 123 inputs. Three of those four
    walk more than one work, so the block is a list of works rather than one
    work with a list under it.

    The composition is the world's own: a cue time is a count, counts here are
    mono, and the number gutter it sits in is the 46px the clause numbers use
    directly above it, so one column of figures runs down the whole plate. The
    cue text is a sentence, which is why this is not in the 300px spec column
    with the listen block.

    Only the time is a link. The cue text stays text so it can be read off a
    projector and copied into a book without a student pressing it by accident,
    and the time is a real `watch?t=` link before site.js makes it a seek.

    The player folds out under the work's own name, above that work's cues, so
    a teacher pressing a cue sees the recording and the rest of the list at
    once. It is capped rather than run to the block's full width: this sits on
    a document, and half a metre of another company's chrome is not a document.
    """
    works = []
    for w in g["works"]:
        vid = e(w["embed"])
        cues = "".join(
            f'<li><a class="cue mono" data-at="{int(c["at"])}"'
            f' href="https://www.youtube.com/watch?v={vid}&amp;t={int(c["at"])}s">'
            f'{mmss(c["at"])}<span class="vh"> into {e(w["title"])}</span></a>'
            f'<span>{rich(c["text"])}</span></li>'
            for c in w["cues"])
        meta = f'<span class="mono">{e(w["meta"])}</span>' if w.get("meta") else ""
        works.append(f'<div class="gw"><h3>{play_link(vid, e(w["title"]))}{meta}</h3>'
                     f'<ol class="cues">{cues}</ol></div>')
    brief = f'<p class="brief">{rich(g["brief"])}</p>' if g.get("brief") else ""
    return (f'<section class="read guide"><h2>Cue sheet</h2>{brief}'
            f'<div class="gws">{"".join(works)}</div></section>')


def explain_block(x):
    """The long version: the taught content, written down.

    The first block in this world that is read rather than done, which is what
    decides everything about it. It cannot take a clause `kind`, because every
    clause kind names where the doing happens and there is no doing here. So it
    is not a fourth clause; it is a section of the document, a sibling of the
    title block and the keep block, and it takes the plate's own left edge and
    the 2px ink rule that already divides this sheet.

    It is on the sheet rather than the floor because it is a paragraph, which
    is the two grounds rule and not a preference.

    One per input and about 250 words, per the depth triage. The subheads and
    the list are there because a definition set reads better broken up than as
    four paragraphs; they are not licence to grow the block.
    """
    parts = []
    for item in x["body"]:
        if "h" in item:
            parts.append(f'<h4>{rich(item["h"])}</h4>')
        elif "ul" in item:
            parts.append("<ul>" + "".join(f"<li>{rich(i)}</li>" for i in item["ul"]) + "</ul>")
        else:
            parts.append(f'<p>{rich(item["p"])}</p>')
    return (f'<section class="read explain"><h2>The long version</h2>'
            f'<h3>{rich(x["title"])}</h3>{"".join(parts)}</section>')



def worked_block(w):
    """Two takes: the same task answered twice, once so it earns and once so it
    does not.

    The third block in this world that is read rather than done, and the first
    that shows rather than tells. `LESSON-DEPTH-TRIAGE.md` gives it to three
    inputs where the taught distinction is a difference between two pieces of
    writing that look alike on the page: a log entry against a diary entry, a
    dot point that earns a mark against one that does not, a rationale that
    names its decisions against one that describes its feelings. None of those
    survives being described. All three are seen in one look or not at all.

    So the composition is a comparison and everything in it is built to be read
    across rather than down. It is a section of the document like its two
    siblings, taking the plate's own left edge and the 2px ink rule, and it
    reuses the world's furniture rather than inventing any:

    - The question takes the read block's own h3, with its marks in mono
      immediately after it, because a count is mono here and because a single
      right-aligned figure with nothing under it reads as an orphan rather than
      as a column.
    - **Both specimens are marked, and the two marks are the world's own two
      line weights.** The take that works is bound by the 4px painted keyline,
      the take that does not is drawn with the 1px sheet rule, at the same
      inset. That is the two weights rule used as an argument: 4px bounds what
      is kept, 1px draws what is not. No fill, no tint and no colour, which the
      sheet does not take anyway, and each is said in words as well.
    - **A rung is a clause.** A named move with a sentence under it, in the same
      46px gutter the clauses and the cue times use, so the one column of
      figures runs down the whole plate. The moves are ALARM's where the task is
      a dot point and the task's own where it is not; the shape is what carries,
      not the vocabulary.

    The failing take is not dimmed and is not folded away. It is the half of the
    block a student has to study closely, and a page that is projected while the
    class compares the two has to hold both at once.
    """
    marks = (f'<span class="mono">&middot; {e(w["marks"])}</span>'
             if w.get("marks") else "")
    brief = f'<p class="brief">{rich(w["brief"])}</p>' if w.get("brief") else ""
    rungs = ""
    if w.get("rungs"):
        rungs = '<ol class="rungs">' + "".join(
            f'<li><span class="n mono">{i:02d}</span>'
            f'<div><h5>{e(r["move"])}</h5><p>{rich(r["text"])}</p></div></li>'
            for i, r in enumerate(w["rungs"], 1)) + "</ol>"
    return (f'<section class="read worked"><h2>Two takes{marks}</h2>'
            f'<h3>{rich(w["question"])}</h3>{brief}'
            f'<div class="take kept"><h4>The one that works</h4>'
            f'<p class="said">{rich(w["model"])}</p>{rungs}</div>'
            f'<div class="take dropped"><h4>The one that doesn\u2019t</h4>'
            f'<p class="said">{rich(w["zero"]["answer"])}</p>'
            f'<p>{rich(w["zero"]["why"])}</p></div></section>')

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
    # The row is ruled into as many cells as it has fields. A fixed five-column
    # grid gives the assessment lessons, which carry no repertoire, one
    # double-width cell and a rhythm that disagrees with every other page.
    tbcols = f"tbgrid c{len(meta)}"

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
        tracks = "".join(track_row(t) for t in b["listen"])
        spec.append(f'<div class="blk"><h4>Listen</h4><div class="listen">{tracks}</div></div>')
    if b.get("patched"):
        rows = "".join(f'<div class="row"><span class="n mono">{e(p["n"])}</span><span>{e(p["text"])}</span></div>'
                       for p in b["patched"])
        spec.append(f'<div class="blk"><h4>Patched in</h4>{rows}</div>')
    if lesson.get("outcomes"):
        codes = "".join(f'<span class="mono">{e(c)}</span>' for c in lesson["outcomes"])
        spec.append(f'<div class="blk"><h4>Outcomes</h4><div class="codes">{codes}</div></div>')

    # The read, under the rider and above the keep. The order inside it is the
    # teaching order and is fixed here rather than by the data: you hear the
    # thing before you are told what it is, which is what clause 01 of the one
    # input carrying both actually says, and you are shown it done after you
    # have been told what it is.
    read = ""
    if b.get("guide"):
        read += guide_block(b["guide"])
    if b.get("explain"):
        read += explain_block(b["explain"])
    if b.get("worked"):
        read += worked_block(b["worked"])

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
          <dl class="{tbcols}">{fields}</dl>
        </div>
        <div class="rider">
          <div class="clauses">
            <p class="lead">{e(b['lead'])}</p>
            {"".join(clauses)}
          </div>
          <div class="spec">{"".join(spec)}</div>
        </div>
        {read}{keep}
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
        parts = [f'<a href="{site["base"]}/{term["id"]}/blueprint/{b["slug"]}/">{e(b["title"])}</a>'
                 for b in term["blueprint"] if b.get("built")]
        waiting = [b for b in term["blueprint"] if not b.get("built")]
        if waiting:  # one line, as on the rail
            names = ", ".join(e(b["title"]) for b in waiting)
            parts.append(f'<span class="soon">{names}<i>not on the site yet</i></span>')
        blueprint = f'<div class="bpbar"><b>The blueprint</b><div>{"".join(parts)}</div></div>'

    body = f"""<main class="termpage" id="main">
  <div class="termhead">
    <p class="of mono">Unit {term['n']} of 4 &middot; {len(term['lessons'])} inputs</p>
    <h1>{e(term['name'])}</h1>
    <p class="focus">{e(term['focus'])}</p>
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
    <thead><tr><th>CH</th><th>Input</th><th>Content</th><th class="oc">Outcomes</th></tr></thead>
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
