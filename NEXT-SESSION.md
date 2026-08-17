# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026

**All three surfaces are built, all four terms are poured, the finish review is
closed, and the book-work triage is done and ruled on. The next task is the
embedding fix, which is now a prerequisite rather than a cleanup.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. The live
  site is the 17 August push; the repo has moved ahead of it since.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- Last commit: `fcf0769 Triage the book-work gap across all 123 inputs`. **Not
  pushed.**
- Session write-ups in the vault at `projects/School Master/Session Logs/2026/`:
  `Year 9 Lesson Depth Triage.md` (this session), `Year 9 Finish Review and
  DESIGN.md`, and one per term pour. All linked from that folder's `_index.md`.

| File | What it is |
| --- | --- |
| `PRODUCT.md` | Product truth. |
| `DIRECTION.md` | The direction contract, the rules, the anti-references, the fonts. |
| `DESIGN.md` | The design system as built, with every ruling and every gap. **System of record for the design.** |
| `DESIGN-NOTES.md` | The build record for the hub and home. Says so at the top. |
| `LESSON-DEPTH-TRIAGE.md` | **New.** Which of the 123 inputs get book-work content, and which do not. Governs the pour. |
| `README.md` | How to build, how to author a lesson, what must never go on the site. |
| `build.py` | Reads `data/`, writes `docs/`. Standard library only. |
| `plots.py` | The four unit sheets at hub scale, plus the small stage plot. |
| `tools/extract_program.py` | Pulls the lesson skeleton out of the four unit programs. |
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

## The one question still open

**Does Year 9 get a `worked` block as well?** Asked and explained; the session
ended before it was ruled on. It is not more exposition: it is one exam
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

## The next task, and why it moved

**Embed the verified repertoire.** This was filed last session as mechanical
cleanup. It is not: **the four guides are dead without it.** A cue table whose
timestamps cannot seek a player is a list of numbers. So the order is embed,
then guide, then the explains.

- `PRODUCT.md` names "the year's repertoire with embedded listening" as a
  must-carry and says audio and video are embedded from their host, never
  uploaded. `build.py` carries no `iframe` or embed code anywhere and the
  `listen` block is a plain text list: title, artist, duration.
- **All 26 repertoire picks across all four terms are fully verified with live
  ids**, sitting in `Music7-10_Y9_RepertoireRegister.md`. They were deliberately
  never written into `data/` because nothing rendered one yet.
- The work: add an `id` field per track across all four terms' `data/`, wire a
  player into the `listen` block in `build.py`, rebuild.

Two things the world already decides for the block design, before anyone opens
the CSS:

- An `explain` is sustained prose, and **long white prose never sits on the
  black field**, so it sits on the sheet. It is the first block in this world
  that is **read rather than done**, so it cannot take a clause `kind`.
- A `guide`'s timestamps are counts, and counts here are mono, like the input
  numbers on the rail. That grammar already exists.

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
- **Nothing is embedded.** See above; this is now the next task.
- **No book-work content.** Triaged, ruled on, not written.

## Decisions waiting on Matthew

1. **Does Year 9 get a `worked` block?** See above. **Recommendation: yes to
   `worked`, no to `check`.**
2. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
3. **Home's four unit blocks are equal weight**, which is the one arrangement
   the thesis names and refuses. The review's ruling is **unequal weight, not a
   drawing**: the live unit takes the block and carries its own inputs, the
   other three compress to a line each, which is the live/not-live logic the
   hub's ghost bracket already owns. A year-scale drawing was proposed and
   withdrawn, because a third instance of the sheet is the metaphor doing
   overtime, which `DESIGN-NOTES.md` had already ruled out once. Half a session
   with Opus.
4. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both are
   already in pushed history. Same question as Year 8, smaller.
5. **Whether to push.** The repo is several commits ahead of the live site.

Settled and no longer decisions: the push and history rewrite of 17 August; the
three torn strips are two acts of taping; the `artist` field is rendered rather
than deleted under a rule written into `DESIGN.md`; `bring` is a closed set of
seven and the seventh is recorded with its source; the guide count and the
A-with-promotion rule above.

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

**Sonnet, medium** for the embedding work, which is the next task: add an `id`
per track across all four terms' `data/`, wire a player into the `listen` block,
rebuild. Every id is already verified and sitting in the register, so this is
mechanical, but it gates the four guides.

**Opus, medium** for designing `explain` and `guide` into this world. Neither
block type exists in `build.py`, the Year 10 versions live in a different design
system, and this is the first block in the world that is read rather than done.
A composition decision, not a port.

**Sonnet, medium** for writing the 35 explains once the blocks exist. Routine
authoring against a settled, signed-off scope.

**Opus, medium** for home's unequal-weight rebuild. A composition decision on
the one surface that never had a comp, and the fix has to be looked at beside
the incumbent before it is kept.

**Sonnet, medium** for the four blueprint sheets when they are written. Authored
teaching material on an established page shape, not new design.
