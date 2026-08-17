# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026 (night)

**Both read blocks are designed, built and documented. `explain` and `guide`
exist in `build.py`, in the CSS, in `site.js` and in `DESIGN.md`, and Term 1
input 04 carries a real one of each. The next task is writing the other 34
explains and three guides, which is authoring against a settled shape.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. The live
  site is the 17 August push; the repo is now six commits ahead of it.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- The work commits are `7e88582 Embed the verified repertoire in the listen
  block` and the read-block commit above it. **None pushed.**
- Session write-ups in the vault at `projects/School Master/Session Logs/2026/`:
  `Year 9 Repertoire Embedded and the Listen Player.md`, `Year 9 Lesson Depth
  Triage.md`, `Year 9 Finish Review and DESIGN.md`, and one per term pour. All
  linked from that folder's `_index.md`. **This session is not yet written up.**

### What the two blocks are

Read the new section of `DESIGN.md` (**The read: the cue sheet and the long
version**) before writing either. The short version:

- Neither is a fourth clause. Every clause `kind` names where the doing happens
  and there is no doing in either, so both are **sections of the document**,
  siblings of the title block and the keep block, opened by the same 2px ink
  rule and sitting on the plate's own left edge with their content in a 66ch
  column.
- **The long version** (`explain`): label, its own title, about 250 words.
- **The cue sheet** (`guide`): a list of works, each with the name as the player
  control and its cue times **in the 46px gutter the clause numbers use**, so one
  column of figures runs down the whole plate. Only the time is a link; the cue
  text stays text.
- The order on the page is guide then explain, fixed in `build.py` not in the
  data, because you hear a thing before you are told what it is.
- `.play` is no longer scoped to `.listen`: the name of a work is the control on
  both blocks, from one `play_link()`. **One player at a time on the page**, not
  one per block.
- `assert_no_doubled_work()` fails the build if a work is in both the cue sheet
  and the listen block on one page. Proven by mutation.

### Cue times are measured, and this is the constraint on the other three guides

A cue time is a claim about a recording and a wrong one fails in front of a
class. `tools/loop.py` is new: it pulls the chord grid out of the audio, finds
the loop length by self-similarity and finds where each pass starts. Input 04's
eight cue times came out of it. The check that it works is the tempo, and both
measured loops match their recording's published tempo.

**Two of that lesson's three works are cued. The third would not download at
all** (403 on every client tried), so it has no cues and stays in the listen
block, which is also the case that proves the guard. Adding it is a few minutes
for someone with the recording playing. Expect the same failure on some works in
the other three guides: when it happens, the cues wait for an ear rather than
being guessed at.

| File | What it is |
| --- | --- |
| `PRODUCT.md` | Product truth. |
| `DIRECTION.md` | The direction contract, the rules, the anti-references, the fonts. |
| `DESIGN.md` | The design system as built, with every ruling and every gap. **System of record for the design.** |
| `DESIGN-NOTES.md` | The build record for the hub and home. Says so at the top. |
| `LESSON-DEPTH-TRIAGE.md` | Which of the 123 inputs get book-work content, and which do not. Governs the pour. |
| `README.md` | How to build, how to author a lesson, the `explain` and `guide` data shapes, what must never go on the site. |
| `build.py` | Reads `data/`, writes `docs/`. Standard library only. |
| `assets/site.js` | The only script on the site. Unfolds a recording inside a listen row or a cue sheet's work, and seeks it from a cue time. One player at a time on the page. |
| `plots.py` | The four unit sheets at hub scale, plus the small stage plot. |
| `tools/extract_program.py` | Pulls the lesson skeleton out of the four unit programs. |
| `tools/loop.py` | **New.** Measures a chord loop off the audio: its length, and where each pass starts. Where a guide's cue times come from. Needs numpy and scipy, which the build does not. |
| `data/` | `site.json`, `course/course.json`, four `course/termN/term.json`. |
| `docs/` | Build output. Generated, never edited by hand. |
| `.impeccable/mocks/comp-d-thedesk.html` | Comp D, approved. Governs the lesson page only. |

## What the triage decided

Read `LESSON-DEPTH-TRIAGE.md` in full before writing anything. The short version:

**76 of 123 inputs are untouched** and stay lesson plans. Every practice,
rehearsal, performing, workshop, feedback, reflection, logging, assessment
sitting and issue-the-task lesson. Those pages were never broken.

