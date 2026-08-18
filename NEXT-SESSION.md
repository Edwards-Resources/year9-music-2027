# Next session: Year 9 Music 2027

## Where this stands, 18 August 2026

**The `worked` block is designed, built, documented and rendered.** It is
called **two takes** on the page. T3 #09 carries the exemplar. The two
remaining ones, T1 #26 and T4 #19, are authoring against a fixed shape and
are the next task.

- Live at **https://edwards-resources.github.io/year9-music-2027/**, but this
  session's commit is **not pushed**. Ask before pushing.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- This session's commit: `ef2af30` "Design the worked block into the world:
  two takes". One commit behind the live site.
- Vault session log written: `Session Logs/2026/Year 9 The Worked Block
  Designed.md`, linked in `_index.md`. The previous session's log was already
  there despite the last handoff saying otherwise.

## What the block is

The same task answered twice, once so it earns and once so it does not. Read
`DESIGN.md`'s "The read: the cue sheet, the long version and the two takes"
before touching any of it; the short version:

- Third read block, after `guide` and `explain`, in that order fixed in
  `build.py`. A section of the document, not a fourth clause.
- The label row carries the mark value joined by a middot, the way the plate's
  own header line already carries a count and a status.
- **Both specimens are marked with the world's two line weights**: 4px painted
  keyline bounds the take that works, 1px sheet rule draws the one that does
  not, same 18px inset, with the label above each saying it in words too. No
  fill and no tint; the sheet takes no colour.
- **A rung is a clause**: a named move with a sentence under it, in the same
  46px gutter. Verified to land on the clause gutter's exact pixel at 390,
  620, 760, 980 and 1100.
- The failing take is **not dimmed and not folded away**, deliberately and
  unlike Year 10's.
- `assert_worked_complete()` fails the build if either take is incomplete.
  Proven by mutation. Two takes means two.
- **No `site.js` change.** Nothing in this block is pressed. The last handoff
  expected a change here and there isn't one.

## The next task: two worked blocks

Data shape is in `README.md` under "The read". Copy the register from T3 #09
in `data/course/term3/term.json`, which is the exemplar.

**T1 #26, the process log opens.** The distinction is **a record against a
diary**. The task is a log entry rather than an exam answer, so `marks` is
omitted and the rungs are the task's own moves, not ALARM's: name what was
tried, say what changed, give the reason. The failing take should be a real
diary entry, the kind students actually write ("worked on my song today, it
sounds better now"), not a lazy one.

**T4 #19, the 250-word rationale.** The distinction is **naming a decision
against describing a feeling**. 250 words is too long to print twice, so the
task should be **one decision at about sixty words**, which is the lesson's
own four-decisions-at-sixty-words plan, and the block says so. Rungs are the
rationale's moves: name the decision, say what it does, connect it to the
brief. Marks come off the AT4 criteria; **do not invent a weighting or a
criterion wording that has not been read.** If a real figure is not to hand,
omit `marks` rather than guess it.

Both: write the failing take at the length students actually write, and make
it one that **looks fine**. An obviously lazy answer teaches nothing, and it
is the whole reason this block exists rather than an explain.

## What's left after that

1. **The four blueprint sheets still don't exist** (unchanged for several
   handoffs) - `data/course/term2/term.json` holds them at `built: false`, no
   other term has any, and four rejected explains depend on them existing
   somewhere.
2. **No AT3 exam paper.** On the program thread, not this one.
3. **Home's four unit blocks, unequal weight.** Half a session with Opus. The
   one arrangement the THESIS names and refuses is still on the page.
4. **The third work in T2 #02's `listen`, Hoochie Coochie Man**, could get its
   own guide entry if someone works out its harmonic rhythm by ear. Not
   urgent; it reads fine as a plain `listen` row.

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
named here either. T3 #09's worked block names no work at all - it says "the
excerpt", which is what an examination paper says, and that is the safest
default for the two still to be written.

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
preview (`course-sites` on port 8820 serves all four sites), and **italics need
`_underscores_`, not `*asterisks*`**.

Three additions from this session:

- **The preview server caches `site.css` hard.** Editing the stylesheet and
  reloading shows the old rules and looks exactly like a CSS bug. Bust it with
  a query string on the `<link>` href before believing any measurement or
  screenshot. This cost two false readings.
- **A new list inherits the container's width, and the container is wider than
  the reading measure everywhere in this plate.** The rung rules ran to the
  plate's full width on first build, crossing empty sheet, which is the same
  fault the cue sheet was held to 66ch to avoid. Set a measure on anything
  ruled.
- **`DESIGN.md`'s known-gaps list goes stale first**, because it is written at
  a moment and read as current. Two lines in it still said one explain and one
  guide existed. Check it against reality whenever you write into it.

## Model and effort

**Sonnet, medium** for the two remaining worked blocks. Routine authoring
against a fixed, small shape with a rendered exemplar to match, same register
as the explains and T3 #09.

**Opus, medium** for home's unequal-weight rebuild, unchanged.

**Sonnet, medium** for the four blueprint sheets when they're written,
unchanged.
