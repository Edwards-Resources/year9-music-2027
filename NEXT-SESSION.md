# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026

**All three surfaces are built, all four terms are poured, and the finish review
is closed. The site is 123 of 123 inputs and the build is finished by its own
contract's definition.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. Pushed and
  checked against the live URL on 17 August 2026: home, `term3/index.html` and
  `term3/07/index.html` all return 200. All four terms are live and complete.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- Last pushed commit: `5d9f05e Record the commit line and the vault write-up in
  the handoff`. History from `2b40718` to `5d9f05e` was rewritten before this
  push to take an artist name out of one commit; see the leak note below.
- Session write-up in the vault at
  `projects/School Master/Session Logs/2026/Year 9 Finish Review and DESIGN.md`,
  linked from that folder's `_index.md`.
- Session write-up in the vault at
  `projects/School Master/Session Logs/2026/Year 9 Term 3 Content Pour.md`,
  linked from that folder's `_index.md`.

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
| `DESIGN.md` | The design system as built, with every ruling and every gap. Written at the finish review, 17 August 2026. |

## What the Term 3 pour built, the session before the review

### Term 3 poured

**30 bodies, so every input of every term now has a page.** The house style is
unchanged. Where Term 3 sits against the three terms that set it:

- **90 clauses, mean 19.6 words**, against 21.2 across the other three. Three
  clauses on every page, two success criteria on every page, two or three
  patched-in rows, as everywhere else.
- **Leads mean 12.2 words** against 12.5. Most are the program's learning
  intention verbatim, which is what the other terms do too.
- **`Assessed` is spent once**, on input 23, the only lesson where marks are
  taken. Same reading as Term 4: the practice paper in input 22 is sat under
  full conditions but is not a mark, so it does not get it.
- **`plot: band` is on six lessons**, the ones where the room is actually a band
  on the floor: the Week 2 performance, the two Week 6 performance lessons and
  the three arrangement workshops. Terms 1 and 2 were at 15 and 14, Term 4 at 1.
- **`In flat.io` is on one clause.** The unit names flat.io once, as the aural
  notebook that holds the weekly routine. Terms 1 and 2 together carried 16 and
  Term 4 carried 13, but this is a paper-and-pen examination term and writing
  more would be describing a different room.
- **Seven `listen` blocks, ten tracks.** Against 13 blocks and 22 tracks across
  the other three terms.

### The repertoire is now fully verified

**All nine outstanding Term 3 picks went the full order**: Apple explicitness
flag, then oEmbed for a live id on the right channel, then duration. All nine
came back clean and the ids are in the repertoire register, off this repo. Six
things came out of it that are worth carrying:

1. **Two titles in the register were wrong** and are corrected. One was missing
   its article and its feature credit; one had a singular where the released
   title is plural. Both were caught by the Apple lookup, which is an argument
   for doing the explicitness check first rather than treating it as a
   formality.
2. **Three of the nine sit on `- Topic` channels** where the official channel
   carries only an edit, a live version or a remix. Recorded with the reason
   each time, as the three poured terms already do.
3. **One sits on a label channel**, the band's own, which is the same reading as
   the Term 4 pick that sits on a film label's channel.
4. **The Week 6 art music pick's Topic channel is the conductor's**, not the
   orchestra's, which is how the auto-generated channels credit that recording.
   The duration matches the Apple master to the second, so it is the right
   recording under a surprising name. A second conductor's reading is recorded
   beside it in case the other is wanted.
5. **One track is not flagged by Apple but is pointed political writing**, and
   the Week 5 lesson is built on exactly that. The flag is recorded as what it
   is, along with a note that Matthew should hear it through before Week 5
   rather than treat a clean flag as the whole answer.
6. **The ninth pick was already verified**, but its record lived only in the
   register's Section 3 beside the ruling that freed the artist, which read from
   the forward table as an unverified pick. It is written out in both places now
   and was re-checked live today.

The register generator is `School Master/Tools/y9_repertoire_register.py` and it
has been re-run, so `Music7-10_Y9_RepertoireRegister.md` is current.

### The two barred works