| | Inputs | `explain` A | `explain` B | `guide` |
| --- | --- | --- | --- | --- |
| Term 1 | 33 | 7 | 5 | 1 |
| Term 2 | 30 | 7 | 3 | 1 |
| Term 3 | 30 | 11 | 4 | 1 |
| Term 4 | 30 | 9 | 1 | 1 |
| **Total** | **123** | **34** | **13** | **4** |

A-only is about **8,500 words**; A-and-B about 11,750. Year 10 ran 12 explains
across 28 inputs, which is 43 percent, so both options here are tighter per
input than the precedent.

**Matthew ruled, 17 August:**

1. **Four guides confirmed**, one per term: T1 #04, T2 #02, T3 #14, T4 #02.
2. **A only, with individual Bs promoted where a lesson really needs it.** The
   gate, so it cannot quietly reinflate to 47: **promote a B only when writing
   an A explain hits content that is not there** - a specific dependency, not a
   preference - and **name every promotion in the commit message** beside the A
   explain that forced it.
3. **T3 #14 is promoted before starting**, making it 35. It was the only one of
   the four guide lessons whose explain was marked B, which was an
   inconsistency in the triage rather than a judgement.

Most likely to be promoted once writing starts, on current reading: **T2 #15**
(drum notation, since Part A requires writing a drum part) and **T1 #01** (the
four ensemble roles, which three later explains lean on).

## The `worked` block, still unruled

**Does Year 9 get a `worked` block as well?** Asked on 17 August and not yet
ruled on. Cheaper now than when it was asked: the read section exists, so this
is a third block inside a settled frame rather than new composition. It is not more exposition: it is one exam
question, one full-mark answer, the reasoning broken into ALARM rungs, and **a
zero-mark answer that looks fine and is not**. The zero answer is the half that
does the work, and the whole block is cheaper than an explain, about 150 words.

Three inputs want one instead of 250 words of prose, and in all three the
lesson already contains a worked example that currently only happens out loud:

- **T3 #09**, students mark real anonymised responses and justify the mark
- **T4 #19**, a strong rationale read and marked, then a weak one
- **T1 #26**, a model log entry written together, then a weak one improved

Recommendation on file: **yes to `worked`, no to `check`**, since Year 9 has no
gapfill for `check` to answer. Year 10's `build.py` has both and is the
reference implementation, but the rendering has to be redesigned for this
world, not ported.

## The embed is done, 17 August 2026

Commit `7e88582`, **not pushed**. All 24 site-eligible picks are in `data/` as an
`embed` field and play in place: 35 rows across 20 lessons, 24 distinct works,
every id re-checked live through oEmbed with every channel matching the
register. The field is called `embed`, not `id`, matching the three sibling
sites. The two barred excerpts stayed off the site and out of the repo.

**The name of the work is the control.** A 24px button in its own column was
built first and cost the work's name 34px in a 240px block, which put all three
of Term 4 input 08's titles onto two lines each. `assets/site.js` is new and is
the only script on the site: it folds the recording into the row, one player at
a time per block, and it takes a start time **because that is the seam the
guide's cue table plugs into**. With scripting off the row is still a link to
the recording. Both rulings are in `DESIGN.md`, in a rewritten listen-block
section.

Focus inside the plate is now ink rather than the term's tape, because tape on
the sheet runs 1.01 to 1 in Term 1 and 1.20 in Term 4 and this block put the
first focusable element on the sheet. Also in `DESIGN.md`.

Three things noticed and deliberately not changed, all needing Matthew's eye
rather than a session's judgement:

- **The player is 210px wide**, inside the 240px block inside the 300px spec
  column. It works and the recording sits under the work it names, but YouTube's
  own controls are cramped at that size. Whether it should break out of the
  column is a decision about the spec column, not about this block.
- **Term 1 input 04 reads "With or Without You / U2" then "U2" again.** `by()`
  suppresses the artist line when a word of the artist appears in the meta, but
  only for words longer than two characters, and the guard exists to stop short
  words matching spuriously. Pre-existing, one row.
- **`DESIGN.md` said the listen block's mono column was a duration**; it is the
  locating fact and always was. Corrected in passing. The register does carry a
  verified duration for all 24, so a duration column is available if wanted.

## The next task

**The remaining three guides, then the 34 explains.** Both shapes are settled and
rendered, so this is authoring rather than design. `LESSON-DEPTH-TRIAGE.md` says
which inputs get what and `README.md` carries both data shapes.

