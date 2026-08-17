# Year 9 Music 2027

Lesson material for a Year 9 Music elective, published with GitHub Pages. Students read
it; assessment stays in Canvas.

Read `DIRECTION.md` before touching any CSS, and `.impeccable/mocks/comp-d-thedesk.html`
before touching the lesson page. Comp D is the approved composition and it is king.

## How it works

- `data/` is the source of truth. `site.json`, `course/course.json`, and one
  `course/termN/term.json` per term.
- `build.py` turns that into static pages in `docs/`. Standard library only, no
  dependencies to install and nothing to keep updated.
- `docs/` is what GitHub Pages serves. It is generated. Never edit it by hand.

## Building

```
python3 build.py
```

## Where the lessons come from

`tools/extract_program.py` reads the four registered unit programs and writes the
lesson skeleton into each `term.json`: week, title, content dot point, outcomes,
learning intention, success criteria, activities, resources and the enduring
understanding. It is safe to rerun; the program wins on those fields and anything
authored by hand is carried across untouched.

The extractor deliberately leaves the unit programs' learning-adjustments column
behind. Adjustments are teacher-side only and none of it reaches the site.

## Authoring a lesson

A lesson gets a page when, and only when, it has a `body`. Everything the extractor
produces is the teacher's voice and is not student-facing prose, so the body has to be
written. See input 02 of `term2` for the shape: `lead`, `clauses`, `criteria`,
`listen`, `patched`, `plot`, `repertoire`, `bring`.

An input with no body still appears in the input list and on the term page. It just
has no link.

## The live position

`currentTerm` and `currentLesson` in `data/course/course.json`. That is the one row in
the input list wearing the term's tape, and it is updated from the daily debriefs.

## Repertoire

No track goes into a lesson without the full check, in this order: Apple explicitness
flag, then oEmbed for a live video id on the right channel, then duration. Two works
are barred from the site outright because they are the Term 3 unseen excerpts.

A `listen` track is `title`, `meta`, an optional `artist` and the verified id in
`embed`:

```json
{ "title": "Let It Be", "artist": "The Beatles", "meta": "The Beatles",
  "embed": "CGj85pVzRJs" }
```

`title` is the work, `meta` is the locating fact for that term (an era in some, an
artist in others), and `artist` renders only where it adds a name the row does not
already carry. `embed` makes the work's name playable in place. A track with no
`embed` still gets its row and simply cannot be played, which is the shape of a pick
still going through the check above. The ids themselves live in
`Music7-10_Y9_RepertoireRegister.md`, which is off this repo and stays there.

## What must never go on this site

Student names, student work, marks, markbook data, NESA past papers or marking
guidelines, the school's name or branding, and copyright audio or video files.
Recordings are embedded from their host, never uploaded. The site is public and every
page carries `noindex`.
