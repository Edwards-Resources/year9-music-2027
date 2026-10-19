# Year 9 Music 2027

Lesson material for a Year 9 Music elective, published with GitHub Pages. Students read
it; assessment stays in Canvas.

Every page is built on the shared music shell (`shell.py`, `assets/shell.css`,
`assets/shell.js`), the same look as the other music sites with Year 9's green accent.
Read `DESIGN.md` before changing how anything looks. The shell's own files here are
copies: never edit them in this repo. They are edited in `music-shell/`, a local repo
beside this one, and synced in.

## How it works

- `data/` is the source of truth. `site.json`, `course/course.json`, and one
  `course/termN/term.json` per term.
- `build.py` turns that into static pages in `docs/` by handing the data to the shell.
  Standard library only, no dependencies to install and nothing to keep updated.
- `plots.py` draws the unit drawings, the small stage plot and the blueprint sheets.
  These are this site's own; the shell does not know about them.
- `docs/` is what GitHub Pages serves. It is generated. Never edit it by hand.

## Building

```
/usr/bin/python3 build.py
```

The build has to run on the Mac's own Python 3.9, so no newer syntax.

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
written. See lesson 02 of `term2` for the shape: `lead`, `clauses`, `criteria`,
`listen`, `patched`, `plot`, `repertoire`, `bring`.

A lesson with no body still appears in its term's schedule. It just has no link.

The field names are from the site's first design and stay as they are; the page uses
plain words for them. `patched` prints as "You'll need", `clauses` as "What we do",
and `plot: "band"` adds the small stage plot beside it.

## The read: `guide`, `explain` and `worked`

Three optional blocks that sit after "What we do", in that order whatever order the data
is in. `LESSON-DEPTH-TRIAGE.md` says which lessons get one; do not add one to a lesson
the triage did not name. Lesson 04 of `term1` carries a guide and an explain and is the
worked example.

An `explain` is about 250 words. One per lesson. `body` items are `p`, `h` (a subhead)
or `ul`, and `**bold**` and `_italic_` work inside any of them:

```json
"explain": {
  "title": "I, V, vi and IV: what the numbers are doing",
  "body": [{ "p": "..." }, { "h": "..." }, { "ul": ["...", "..."] }]
}
```

A `guide` is a cue sheet. `at` is seconds into the recording:

```json
"guide": {
  "brief": "Press a name to play it from the top, or a time to drop into that moment.",
  "works": [{ "title": "With or Without You", "meta": "U2", "embed": "fRBOfkeCF7A",
              "cues": [{ "at": 8, "text": "..." }] }]
}
```

A `worked` is two takes: the same task answered twice, once so it earns and once so it does
not. Three lessons get one instead of an explain. `rungs` are optional and each is a named
move with a sentence under it, ALARM's moves where the task is a dot point and the task's
own where it is not:

```json
"worked": {
  "question": "Describe the tone colour in the opening of the excerpt.",
  "marks": "2 marks",
  "brief": "...",
  "model": "the answer that works",
  "rungs": [{ "move": "Identify", "text": "..." }],
  "zero": { "answer": "the answer that does not", "why": "..." }
}
```

**Two takes means two.** `question`, `model`, `zero.answer` and `zero.why` are all required
and the build fails without them. Write the failing answer at the length students actually
write, and make it one that looks fine: an obviously lazy answer teaches nothing.

**A work in the cue sheet is not also a row in `listen`.** All four guide lessons already
list the works their guide walks, so take them out of `listen` when you write the guide;
the build fails if you do not.

**Cue times are measured, never remembered.** A timestamp is a claim about a recording
and a wrong one fails in front of a class. `tools/loop.py` measures a chord loop's length
and where each pass starts, from the audio; anything it cannot reach waits for someone
with the recording and an ear.

## The live position

`currentTerm` and `currentLesson` in `data/course/course.json`, updated from the daily
debriefs. That lesson says "Up to here" on its own page, on its term's hub and on home,
and home opens its unit.

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