Guides first, for the same reason as last time: there are only three, each needs
`tools/loop.py` run against its works before a single time is written, and a
download failure on any of them is better found now than in the middle of the
explains. They are T2 #02, T3 #14 and T4 #02. **T3 #14 sits outside the Weeks 4
to 6 block on purpose and the block still carries no guide at all.**

Then the explains, in term order. The gate on promoting a B stands: promote only
when writing an A hits content that is not there, and name every promotion in the
commit message beside the A that forced it.

## What is still genuinely missing

- **No AT3 exam paper.** Open on the program thread, not this one. Earlier
  versions of this file called it AT4; AT3 is the aural paper and the one the
  notification promises, which is what `PRODUCT.md` records.
- **The four blueprint sheets do not exist**, so half the STORY block is unmet:
  a student cannot yet get back to the progression, the voicings and the rules.
  `data/course/term2/term.json` holds them at `built: false` and no other term
  has any, though `PRODUCT.md` says Term 4 supplies a timing sheet, a template
  and a bank of motifs. **The triage now depends on this**: four inputs were
  rejected for an explain on the grounds that a sheet is the right artefact for
  them, so if the sheets are never built, that content is nowhere.
- **No book-work content.** Triaged, ruled on, not written.

## Decisions waiting on Matthew

1. **Does Year 9 get a `worked` block?** Still open, and now cheaper than it was:
   the read section exists, so a `worked` block is a third block inside a
   settled frame rather than new composition. See above. **Recommendation: yes to
   `worked`, no to `check`.**
2. **The third work in input 04's cue sheet.** Its audio will not download, so it
   has no cue times. Four or five, set with the recording playing, and it joins
   the cue sheet and comes out of `listen`.
3. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
4. **Home's four unit blocks are equal weight**, which is the one arrangement
   the thesis names and refuses. The review's ruling is **unequal weight, not a
   drawing**: the live unit takes the block and carries its own inputs, the
   other three compress to a line each, which is the live/not-live logic the
   hub's ghost bracket already owns. A year-scale drawing was proposed and
   withdrawn, because a third instance of the sheet is the metaphor doing
   overtime, which `DESIGN-NOTES.md` had already ruled out once. Half a session
   with Opus.
5. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both are
   already in pushed history. Same question as Year 8, smaller.
6. **Whether to push.** The repo is six commits ahead of the live site. The embed
   and the first two read blocks are what a class would notice.
7. **Should the player break out of the 240px listen block?** It renders at
   210px and YouTube's own controls are cramped there. It is a decision about
   the spec column rather than about this block, and Matthew is the one
   projecting it in a room. One line either way.

Settled and no longer decisions: the push and history rewrite of 17 August; the
three torn strips are two acts of taping; the `artist` field is rendered rather
than deleted under a rule written into `DESIGN.md`; `bring` is a closed set of
seven and the seventh is recorded with its source; the guide count and the
A-with-promotion rule above; the listen block's player, the name-is-the-control
ruling and ink focus on the sheet, all three now in `DESIGN.md`.

## The leak that keeps recurring

The general lesson, recorded by three sessions running now: **the handoff file
is the thing that leaks**, because it is the only file in this repo that has to
discuss what must not be on the site in order to warn about it. **Naming a thing
to track its status is the same leak as naming it to prove its absence.** Sweep
this file hardest, every time, before **committing**.

The two barred works are unseen excerpts. They live in the register off this
repo and that is still the only place they are written down. **Do not copy them
into a note here.** Their absence is not silent: input 19 says the excerpt is
checked against the register beforehand, and input 23 describes the paper
without describing what is on it. Neither page carries a `repertoire` field.

`LESSON-DEPTH-TRIAGE.md` was swept before its commit: zero em dashes, no names,
no repertoire titles.

## The Year 8 repo

The 16 August handoff said `year8-music` had the school's name in it including
in served pages. **That was wrong**; the apparent hits were substring and
regex-wildcard noise. **Do not write the search terms out here to make that
claim checkable.** The 16 August handoff did, and in doing so put the school's
name into this public repo for the first time, in the one sentence documenting
its absence somewhere else. Fixed in history as well as forward.

The real leak was the teacher's first name on all 105 served pages, baked in by
`build.py`. Fixed forward to "the user", plus the same name out of `PRODUCT.md`
and three source comments. Pushed and verified on the live pages.

**Why not rewrite the history:** it is his own first name, on his own resources,
published under an org called `Edwards-Resources` at
`edwards-resources.github.io`. The URL already says more than the comment did.
Rewriting 31 published commits buys nothing and costs a rewritten public
history. Matthew's call, and it is still open.

## Watch out for

