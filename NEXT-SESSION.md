# Next session: Year 9 Music 2027 site

## Where this stands, 16 August 2026

**The scaffold is built, the lesson page reproduces comp D, and the site is live.**

- **https://edwards-resources.github.io/year9-music-2027/**
- Repo: `Edwards-Resources/year9-music-2027`, public, Pages serving `main` `/docs`.
- The history starts at `3f52abb`, which is the whole build as one commit. It was
  deliberately rebuilt that way before the first push; see the redaction note below.

The world and the composition are unchanged; this session added the machinery under
them.

| File | What it is |
| --- | --- |
| `PRODUCT.md` | Product truth. |
| `DIRECTION.md` | The direction contract, the rules the world establishes, the anti-references, the fonts. |
| `README.md` | How to build, how to author a lesson, what must never go on the site. |
| `build.py` | Reads `data/`, writes `docs/`. Standard library only. |
| `tools/extract_program.py` | Pulls the lesson skeleton out of the four registered unit programs. Safe to rerun. |
| `data/` | `site.json`, `course/course.json`, four `course/termN/term.json`. |
| `assets/` | `site.css` and the three self-hosted fonts. |
| `docs/` | Build output. Generated, never edited by hand. |
| `.impeccable/mocks/comp-d-thedesk.html` | **Comp D, approved.** Still the governing composition. |

## What was built

**The data spine.** All 123 learning-experience rows across the four unit programs are
extracted into `data/`: week, title, content dot point and its code, the two outcome
codes the strand delivers, learning intention, success criteria, activities, resources
and the enduring understanding. The extractor deliberately drops the
learning-adjustments column, per the teacher-side-only decision.

The extractor also derives `assessmentEvent`, which is what puts the square marker on
an input list row. It is true only where the task is done or handed in, never where it
is issued or discussed, which is exactly the set comp D marks: Term 2 inputs 21, 25, 26
and 28.

**The lesson page.** Term 2 input 02, the lesson comp D was approved on, is authored
and built. Measured element by element against the comp at 1440, every box matches to
the pixel: the floor bar, the rail, the tape strip, the plate, the title block, the
five-field meta row, the clauses, the spec column, the plan drawing, the keep block.

Three deliberate departures, all recorded rather than slipped in:

1. **The rail has two states, not one.** `now` is where the class is up to and wears
   the term's tape. `reading` is the page you have open and gets the 4px painted
   keyline, because a second tape strip in the rail would break the two-strips-a-page
   rule. On comp D's own lesson the two coincide, so the comp could not show this.
2. **An input with no page yet is not dimmed.** It is a real lesson in the term and the
   comp's rail is chalk white. Dimming it would mark 122 of the 123 as inactive until
   the content pour.
3. **A footer.** The Canvas note and the snapshot date, on the floor below the plate.
   The comp has none. Every sibling site does, and PRODUCT requires the Canvas
   link-out. **Flag for the finish review.**

**Mobile is now proved rather than assumed.** No horizontal overflow at 375. The input
list stays open, so the disclosure state and what a screen reader is told never
disagree, but it is capped at 42vh and scrolls, so the lesson is not thirty rows down
the page. Between 980 and 1100 the spec column drops under the clauses and its blocks
go side by side, because a full-width plan drawing would break comp D's rule that the
room is small on a lesson page and large only on the hub.

**Fonts self-hosted**: Saira Stencil One plus the Chivo and Chivo Mono variable faces,
latin subset, confirmed loading with their real weight axes. Nothing from a CDN.

## The redaction, and why the history is one commit

`PRODUCT.md` named both AT3 unseen excerpts with their YouTube ids, and
`NEXT-SESSION.md` named them too. This repo is public, so that hands a student the
paper, which is the exact thing the rule three lines above it exists to prevent. Both
were redacted to a pointer at `Music7-10_Y9_RepertoireRegister.md`, which is off this
repo and is the proper authority for repertoire.

The three original local commits already contained the strings and git history is
permanent, so the history was rebuilt as a single clean commit before the first push
rather than layering a redaction on top of it. Verified across the whole history: no
ids, no work titles, no school name.

**The lesson for the content sessions: the register is the only place those two works
are written down, and it must stay that way.** Do not copy them into a note here to
make it easier to follow.

## The actual next task

