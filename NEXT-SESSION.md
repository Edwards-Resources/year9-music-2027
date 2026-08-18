# Next session: Year 9 Music 2027

## Where this stands, 18 August 2026 (later)

**Home's year section is rebuilt to unequal weight.** This was the last
open item from the finish review, and the one the THESIS had been naming
and refusing on its own front door since the site was built.

The year is now a stack in unit order, not four equal blocks in a row:

- The three units that are not live **fold to a line each** - chip, name,
  focus, assessment meta, and Taught or Ahead at the right.
- The live unit **opens in place** and carries its own thirty inputs on
  the multicore, under the 4px chalk keyline the rail uses for the page
  you have open, with the assessment line under a hairline below it.
- Nothing is lifted out of sequence, so the open block travels down the
  page as the year runs and the shape of the surface is itself a position
  statement.
- **No year-scale room was added**, which was the explicit half of the
  ruling. The multicore is reused rather than a second device invented.
- On home the strip's `--core-inset` is zeroed and replaced by a 38px
  gutter for the ruler's own label. `SH_X` and the hub's 5% are untouched
  and still one number in two files.

Verified in the browser at 1440, 1180 and 390. No console errors. At 390,
home, hub and lesson all report `scrollWidth == clientWidth`.

- Rebuilt clean: `python3 build.py` → 128 pages, 123 of 123 inputs authored.
- `DESIGN.md` and `DESIGN-NOTES.md` updated: the gap is closed in both, the
  keyline rule now says "a left inset on home's open unit", and the "Unit
  blocks (home)" section is rewritten as "The year stack (home)".
- **Committed as `a7c0ae6`. Not pushed** - the live site is still on
  `2edb548` until Matthew says to push.

## Next task

Pick from "What's left" below, in roughly this order of value:

1. **The four blueprint sheets** (`data/course/term2/term.json`, `built: false`)
   - now the only open item in `DESIGN.md`'s known gaps that this repo can
   close. Four rejected explains depend on them, and half the STORY block
   is unmet until they exist.
2. **No AT3 exam paper** - program thread, not this repo's build thread.
3. **Hoochie Coochie Man's harmonic rhythm** (T2 #02's `listen`) - not
   urgent, reads fine as a plain row without it.

## Model and effort recommendation

**Sonnet, medium** for the blueprint sheets - routine authoring against a
shape `term1`'s guide and `plots.py` already establish.

## Watch out for

Everything in the previous handoffs still applies: `SH_X` and the hub's
`--core-inset` both 5% (home's zero is a documented local override, not a
change to that pair), nothing below the sheet's bottom edge, `GHOST` means
the other three units and nothing else, contrast as a product constraint,
focus as tape-on-floor/ink-on-sheet, `assets/site.js` staying small and
working without it, two tape strips per page at most (home spends its two
on the desk plate's corner and the live channel), the stencil face never
used as a heading face, elements of music not "concepts of music", no
school name or student data anywhere, never `git stash` in this repo, the
390px-screenshot trap, `DESIGN.md` as the system of record, sweep before
committing not just before pushing, the register being generated, the
`.serve/` symlink setup for local preview (`course-sites` on port 8820
serves all four sites), and italics need `_underscores_`, not `*asterisks*`.

Two additions:

- **Editing `data/*.json` by round-tripping through `json.dump` reformats
  the whole file** (this repo's JSON is hand-set at 1-space indent). Insert
  new keys with a text edit at the existing indent, then validate with
  `python3 -c "import json; json.load(open(path))"` and rebuild.
- **The in-app browser caches `site.css` hard.** A rebuild will show new
  HTML against the old stylesheet and look like the CSS edit silently
  failed. Bust it in the page rather than reloading:
  `const s=document.querySelector('link[rel=stylesheet]'); s.href=s.href.split('?')[0]+'?cb='+performance.now()`.
  A `?v=` on the page URL does not do it.

## Decisions waiting on Matthew

1. **Push?** `a7c0ae6` is local. The live site does not have the home
   rebuild until it is pushed.
2. **The third work in T1 #04's cue sheet** still has no cue times (audio
   won't download). Four or five, set with the recording playing.
3. **Rewrite `year8-music`'s published history?** Recommendation: no. It's
   his own name on his own resources at his own org.
4. **`DIRECTION.md` and the comp D sidecar name Matthew**, already in
   pushed history. Same question as Year 8, smaller.
5. **Should the player break out of the 240px listen block?** One line
   either way, Matthew's call since he's the one projecting it.

## The leak that keeps recurring

Same standing warning as every recent handoff: **this file is the one place
in the repo that has to discuss what must not be on the site, in order to
warn about it.** Swept before this commit: no school name, no student
names, no repertoire named in the T3 Weeks 4-6 sense, and the two barred
works are not named here either. This session added no content, only
layout, so nothing new was written that could carry a name.

## Last commit

`a7c0ae6 Rebuild home's year section to unequal weight` (local, not pushed)
