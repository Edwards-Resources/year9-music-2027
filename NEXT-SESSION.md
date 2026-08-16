# Next session: Year 9 Music 2027 site

## Where this stands, 16 August 2026 (late)

**All three surfaces are built. The content is not.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**, and the live
  site is this session's work. Pushed and **verified against the live URL**, not
  against the push: home, all four term hubs, the lesson page and the stylesheet
  all return 200, and the four unit sheets are serving.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main` `/docs`.
- Last commit: `5cac94a Point the handoff at the content pour`

| File | What it is |
| --- | --- |
| `PRODUCT.md` | Product truth. |
| `DIRECTION.md` | The direction contract, the rules, the anti-references, the fonts. |
| `DESIGN-NOTES.md` | **New.** What the hub and home are, what was ruled, what is still open. |
| `README.md` | How to build, how to author a lesson, what must never go on the site. |
| `build.py` | Reads `data/`, writes `docs/`. Standard library only. |
| `plots.py` | **New.** The four unit sheets at hub scale, plus the small stage plot. |
| `tools/extract_program.py` | Pulls the lesson skeleton out of the four unit programs. |
| `data/` | `site.json`, `course/course.json`, four `course/termN/term.json`. |
| `docs/` | Build output. Generated, never edited by hand. |
| `.impeccable/mocks/comp-d-thedesk.html` | Comp D, approved. Governs the lesson page only. |

## What was built this session

**The term hub.** Unit head and where the class is, the unit's sheet at full
width, the multicore running out of its bottom edge, the assessment bar, the
blueprint, and the full input list as a table.

**The home surface.** The lesson on the desk as a taped plate with the way in,
then the year as four units. No plan drawing; the sheet is already large on the
hub and small on a lesson page.

**The ghost layer, rebuilt.** 26 percent instead of comp B's 7 to 10, and the
**dash** rather than the fade carries "not live". Drawn as a bracket, not a
rectangle. See `DESIGN-NOTES.md`.

**The four drawings were replaced.** This is the thing to read `DESIGN-NOTES.md`
about before touching them. The first version drew all four units as one floor
plan wearing four costumes, and it read as music-adjacent nonsense — a band
standing on a 12-bar chord progression taped across the floor, which is time
drawn as floor space. Each unit is now the document its musicians actually use:
stage plot, chord chart, listening set-up, cue sheet. The lesson page's small
drawing got the same fix.

## The actual next task

**The content pour. One session per term, and it is writing rather than
conversion.**

122 of 123 lessons have no authored body, so they have no page. They appear in
the input list, the multicore and the term table with no link, which is honest
and looks deliberate. The extractor's `steps`, `intention` and `criteria` are in
the **teacher's voice** and are not student-facing prose. Cost it as writing.

Start with Term 2, since input 02 is already authored and is the model to match.

## What is genuinely missing

- **122 lesson bodies**, as above.
- **No verified YouTube ids for 24 of the 26 repertoire picks.** The two verified
  ones are **barred from the site** because they are the Term 3 unseen excerpts,
  and **neither is named anywhere in this repository**, which is public. They
  live in `Music7-10_Y9_RepertoireRegister.md`, off this repo, and that is the
  only place they are written down. **Do not copy them into a note here to make
  it easier to follow.** Every other track needs the full order before it goes
  into a lesson: Apple explicitness flag, then oEmbed for a live id and the right
  channel, then duration. That order, every time.
- **The Term 3 ATSI protocol block, Weeks 4 to 6, is deliberately empty** until
  Matthew selects through the school's consultation.
- **No AT4 exam paper.** Open on the program thread, not this one.
- **No DESIGN.md and no finish review.** The direction contract ends with
  "unreviewed and undocumented is unfinished". `DESIGN-NOTES.md` is a record of
  this session's decisions, not a substitute for either.

## Decisions waiting on Matthew

1. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
2. **The lesson page carries three pieces of torn tape, not two** — the plate's
   two corner strips plus the rail's current row. Either the two corners count as
   one act of taping the plate down, or the build has been over budget since the
   first commit. Inherited from comp D, not introduced this session. A ruling is
   owed at the finish review.
3. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both are
   already in pushed history. Same question as Year 8, smaller.

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
  one place in `plots.py`. Using it for a live element (the stereo field was, at
  first) makes the device stop meaning anything.
- **Contrast is a product constraint here, not a style preference.** Every text
  pair in use passes AA. Check every new dimmed state on the black ground.
  `--hair` at `#313337` is 1.48:1 and is still an open question from last session.
- **Two torn tape strips per page at most.** The hub spends two: the standing
  line and the taped channel. See the open ruling above for the lesson page.
- **The stencil face is not a heading face.** One CSS selector enforces it. This
  session read the third slot as "the page's own subject name", which added the
  desk plate's lesson title on home. Do not widen it further.
- **Elements of music, never "concepts of music".** Only the ten real outcome
  codes exist.
- **No school name anywhere in the repository**, and no student names, work or
  marks, ever. `noindex` on every page.
- **Never `git stash` in these repos** now that `docs/` is tracked build output.
- **The repo is public and git history is permanent.** Sweep any new file before
  **committing**, not just before pushing. **Ask Matthew before pushing.**

## Model and effort

**Opus, medium**, for the content pour: it is student-facing writing against a
registered program, not conversion, and the repertoire checks have a strict order
that must not be shortcut. Split it one session per term.

If instead you are doing the finish review and DESIGN.md, **Opus, medium** as
well — it is a judgement pass over an approved contract, and there are three
rulings already queued for it.