1. **Design the term hub.** No approved comp. It currently renders as a page that says
   so in as many words, with the registered input list under it, so nothing links into
   nowhere. B's multicore strip, thirty lessons as one line along the downstage edge,
   is the starting point, and this is where the plan drawing is allowed to be large and
   where the other three terms show through as ghost line. B rendered those ghosts
   weakly at 7 to 10 percent; rebuild the device before trusting it.
2. **Design the home surface.** No comp at all. `docs/index.html` is currently a copy
   of the current lesson page, which is the one thing home certainly has to do, and
   nothing more.
3. Then the content pour, which is a different kind of session again. See below.

## What is genuinely missing

- **122 of 123 lessons have no authored body**, so they have no page. They appear in
  the input list and on the term page with no link, which is honest and looks
  deliberate. The extractor's `steps`, `intention` and `criteria` are in the teacher's
  voice and are **not** student-facing prose. **The content sessions are writing, not
  conversion, and should be costed that way.**
- **No verified YouTube ids for 24 of the 26 repertoire picks.** The two verified ones
  are both **barred from the site** because they are the Term 3 unseen excerpts, and
  **neither is named anywhere in this repository**, which is public. They live in the
  repertoire register, off this repo, and that is the only place they are written down.
  Every other track needs the full order before it goes into a lesson: Apple
  explicitness flag, then oEmbed for a live id and the right channel, then duration.
  That order, every time.
- **The Term 3 ATSI protocol block, Weeks 4 to 6, is deliberately empty** and stays
  that way until Matthew selects through the school's consultation. Honest placeholder;
  nothing invented.
- **No AT3 exam paper.** Still open on the program thread, not this one.
- **No DESIGN.md and no finish review.** The direction contract ends with "unreviewed
  and undocumented is unfinished". Both are owed once the term hub and home exist.

## Open questions for the finish review

- **The listen block names no artist.** Comp D shows title and era only, so the build
  reproduces that, but "Sweet Home Chicago / 1930s" without Robert Johnson is thin for
  a student. The artist is already in the data, unused.
- **`--hair` at `#313337` on the floor is 1.48:1.** It is the chalk hairline and comp D
  sets it, so it stands, but it is faint on a projector in a daylit room, which is a
  stated product constraint. Worth a ruling rather than a drift.
- **An input with no page has no static affordance** telling you it is not a link, only
  the absence of a hover state. Transient, and it goes away with the content pour.
- **The live position is a placeholder.** `currentLesson` is set to Term 2 input 02 so
  the build could be checked against the comp. It becomes real when 2027 teaching
  starts. `positionNote` in `course.json` says so.

## Watch out for

- **Contrast is a product constraint here, not a style preference.** Every text pair in
  use was measured and passes AA: chalk 16.6, chalk-dim 5.8, the already-taught grey
  6.7, ink on sheet 16.4, and black ink on all four tapes from 5.1 to 16.8. Check every
  new dimmed state on the black ground.
- **Two tape strips per page at most.** One on the rail's current row, one holding the
  plate down. A third is a defect, and the tape is torn, never cut square.
- **The stencil face is not a heading face.** Three uses only: class mark, input list
  head, lesson title. The CSS enforces this with one selector; do not widen it.
- **Elements of music, never "concepts of music".** Only the ten real outcome codes exist.
- **No school name anywhere in the repository**, not just on the built site. Swept clean
  at the commit; grep any new file before committing.
- **No student names, work or marks**, ever. `noindex` on every page.
- **Never `git stash` in these repos** now that `docs/` is tracked build output.
- **The repo is public and live, and git history is permanent.** Sweep any new file
  before committing, not just before pushing: once it is in a commit that has been
  pushed, taking it out means rewriting published history. **Ask Matthew before
  pushing.**
- **`year8-music` has the same problem already, unfixed.** That repo is public and has
  the school's name in it, including in served pages under `docs/`. Not this session's
  job and not touched, but it needs one: scrubbing it means rewriting that repo's
  published history, not a follow-up commit.

## Model and effort

**Opus, medium**, for the term hub and the home surface: two compositions that do not
yet exist, and the ghost-line device has to be rebuilt before it can be trusted. Opus
again for the content authoring, which is writing rather than conversion, and it is
worth splitting into one session per term.