- **A blueprint sheet is not an explain.** A sheet holds the what, an explain
  holds the why. Four inputs were rejected on this ground, so writing an explain
  for them puts the sheet's content on the wrong page, in prose, twice.
- **No explain may name repertoire in the Term 3 Weeks 4 to 6 block.** T3 #11,
  #12 and #16 carry explains and all three must stay general. This is the single
  easiest place in the whole pour to leak a title.
- **`SH_X` in `plots.py` and `--core-inset` in `site.css` are both 5%.** Change
  one without the other and the multicore quietly stops reading as plugged into
  the sheet. Both files say so.
- **Nothing is drawn below the sheet's bottom edge.** Anything hanging below it
  opens a band of empty floor between the drawing and the strip and breaks the
  same device.
- **Ghost = the other three units, and nothing else.** `GHOST` is used in
  exactly one place in `plots.py`. Using it for a live element makes the device
  stop meaning anything.
- **Contrast is a product constraint here, not a style preference.** Every text
  pair in use passes AA. Check every new dimmed state on the black ground.
- **Focus is tape on the floor and ink on the sheet.** Tape on cream measures
  1.01:1 in Term 1 and 1.20:1 in Term 4, so anything focusable inside the plate
  needs the ink ring, which `.plate :focus-visible` already gives it. The
  general form of that trap: **a rule can be complete for every case that
  exists and wrong for the first new one.** An `explain` or a `guide` carrying a
  link is the next thing to land on the sheet.
- **`assets/site.js` is the only script and stays small.** Anything it does has
  to work without it: the listen row is a real link to the recording first and a
  player second, the rail is a `<details>` rather than a scripted toggle, and
  the guide's cue times must be real `watch?t=` links before they are seeks.
- **Two torn tape strips per page at most**, counting a corner pair as one act.
- **The stencil face is not a heading face.** One CSS selector enforces it.
  Read as "the page's own subject name": the lesson title, the unit name, and on
  home the title of the lesson on the desk. Do not widen it further.
- **Elements of music, never "concepts of music".** Only the ten real outcome
  codes exist.
- **No school name anywhere in the repository**, and no student names, work or
  marks, ever. `noindex` on every page.
- **Never `git stash` in these repos** now that `docs/` is tracked build output.
- **A 390px screenshot from headless Chrome on macOS is a lie.** Chrome will not
  render a window below about 400px wide, so `--window-size=390,H` renders a
  wider layout and crops the PNG to 390. It looks exactly like a broken mobile
  layout and cost one session a false review failure. Render the page in a
  **390px iframe inside a wider window** and capture that, or measure
  `documentElement.scrollWidth` against `clientWidth` in a 390px iframe.
- **`DESIGN.md` is the system of record for the design.** Read it before
  touching CSS, alongside `DIRECTION.md`. Most of its rules are held by review
  rather than by the build, so nothing will stop you breaking them.
- **The repo is public and git history is permanent.** Sweep any new file before
  **committing**, not just before pushing. **Ask Matthew before pushing.**
- **The register is generated.** Verification records go into
  `School Master/Tools/y9_repertoire_register.py` and the generator is re-run;
  editing `Music7-10_Y9_RepertoireRegister.md` by hand is thrown away next run.
- **Serving the build: stop making scratchpad symlinks.** `base` is
  `/year9-music-2027`, so a server has to be rooted at a directory whose child
  has that exact name. `Sites/.serve/` holds a permanent symlink to each of the
  four sites' `docs/`, and one config called **`course-sites` on port 8820**
  serves all four. `.serve/` sits above every repo, so nothing in it is
  committed or published.

  ```
  http://localhost:8820/year9-music-2027/
  ```

## Model and effort

**No model needed** to rule on the `worked` question. It is one decision and the
argument is in this file.

**Opus, medium** for designing `explain` and `guide` into this world, which is
the next task now the embed is in. Neither block type exists in `build.py`, the
Year 10 versions live in a different design system, and this is the first block
in the world that is read rather than done. A composition decision, not a port.
Start with `guide`: there are only four, the player they need now exists, and
one built guide settles the cue grammar before 35 explains commit to a shape.

**Sonnet, medium** for writing the 35 explains once the blocks exist. Routine
authoring against a settled, signed-off scope.

**Opus, medium** for home's unequal-weight rebuild. A composition decision on
the one surface that never had a comp, and the fix has to be looked at beside
the incumbent before it is kept.

**Sonnet, medium** for the four blueprint sheets when they are written. Authored
teaching material on an established page shape, not new design.
