# Next session: Year 9 Music 2027

## Where this stands, 17 August 2026

**All three surfaces are built. Terms 1, 2 and 4 are poured. Term 3 is not.**

- Live at **https://edwards-resources.github.io/year9-music-2027/**. The live
  site is still the **16 August** build. The Term 2, Term 1 and Term 4 pours
  are all committed and **not pushed**. Ask before pushing.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- Last commit: `5cb2e7b Pour the Term 4 lesson bodies`

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

### Ruling 1 is settled and done

**The school's name is out of this repo's pushed history.** Matthew chose the
rewrite with the repo left public. What was actually there, checked before
acting: one occurrence per commit, in `NEXT-SESSION.md` only, in six commits,
two of them pushed. Never in `docs/`, so never served. The initials sat in the
same line of the same six commits and the working tree had already dropped
both, so both were stripped.

All ten commits were rewritten, and the tip tree came out byte-identical to
before, so `docs/` was untouched. The push was **deliberately only up to the
rewritten old tip** (`3cb15fb`, formerly `fa3bc75`), so the history was fixed
without also publishing the Terms 1, 2 and 4 pours, which is still Matthew's
call. `origin/main` was re-scanned after the push and is clean. The local
backup refs were dropped and the reflogs expired, so a future `--all` search
does not turn up a false alarm the way the last one did.

**One thing worth carrying forward:** a force-push does not delete the old
commits from GitHub. They are unreachable but stay fetchable by exact SHA until
GitHub garbage-collects. Nobody has those SHAs, so the residual risk is
theoretical, but it is not zero and the deletion-and-recreate option was the
only one that would have closed it completely.

### Term 4 poured

**30 bodies, so all 30 inputs of Level Up have a page.** The site is now 93 of
123, and the house style is unchanged from the two terms that set it. Three
things this unit does differently, all because it is a composing unit rather
than a performing one, and none of them a drift:

- **`Assessed` is spent once, not twice.** The rule was two per term because
  Terms 1 and 2 each had two days of marks taken while a student played. This
  term has one marked moment, the AT4 submission, so it is spent once, on input
  23. The two draft checkpoints are explicitly not marks and do not get it.
- **`plot: band` is on one lesson**, the Week 10 performance check-in, against
  Terms 1 and 2 at 15 and 14. The rest of the term is at a screen and drawing a
  band plot on it would be a lie about the room.
- **`In flat.io` carries 13 clauses**, against 16 across the whole of Terms 1
  and 2 together. Every composing lesson has exactly one.

Everything else lands where the first two terms did: 90 clauses, mean 21.8
words against their 20.9; leads mean 11.7 words against 12.9; three clauses
everywhere; `bring` from the fixed set of six, using four of them.

**The Term 4 repertoire is fully verified.** All five went the full order:
Apple explicitness flag, then oEmbed for a live id on the right channel, then
duration. All five are `notExplicit`, all five sit on an official, artist or
Topic channel, and **the ids are in the repertoire register, off this repo**.
Two carry a judgement recorded with them. The Studio Ghibli film soundtrack is
not on Apple Music in Australia, so the Hisaishi taught is his own Royal
Philharmonic recording, which is also what his official channel carries. Daft
Punk's main theme has no official video upload, only Topic, while the official
channel carries other cues from the same score.

**Only the main theme of The Last of Us is verified**, not the fuller cue the
Week 5 orchestration lesson pairs it against. So only the main theme is named
on the site and the clause prose carries the other one, the same way Term 1
input 10 handles its missing pair.

**Input 27 has no Listen block on purpose.** It is the deliberately unfamiliar
work, chosen to be outside the unit's repertoire, so there is nothing to name.

**One small ruling taken in passing.** The Last of Us first went in with
`meta: "Santaolalla, 2013"` and the meta was wide enough to wrap the title onto
two lines, exactly the squeeze open ruling 5 describes. It was cut to `"2013"`,
because the title already names the work. So the Term 4 convention is: the meta
identifies whatever the title does not. For a cue title nobody would place, that
is the composer or the film (`"Zimmer, 2014"`, `"Celeste, 2018"`); for a work
whose title is its own name, the year alone. This is more evidence for ruling 5,
not against it: identification is being carried by `meta` again, and `artist`
still has never been read.

## The actual next task

**Pour Term 3. It is the last one.** 30 bodies, and it is the hardest of the
four, which is why it was left until last:

- **Nine repertoire picks are still unverified**, more than any other term had.
  Note this is nine, not the eight the last handoff said; the Flume entry says
  its verification is recorded in Section 3 but it carries no record in
  `FORWARD`, so check that one rather than assuming it is done.
- **The two verified Term 3 unseen excerpts are barred from the site**, and
  **neither is named anywhere in this repository**, which is public. They live
  in `Music7-10_Y9_RepertoireRegister.md`, off this repo, and that is the only
  place they are written down. **Do not copy them into a note here to make it
  easier to follow.**
- **The ATSI protocol block, Weeks 4 to 6, is deliberately empty** until Matthew
  selects through the school's consultation. Do not fill it, and do not write
  around it in a way that pretends it is not there.

Cost it as writing, not as conversion: the extractor's `steps`, `intention` and
`criteria` are in the teacher's voice. Term 4 took well under one session at
Opus medium including the five repertoire checks, and Term 1 took one session
for 33 bodies plus four checks.

## What is genuinely missing

- **30 lesson bodies**, all of them Term 3.
- **9 of the 26 repertoire picks are still unverified**, all in Term 3.
  Seventeen are done. Every remaining track needs the full order: **Apple
  explicitness flag, then oEmbed for a live id and the right channel, then
  duration.** That order, every time. Where an official upload turns out to be
  an edit, or does not exist, take the Topic master and record why, as all three
  poured terms now do.
- **No AT4 exam paper.** Open on the program thread, not this one.
- **No DESIGN.md and no finish review.** The direction contract ends with
  "unreviewed and undocumented is unfinished". `DESIGN-NOTES.md` is a record of
  decisions, not a substitute for either.

## Decisions waiting on Matthew

1. **Push the three pours?** The live site is still the 16 August build and is
   three terms behind the repo. The history rewrite was pushed on its own
   deliberately, so this is now a clean, separate yes or no. **Recommendation:
   push once Term 3 is poured**, so the site goes live complete rather than
   three-quarters done.
2. **Rewrite `year8-music`'s published history?** See below. **Recommendation:
   no.**
3. **The lesson page carries three pieces of torn tape, not two** - the plate's
   two corner strips plus the rail's current row. Either the two corners count
   as one act of taping the plate down, or the build has been over budget since
   the first commit. Inherited from comp D. A ruling is owed at the finish
   review.
4. **`DIRECTION.md` and the comp D approval sidecar name Matthew**, and both
   are already in pushed history. Same question as Year 8, smaller. Note the
   history rewrite in item 1 above did **not** touch this; it was scoped to the
   school's name, which is a different rule and a different party.
5. **The `artist` field in a `listen` entry is never rendered, and the case for
   deleting it is now stronger again.** Comp D shows the title and a short meta
   only, and that is approved. The meta is `white-space:nowrap`, so a long name
   in it squeezes the title. Term 4 hit this a third time and solved it the same
   way the other two did, by shortening the meta. Across all 93 pages,
   identification is carried by `meta` or by clause prose, and `artist` has
   never once been read. **Recommendation: the field goes at the finish review.**
   A second line in the block is the alternative and nobody has needed it yet.

## The Year 8 repo

The 16 August handoff said `year8-music` had **the school's name** in it
including in served pages. **That was wrong.** The school's name, its initials
and the words for a high school all return zero on a word-boundary search
across every blob in all 31 commits; the apparent hits were substring and
regex-wildcard noise.

**Do not write the search terms out here to make that claim checkable.** The
16 August handoff did, and in doing so it put the school's name into this
public repo for the first time, in the one sentence that was documenting its
absence somewhere else. That is now fixed in history as well as forward, per
ruling 1 above.

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
  from the session that wrote it, and so do all three `year9` configs in the
  School Master root. Serving the build needs a directory whose child is named
  `year9-music-2027`, because `base` is `/year9-music-2027`. This session used a
  symlink in its own scratchpad and a config named `year9-t4` on port 8814 in
  the School Master root `.claude/launch.json`. That one is now dead too.

## Model and effort

**Opus, medium**, for the Term 3 pour: it is student-facing writing against a
registered program, nine repertoire checks have a strict order that must not be
shortcut, and there are two barred works and an empty ATSI block to write around
without pretending either is not there. Terms 1, 2 and 4 each fitted comfortably
in one session at that setting, and this one is the heaviest of the four.

If instead you are doing the finish review and DESIGN.md, **Opus, medium** as
well. It is a judgement pass over an approved contract, and there are five
rulings queued for it.
