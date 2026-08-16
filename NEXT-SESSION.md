# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026

**All three surfaces are built. Term 2's content is poured. Three terms are
not.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. The live
  site is the **16 August** build; this session's 29 new pages are committed but
  **not pushed**. Ask before pushing.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- Last commit: `aed82e5 Pour the Term 2 lesson bodies`

| File | What it is |
| --- | --- |
| `PRODUCT.md` | Product truth. |
| `DIRECTION.md` | The direction contract, the rules, the anti-references, the fonts. |
| `DESIGN-NOTES.md` | What the hub and home are, what was ruled, what is still open. |
| `README.md` | How to build, how to author a lesson, what must never go on the site. |
| `build.py` | Reads `data/`, writes `docs/`. Standard library only. |
| `plots.py` | The four unit sheets at hub scale, plus the small stage plot. |
| `tools/extract_program.py` | Pulls the lesson skeleton out of the four unit programs. |
| `data/` | `site.json`, `course/course.json`, four `course/termN/term.json`. |
| `docs/` | Build output. Generated, never edited by hand. |
| `.impeccable/mocks/comp-d-thedesk.html` | Comp D, approved. Governs the lesson page only. |

## What was built this session

**Term 2 poured: 29 bodies, so all 30 inputs of Blues to Jazz have a page.**
Input 02 was left exactly as it was; it is the model comp D was approved on and
the other 29 are written to match it. The site is now 30 of 123.

**The house style for a body, now established across a whole term.** Match it
when pouring Terms 1, 3 and 4:

- `lead` is one sentence, the learning intention in the student's own words. It
  is also the page description and the line on the home desk plate, so it has to
  read alone.
- `clauses` are three, and the `kind` is a small controlled vocabulary. **In the
  room** and **With the band** describe what happens, in that order of scale.
  **On your own**, **In pairs** and **In flat.io** are addressed to the student
  as instructions. **Assessed** is used twice only, on the Part B lessons, for
  the fact that marking is happening while they play. Six kinds in 90 clauses; do
  not invent a seventh without a reason.
- `criteria` are short "I can" statements, usually two, split out of the
  program's single longer criterion. Reading level is a product constraint here,
  not a preference.
- `bring` is a short noun phrase from a fixed set: Headphones, Your instrument,
  Process log, Instrument and log, Instrument and printed parts, Headphones and
  log.
- `plot: band` is on the 14 lessons where the room is actually set up as a band,
  and off the 16 where it is not. A stage plot on a lesson spent at a screen
  would be decoration.
- `patched` is the program's resource list, numbered R1 up.

**The Term 2 repertoire is fully verified.** All seven picks went through the
full order before being written in: Apple explicitness flag, then oEmbed for a
live id on the right channel, then duration. All seven are `notExplicit` and all
seven have an id on the artist's official or Topic channel. **The ids are
recorded in the repertoire register, off this repo**, following the precedent
the barred-work rows set. Nothing on the site renders an id yet, so
putting them in `data/` would be inventing a field.

Two of the seven needed a judgement recorded with them: the Muddy Waters pick is
the 1954 Chess single rather than the live version the VEVO channel carries, and
the Charlie Parker pick is the 1952 quartet remake, because the 1945 Savoy master
has no upload on an official or Topic channel. The Fisk Jubilee Singers
recording of Wade in the Water is a **choice**, not a verification: the register
left that performer open, and Matthew can swap it.

## The actual next task

**Pour Term 1, Term 3 or Term 4. One term per session.**

93 of 123 inputs still have no authored body, so no page. They appear in the
input list, the multicore and the term table with no link, which is honest and
looks deliberate. The extractor's `steps`, `intention` and `criteria` are in the
**teacher's voice** and are not student-facing prose. Cost it as writing, not as
conversion. Term 2 took one session at Opus medium, including the repertoire
checks.

Term 3 is the one to do last or to do carefully: it carries the ATSI protocol
block and the two barred works.

## What is genuinely missing

- **93 lesson bodies**, as above. Term 1 (33), Term 3 (30), Term 4 (30).
- **17 of the 26 repertoire picks are still unverified**: 4 in Term 1, 8 in
  Term 3, 5 in Term 4. Nine are now done, the seven from this session plus the
  two that were already recorded. Every remaining track needs the full order
  before it goes into a lesson: **Apple explicitness flag, then oEmbed for a
  live id and the right channel, then duration.** That order, every time.