**Neither is named on any page, and the count of barred works has not changed.**
Both are unseen excerpts, so naming them on a page the class can read is the one
thing that destroys them. They live in the register off this repo and that is
still the only place they are written down. **Do not copy them into a note here.**

Their absence is not silent. Input 19 says the excerpt is checked against the
register beforehand so that it is unseen in fact and not only in intention, and
input 23 describes the paper without describing what is on it. Neither page
carries a `repertoire` field, because naming even the area narrows the field for
a student reading ahead.

### The Weeks 4 to 6 block, written without filling it

The block has no named repertoire because the selection goes through the
school's consultation and has not been made. The pages say so, in the student's
own reading, on the page where it belongs: input 11's third clause says the
works are chosen through the school's consultation and are named in class once
that is done, and not before. Inputs 12, 13, 16, 17 and 26 then refer to "the
consulted repertoire" rather than working around a hole.

That is a teaching fact rather than an apology, and it is one the unit program
already makes: protocols come before the listening, and the consultation is part
of the protocols. None of the six pages carries a `listen` block, because there
is nothing to name yet. When Matthew makes the selection, those pages gain
`listen` blocks and nothing else about them needs to change.

### One new value in a closed set

**`bring: "Pens"` is new**, and it is on exactly two pages: the final practice
paper and AT3 itself. The previous six values are all instrument, log or
headphones, which are the right answers for a performing or composing term and
the wrong answer for a supervised written paper. The words are not invented:
the AT3 notification says "Bring pens. No notes, no devices." So the set is
seven now, the seventh comes from the school's own task notification, and it is
used only where a paper is sat under examination conditions.

## A leak that was settled before pushing

**Done, 17 August 2026.** One of the two barred works (the Week 7 excerpt) was
named by artist in the commit that first recorded the Term 2 repertoire
verification, in a sentence about the verification record rather than about the
work itself. It was never in `docs/`, so it was never served. The commit was
rewritten with `git rebase -i` (the artist reference replaced with
"the barred-work rows"), the whole 14-commit stack was replayed on top of it,
and the rewritten history was checked with `git log -p | grep` before pushing:
zero hits for the artist's name or the work's title anywhere in the pushed
history. All 15 commits, `2b40718` through `5d9f05e`, are now pushed and live.

The general lesson, recorded by two sessions running now: the handoff file is
the thing that leaks, because it is the only file in this repo that discusses
what must not be on the site. Sweep it hardest, every time, before committing.

## The finish review, 17 August 2026

**Done. `DESIGN.md` is written and the contract's FINISH block is satisfied.**
The review ran fresh against comp D, the contract and `PRODUCT.md`, and closed at
"fix". Six defects were fixed and rebuilt, three rulings were taken and recorded,
one item is left for Matthew. It is all in the commit message of `8214b06` and in
`DESIGN.md`; the short version:

- `--hair` went from 1.48:1 to 3.21:1, which closes the oldest open question in
  this repo. The meta row is now ruled to its field count. The `artist` field is
  rendered rather than deleted, but only where `meta` has not already said it.
  The four unbuilt blueprint sheets are one line instead of four dead labels.
  The hub's description moved below the unit name. The Outcomes header hides
  with its column at 390. The small stage plot's label no longer overprints a
  monitor wedge.
- **Mobile is proven at 390 for the first time**: `scrollWidth` equals
  `clientWidth` on all three surfaces. Note for whoever captures next: Chrome
  headless on macOS will not render below about 400px wide, so a
  `--window-size=390` screenshot is a wider layout cropped, not a mobile view.
  Render the page in a 390px iframe inside a wider window instead.
- `DESIGN.md` is now the system of record for the design. `DESIGN-NOTES.md`
  stays as the build record for the hub and home, and says so at the top.

## What is genuinely missing

- **No AT3 exam paper.** Open on the program thread, not this one. Earlier
  versions of this file called it AT4; AT3 is the aural paper and the one the
  notification promises, which is what `PRODUCT.md` records.
