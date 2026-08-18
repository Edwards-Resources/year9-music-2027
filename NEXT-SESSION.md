# Next session: Year 9 Music 2027

## Where this stands, 18 August 2026 (later still)

**The four blueprint sheets are built.** This was the last open item in
`DESIGN.md`'s known gaps and the last unmet half of STORY: a student can now
get back to the progression, the voicings, the pattern and the rules at their
own address, `{term}/blueprint/{slug}/`, not just inside a lesson.

- `plots.py` gained a `blueprint(slug)` dispatcher and four drawing
  functions: `bp_progression` (the 12-bar frame in roman numerals, F-key
  chords written small underneath, the movable half of the pair unit2's hub
  chart already draws concretely), `bp_voicings` (three four-note dominant
  7th stacks, root to ♭7, for I7/IV7/V7), `bp_drum_pattern` (one bar of swing
  on a 12-unit triplet grid: ride, snare backbeat, hi-hat on 2 and 4), and
  `bp_walking_bass` (an 8-note excerpt over the form's first change, F7 to
  B♭7, root on the change and a semitone approach into it).
- **They are drawn in ink on sheet, not chalk on floor**, which is the one
  real bug this session hit and fixed: the first pass reused `CHALK`/`DIM`
  and the roman numerals and header text were invisible (near-white on
  near-white) until switched to `BP_INK`/`BP_DIM`, the same ground
  `small_stage()` already draws on. **Two Grounds Rule, not spotted from
  reading DESIGN.md alone** — it only bit because the blueprint sheet lives
  inside the plate and the four unit sheets it borrows the corner-label habit
  from live on the floor. Verified by grepping the built SVGs for `fill=`;
  none carry `#F2F1EC` or `#8E8F8B` any more.
- `build.py` gained `blueprint_page()` (the plate with no rider and no meta
  row: title block straight to the drawing, straight to a `read`-shaped rules
  block) and wired it into `main()`'s per-term loop. `rail()` gained a
  `reading_bp` parameter so the current sheet gets the same 4px keyline a
  lesson row gets, on the railfoot link rather than a channel.
- `data/course/term2/term.json`'s four blueprint entries are `built: true`
  with a `deck` sentence and a `rules` list each, hand-edited at the file's
  1-space indent (not round-tripped through `json.dump`).
- `assets/site.css` gained `.titleblock.bp`, `.bpsheet` and `.railfoot
  a.reading`; `.bprules` reuses the `.read` family the guide/explain/worked
  blocks already carry, so no new prose styling was needed.
- `DESIGN.md` and `DESIGN-NOTES.md` updated: the known-gap entry is closed
  with strikethrough, and a new **The blueprint sheet** component entry sits
  under **The unit sheets** in DESIGN.md, naming the ink-not-chalk departure
  explicitly so it doesn't get re-broken by a future edit that copies a unit
  sheet function as a starting point.
- Rebuilt clean: `python3 build.py` → 132 pages (128 + 4), 123 of 123 inputs
  still authored. Verified in the browser: all four sheets render correctly
  on desktop and at 390 with no horizontal overflow; the hub's blueprint bar
  and every term 2 lesson's rail foot now link to all four sheets with no
  `not on the site yet` line left anywhere in `docs/`.
- **Committed and pushed as `99ff4ec`.** The live site now has all four
  blueprint sheets.

## Next task

Nothing left in `DESIGN.md`'s known gaps closes from inside this repo except
the two below, which are smaller. Pick from "What's left":

1. **No AT3 exam paper** — program thread, not this repo's build thread.
   Needs Matthew's AT3 materials before there is anything to build against.
2. **Hoochie Coochie Man's harmonic rhythm** (T2 #02's `listen`) — not
   urgent, reads fine as a plain row without it.
3. Otherwise: **general content review** now that the site is functionally
   complete (123 of 123 lessons, all four blueprint sheets). A read-through
   for tone, factual slips, and whether the drum-pattern/walking-bass content
   in this session matches what Matthew actually teaches (it was authored
   from the term's own lesson text and PRODUCT.md, not from a lesson plan he
   supplied, so it is worth his eyes before students see it) would be more
   valuable than new build work.

## Model and effort recommendation

**Sonnet, low** for a first pass reviewing this session's blueprint content
against what's actually taught — reading and flagging, not building.
**Opus, medium** only if the review turns up a genuine musical or pedagogical
correction that needs rethinking rather than a wording fix.

## Watch out for

Everything in the previous handoffs still applies: `SH_X` and the hub's
`--core-inset` both 5% (home's zero is a documented local override), nothing
below the sheet's bottom edge, `GHOST` means the other three units and
nothing else, contrast as a product constraint, focus as
tape-on-floor/ink-on-sheet, `assets/site.js` staying small and working
without it, two tape strips per page at most, the stencil face never used as
a heading face, elements of music not "concepts of music", no school name or
student data anywhere, never `git stash` in this repo, the 390px-screenshot
trap, `DESIGN.md` as the system of record, sweep before committing not just
before pushing, the register being generated, the `.serve/` symlink setup for
local preview (`course-sites` on port 8820 serves all four sites), and
italics need `_underscores_`, not `*asterisks*`.

One addition this session, worth promoting to a standing rule for `plots.py`:

- **A drawing's colour comes from its ground, not from the file it lives in.**
  `plots.py` now carries two colour pairs, `CHALK`/`DIM` for the floor and
  `BP_INK`/`BP_DIM` for the sheet, and every new drawing function has to pick
  the right one by asking where the `<svg>` will actually sit in the page,
  not by copying the nearest existing function. This bit once already; it
  will bite again if a fifth blueprint-style sheet or a small-plate variant
  gets added by copy-paste from `unit2()` instead of from `small_stage()` or
  `bp_progression()`.

The two still-open items from last session's leftovers, unchanged:

- **Editing `data/*.json` by round-tripping through `json.dump` reformats the
  whole file.** Insert new keys with a text edit at the existing indent, then
  validate with `python3 -c "import json; json.load(open(path))"` and
  rebuild.
- **The in-app browser caches `site.css` hard.** Bust it in the page rather
  than reloading, or just open a fresh tab, which is what worked reliably
  this session when a reused tab started returning stale
  `innerWidth`/screenshot state after a scroll.

## Decisions waiting on Matthew

1. **The blueprint content itself.** The drum pattern, the voicings and the
   walking bass excerpt are musically standard but were authored from the
   term's own lesson text rather than from a lesson plan or notation Matthew
   supplied. Worth his read before Week 5 (input 13, comping and voicings)
   and Week 4 (input 12, walking bass) arrive.
2. **The third work in T1 #04's cue sheet** still has no cue times (audio
   won't download). Four or five, set with the recording playing.
3. **Rewrite `year8-music`'s published history?** Recommendation: no.
4. **`DIRECTION.md` and the comp D sidecar name Matthew**, already in pushed
   history. Same question as Year 8, smaller.
5. **Should the player break out of the 240px listen block?** Matthew's call.

## The leak that keeps recurring

Same standing warning as every recent handoff: **this file is the one place
in the repo that has to discuss what must not be on the site, in order to
warn about it.** Swept before this session's commit: no school name, no
student names, no repertoire named in the T3 Weeks 4-6 sense, and the two
barred works are not named here either. This session's new content (the
blueprint sheets) names only chord letters, roman numerals, note names and
drum stems, none of which are the leak this note exists to catch.

## Last commit

`99ff4ec Build the four blueprint sheets: progression, voicings, pattern,
rules` (pushed; the live site has it).
