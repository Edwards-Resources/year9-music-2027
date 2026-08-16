# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026

**All three surfaces are built. Terms 1 and 2 are poured. Terms 3 and 4 are
not.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. The live
  site is still the **16 August** build; the Term 2 pour and this session's
  Term 1 pour are both committed and **not pushed**. Ask before pushing.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- Last commit: `5a012f0 Pour the Term 1 lesson bodies`

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

**Term 1 poured: 33 bodies, so all 33 inputs of Like a Version have a page.**
The site is now 63 of 123. Written to the house style the Term 2 pour set, and
that style now holds across two whole terms, so treat it as settled rather than
as a Term 2 habit:

- `lead` is one sentence, the learning intention in the student's own words. It
  is also the page description and the line on the home desk plate, so it has
  to read alone.
- `clauses` are three, from six kinds and no more. Across 63 lessons the split
  is now In the room 92, On your own 47, With the band 24, In flat.io 16,
  In pairs 6, Assessed 4.
- **In the room** and **With the band** describe what happens; the other four
  are addressed to the student as instructions. Order them by what actually
  happens first in the lesson, not by scale. Term 2's input 25 already put
  **With the band** ahead of **In the room**, and three Term 1 lessons needed
  the same, because a clause that says "which of those changes would you keep"
  cannot come before the clause that made the changes.
- **Assessed** is spent twice per term, on the lessons where marks are being
  taken while the student plays. In Term 1 that is inputs 22 and 23, the two
  AT1 performance days. The clause carries the marking fact only, not the
  lesson.
- `criteria` are short "I can" statements, usually two, split out of the
  program's single longer criterion. Reading level is a product constraint.
- `bring` is a short noun phrase from the fixed set: Headphones, Your
  instrument, Process log, Instrument and log, Instrument and printed parts,
  Headphones and log. Term 1 used five of the six.
- `plot: band` is on the **15** Term 1 lessons where the room is genuinely set
  up as a band, against Term 2's 14. Higher is correct here: Term 1 is the
  performance unit. It is off every lesson spent at a screen.
- `patched` is the program's resource list, numbered R1 up.

**The Term 1 repertoire is fully verified.** All four picks went the full order
before being written in: Apple explicitness flag, then oEmbed for a live id on
the right channel, then duration. All four are `notExplicit` and all four sit
on an official or Topic channel. **The ids are in the repertoire register, off
this repo**, following the Term 2 precedent.

Two carry a judgement recorded with them. The U2 and Kidjo picks are the
Topic-channel album masters rather than the official video uploads, because
those uploads are a 4-second and an **84-second** edit respectively, and both
lessons need the whole recording. The Kidjo gap is the one that mattered.

**Input 10 has no Listen block on purpose.** It is the cover-versus-original
lesson and the register holds no verified pair for it. An unverified track put
on the site to fill a panel is exactly what the verification order exists to
stop. The clause prose carries the lesson without naming a pair.

## The actual next task

**Pour Term 3 or Term 4. One term per session.**

60 of 123 inputs still have no authored body, so no page. They appear in the
input list, the multicore and the term table with no link, which is honest and
looks deliberate. The extractor's `steps`, `intention` and `criteria` are in
the **teacher's voice** and are not student-facing prose. Cost it as writing,
not as conversion. Term 1 took one session at Opus medium, 33 bodies plus four
repertoire checks, and had room to spare.

**Do Term 4 next and Term 3 last.** Term 3 carries the ATSI protocol block and
the two barred works, and it has eight repertoire picks against Term 4's five.
Nothing about Term 4 is blocked.

## What is genuinely missing

- **60 lesson bodies.** Term 3 (30), Term 4 (30).
- **13 of the 26 repertoire picks are still unverified**: 8 in Term 3, 5 in
  Term 4. Thirteen are now done. Every remaining track needs the full order
  before it goes into a lesson: **Apple explicitness flag, then oEmbed for a
  live id and the right channel, then duration.** That order, every time. Where
  an official video upload turns out to be an edit, take the Topic-channel
  master and record why, as Terms 1 and 2 both now do.