- **The four blueprint sheets do not exist**, so half the STORY block is unmet:
  a student cannot yet get back to the progression, the voicings and the rules.
  `data/course/term2/term.json` holds them at `built: false` and no other term
  has any, though `PRODUCT.md` says Term 4 supplies a timing sheet, a template
  and a bank of motifs. This is authoring work, not design work, and it is now
  the largest real gap in the site.

## Decisions waiting on Matthew

1. **Push?** Done, 17 August 2026. The site is live and complete.
2. **Rewrite the three unpushed commits?** Done, same session. See the leak note
   above.
3. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
4. **Home's four unit blocks are equal weight**, which is the one arrangement the
   thesis names and refuses. The review's ruling is **unequal weight, not a
   drawing**: the live unit takes the block and carries its own inputs, the other
   three compress to a line each, which is the live/not-live logic the hub's
   ghost bracket already owns. A year-scale drawing was proposed and withdrawn,
   because a third instance of the sheet is the metaphor doing overtime, which
   `DESIGN-NOTES.md` had already ruled out once. **This is the only design work
   left on the site.** Half a session with Opus.
5. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both are
   already in pushed history. Same question as Year 8, smaller.

Settled at the finish review and no longer decisions: the three torn strips are
two acts of taping; the `artist` field is rendered rather than deleted, under a
rule written into `DESIGN.md`; `bring` is a closed set of seven and the seventh
is recorded with its source.

## The Year 8 repo

The 16 August handoff said `year8-music` had **the school's name** in it
including in served pages. **That was wrong.** The school's name, its initials
and the words for a high school all return zero on a word-boundary search across
every blob in all 31 commits; the apparent hits were substring and
regex-wildcard noise.

**Do not write the search terms out here to make that claim checkable.** The
16 August handoff did, and in doing so it put the school's name into this public
repo for the first time, in the one sentence that was documenting its absence
somewhere else. That is fixed in history as well as forward.

The real leak was **the teacher's first name on all 105 served pages**, baked in
by `build.py`. Fixed forward to "the user", matching what this repo already
does, plus the same name out of `PRODUCT.md` and three source comments. Pushed,
and the live pages were checked: the name returns zero on every one of them.

**Why not rewrite the history:** it is his own first name, on his own resources,
published under an org called `Edwards-Resources` at
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
  layout and cost this session a false review failure. Render the page in a
  **390px iframe inside a wider window** and capture that, or measure
  `documentElement.scrollWidth` against `clientWidth` in a 390px iframe, which is
  the check that actually answers the question.
- **`DESIGN.md` is the system of record for the design now.** Read it before
  touching CSS, alongside `DIRECTION.md`. It carries the named rules, the cited
  deviations and the gaps, and most of its rules are held by review rather than
  by the build, so nothing will stop you breaking them.
- **The repo is public and git history is permanent.** Sweep any new file before
  **committing**, not just before pushing, and sweep this file hardest. **Ask
  Matthew before pushing.**
- **The register is generated.** `Music7-10_Y9_RepertoireRegister.md` says so at
  the top. Verification records go into
  `School Master/Tools/y9_repertoire_register.py` and the generator is re-run;
  editing the markdown by hand is thrown away on the next run.
- **Serving the build is fixed now, so stop making scratchpad symlinks.**
  `base` is `/year9-music-2027`, so a server has to be rooted at a directory
  whose child has that exact name. Every session so far built that directory in
  its own scratchpad, which died with the session and left another dead entry in
  the School Master root `.claude/launch.json`; there were six of them by this
  morning. `Sites/.serve/` now holds a permanent symlink to each of the four
  sites' `docs/`, with a README, and one config called **`course-sites` on port
  8820** serves all four. The six dead entries are gone. `.serve/` sits above
  every repo, so nothing in it is committed or published.

  ```
  http://localhost:8820/year9-music-2027/
  ```

## Model and effort

**Haiku, low** for the history rewrite and the push, once Matthew has decided.
It is mechanical and the decisions are written down above.

**Opus, medium** for home's unequal-weight rebuild, which is the only design work
left. It is a composition decision on the one surface that never had a comp, and
the fix has to be looked at beside the incumbent before it is kept.

**Sonnet, medium** for the four blueprint sheets when they are written. They are
authored teaching material on an established page shape, not new design.
