# Next session: Year 9 Music 2027

## Where this stands, 18 August 2026

**All three `worked` blocks are now written.** T1 #26 (the process log opens,
a record against a diary), T3 #09 (the exemplar, marking a dot point against
the criteria) and T4 #19 (the 250-word rationale, naming a decision against
describing a feeling) all render. `assert_worked_complete()` passes for all
three. Every input the triage named in `LESSON-DEPTH-TRIAGE.md` now has its
content — nothing from that list is outstanding.

- Neither new block carries `marks`: no real AT4 criteria figure was to hand
  for T4 #19, and T1 #26's task (a log entry) has no mark value at all. Both
  omit the field rather than guess, per the design rule in `README.md`.
- Rebuilt clean: `python3 build.py` → 128 pages, 123 of 123 inputs authored.
- **Committed and pushed** as `2edb548`. Live site is now current with this
  work: **https://edwards-resources.github.io/year9-music-2027/**.
- Vault session log written: `Session Logs/2026/Year 9 The Two Remaining
  Worked Blocks.md`, linked in `_index.md`.

## Next task

No task is queued in the `worked`/`explain`/`guide` thread — it's complete.
Pick from "What's left" below, in roughly this order of value:

1. **The four blueprint sheets** (`data/course/term2/term.json`, `built: false`)
   — unchanged for several handoffs, four rejected explains depend on them.
2. **Home's four unit blocks, unequal weight** — half a session with Opus,
   the arrangement the THESIS names and refuses is still on the page.
3. **No AT3 exam paper** — program thread, not this repo's build thread.
4. **Hoochie Coochie Man's harmonic rhythm** (T2 #02's `listen`) — not urgent,
   reads fine as a plain row without it.

## Model and effort recommendation

**Sonnet, medium** for the blueprint sheets when tackled next — routine
authoring against a shape `term1`'s guide and `plots.py` already establish.
**Opus, medium** for home's unequal-weight rebuild — a design decision
against a named-and-refused arrangement, not mechanical authoring.

## Watch out for

Everything in the previous handoffs still applies: `SH_X` and `--core-inset`
both 5%, nothing below the sheet's bottom edge, `GHOST` means the other three
units and nothing else, contrast as a product constraint, focus as
tape-on-floor/ink-on-sheet, `assets/site.js` staying small and working without
it, two tape strips per page at most, the stencil face never used as a heading
face, elements of music not "concepts of music", no school name or student
data anywhere, never `git stash` in this repo, the 390px-screenshot trap,
`DESIGN.md` as the system of record, sweep before committing not just before
pushing, the register being generated, the `.serve/` symlink setup for local
preview (`course-sites` on port 8820 serves all four sites), and italics need
`_underscores_`, not `*asterisks*`.

One addition from this session: **editing `data/*.json` by round-tripping it
through `json.dump` reformats the whole file** (this repo's JSON is hand-set
at 1-space indent; Python's default is different) and turns a two-line
addition into a 4,000-line diff. Insert new keys with a text edit at the
existing indent instead, then validate with `python3 -c "import json;
json.load(open(path))"` and rebuild. Cost a wasted commit's worth of diff
this session before being caught and reverted.

## Decisions waiting on Matthew

1. **The third work in T1 #04's cue sheet** still has no cue times (audio
   won't download). Four or five, set with the recording playing.
2. **Rewrite `year8-music`'s published history?** Recommendation: no. It's his
   own name on his own resources at his own org.
3. **`DIRECTION.md` and the comp D sidecar name Matthew**, already in pushed
   history. Same question as Year 8, smaller.
4. **Should the player break out of the 240px listen block?** One line either
   way, Matthew's call since he's the one projecting it.

## The leak that keeps recurring

Same standing warning as every recent handoff: **this file is the one place in
the repo that has to discuss what must not be on the site, in order to warn
about it.** Swept before this commit: no school name, no student names, no
repertoire named in the T3 Weeks 4-6 sense, and the two barred works are not
named here either. Neither new worked block names a real work: T1 #26 talks
about "the intro" of an unnamed student song, T4 #19 about a fictional AT4
"boss theme" for the Level Up brief.

## Last commit

`2edb548 Write the two remaining worked blocks: T1 #26 and T4 #19` (pushed)