- **The two verified Term 3 unseen excerpts are barred from the site**, and
  **neither is named anywhere in this repository**, which is public. They live
  in `Music7-10_Y9_RepertoireRegister.md`, off this repo, and that is the only
  place they are written down. **Do not copy them into a note here to make it
  easier to follow.**
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
   two corner strips plus the rail's current row. Either the two corners count
   as one act of taping the plate down, or the build has been over budget since
   the first commit. Inherited from comp D. A ruling is owed at the finish
   review.
3. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both
   are already in pushed history. Same question as Year 8, smaller.
4. **The `artist` field in a `listen` entry is never rendered, and the case for
   deleting it is now stronger.** Comp D shows the title and a short meta only,
   and that is approved. The meta is `white-space:nowrap`, so a long performer
   name in it squeezes the title onto three lines. Term 1 input 04 tested the
   third workaround and it is the good one: where the artist name is short, put
   it in `meta` and let it do the identifying. The Beatles, U2 and Adele all
   render on one line beside their titles. Term 2 input 17 had already done
   this with Ellington and Parker. So identification is being carried by `meta`
   or by clause prose in all 63 pages and `artist` has never once been read.
   **Recommendation: the field goes at the finish review.** A second line in
   the block is the alternative and nobody has needed it yet.

## The Year 8 repo

The previous handoff said `year8-music` had **the school's name** in it
including in served pages. **That was wrong.** the school's name, its initials and "high
school" all return zero on a word-boundary search across every blob in all 31
commits; the apparent hits were substring and regex-wildcard noise.

The real leak was **the teacher's first name on all 105 served pages**, baked
in by `build.py`. Fixed forward to "the user", matching what this repo already
does, plus the same name out of `PRODUCT.md` and three source comments. Pushed,
and the live pages were checked: the name returns zero on every one of them.

**Why not rewrite the history:** it is his own first name, on his own
resources, published under an org called `Edwards-Resources` at
`edwards-resources.github.io`. The URL already says more than the comment did.
Rewriting 31 published commits buys nothing and costs a rewritten public
history. Matthew's call, and it is still open.

## Watch out for

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
  `--hair` at `#313337` is 1.48:1 and is still an open question.
- **Two torn tape strips per page at most.** The hub spends two: the standing
  line and the taped channel. See the open ruling above for the lesson page.
- **The stencil face is not a heading face.** One CSS selector enforces it.
  Read as "the page's own subject name": the lesson title, the unit name, and
  on home the title of the lesson on the desk. Do not widen it further.
- **Elements of music, never "concepts of music".** Only the ten real outcome
  codes exist.
- **No school name anywhere in the repository**, and no student names, work or
  marks, ever. `noindex` on every page.
- **Never `git stash` in these repos** now that `docs/` is tracked build output.
- **The repo is public and git history is permanent.** Sweep any new file before
  **committing**, not just before pushing. **Ask Matthew before pushing.**
- **The register is generated.** `Music7-10_Y9_RepertoireRegister.md` says so at
  the top. Verification records go into
  `School Master/Tools/y9_repertoire_register.py` and the generator is re-run;
  editing the markdown by hand is thrown away on the next run.
- **`.claude/launch.json` in this repo points at a dead scratchpad directory**
  from the session that wrote it, and its port is usually already taken by
  another chat's server. Serving the build needs a directory whose child is
  named `year9-music-2027`, because `base` is `/year9-music-2027`. This session
  used a symlink in its own scratchpad and a config named `year9-t1` in the
  School Master root `.claude/launch.json`.

## Model and effort

**Opus, medium**, for the next term's pour: it is student-facing writing
against a registered program, the repertoire checks have a strict order that
must not be shortcut, and Terms 1 and 2 each fitted comfortably in one session
at that setting.

If instead you are doing the finish review and DESIGN.md, **Opus, medium** as
well. It is a judgement pass over an approved contract, and there are four
rulings queued for it.