- **The two verified Term 3 unseen excerpts are barred from the site**, and
  **neither is named anywhere in this repository**, which is public. They live in
  `Music7-10_Y9_RepertoireRegister.md`, off this repo, and that is the only place
  they are written down. **Do not copy them into a note here to make it easier
  to follow.**
- **The Term 3 ATSI protocol block, Weeks 4 to 6, is deliberately empty** until
  Matthew selects through the school's consultation.
- **No AT4 exam paper.** Open on the program thread, not this one.
- **No DESIGN.md and no finish review.** The direction contract ends with
  "unreviewed and undocumented is unfinished". `DESIGN-NOTES.md` is a record of
  decisions, not a substitute for either.

## Decisions waiting on Matthew

1. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
2. **The lesson page carries three pieces of torn tape, not two** - the plate's
   two corner strips plus the rail's current row. Either the two corners count as
   one act of taping the plate down, or the build has been over budget since the
   first commit. Inherited from comp D. A ruling is owed at the finish review.
3. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both are
   already in pushed history. Same question as Year 8, smaller.
4. **New: the `artist` field in a `listen` entry is never rendered.** Comp D
   shows the title and a short meta only, and that is approved. It was tested
   this session: the meta is `white-space:nowrap`, so a performer's name in it
   squeezes the title onto three lines and reads worse. The workaround used in
   Term 2 is to name the performer in the clause prose where identification
   matters, which worked for the two roots-lesson recordings but does not scale
   to a lesson with five tracks. **Either the field goes, or the block gets a
   second line.** A ruling is owed at the finish review.

## The Year 8 repo

The previous handoff said `year8-music` had **the school's name** in it including
in served pages. **That was wrong.** the school's name, its initials and "high school" all
return zero on a word-boundary search across every blob in all 31 commits; the
apparent hits were substring and regex-wildcard noise.

The real leak was **the teacher's first name on all 105 served pages**, baked in
by `build.py`. Fixed forward to "the user", matching what this repo already does,
plus the same name out of `PRODUCT.md` and three source comments. Pushed, and
the live pages were checked: the name returns zero on every one of them.

**Why not rewrite the history:** it is his own first name, on his own resources,
published under an org called `Edwards-Resources` at `edwards-resources.github.io`.
The URL already says more than the comment did. Rewriting 31 published commits
buys nothing and costs a rewritten public history. Matthew's call, and it is
still open.

## Watch out for

- **`SH_X` in `plots.py` and `--core-inset` in `site.css` are both 5%.** Change
  one without the other and the multicore quietly stops reading as plugged into
  the sheet. Both files say so.
- **Nothing is drawn below the sheet's bottom edge.** Anything hanging below it
  opens a band of empty floor between the drawing and the strip and breaks the
  same device.
- **Ghost = the other three units, and nothing else.** `GHOST` is used in exactly
  one place in `plots.py`. Using it for a live element makes the device stop
  meaning anything.
- **Contrast is a product constraint here, not a style preference.** Every text
  pair in use passes AA. Check every new dimmed state on the black ground.
  `--hair` at `#313337` is 1.48:1 and is still an open question.
- **Two torn tape strips per page at most.** The hub spends two: the standing
  line and the taped channel. See the open ruling above for the lesson page.
- **The stencil face is not a heading face.** One CSS selector enforces it. Read
  as "the page's own subject name": the lesson title, the unit name, and on home
  the title of the lesson on the desk. Do not widen it further.
- **Elements of music, never "concepts of music".** Only the ten real outcome
  codes exist.
- **No school name anywhere in the repository**, and no student names, work or
  marks, ever. `noindex` on every page.
- **Never `git stash` in these repos** now that `docs/` is tracked build output.
- **The repo is public and git history is permanent.** Sweep any new file before
  **committing**, not just before pushing. **Ask Matthew before pushing.**

## Model and effort

**Opus, medium**, for the next term's pour: it is student-facing writing against
a registered program, the repertoire checks have a strict order that must not be
shortcut, and Term 2 fitted comfortably in one session at that setting.

If instead you are doing the finish review and DESIGN.md, **Opus, medium** as
well. It is a judgement pass over an approved contract, and there are now four
rulings queued for it.
