# Next session: Year 9 Music 2027

## Where this stands, 18 August 2026

**All four guides and 33 of the 35 explains are written. The remaining two,
plus one from Term 1, wait on a `worked` block that is designed and ruled
on but not built.** The `worked` question was the only thing genuinely
undecided going into this session; the guide and explain shapes were
already settled and this session was pure authoring against them, work
that spanned three separate sessions across 17 and 18 August.

- Live at **https://edwards-resources.github.io/year9-music-2027/**, but
  this session's commits are **not pushed**. Ask before pushing.
- Repo `Edwards-Resources/year9-music-2027`, public, Pages serving `main`
  `/docs`.
- This session's commits, oldest first: `b14a38a` the three remaining
  guides, `a49933c` Term 1's six explains, `0c4ae6d` Term 2's seven,
  `f72fd03` Term 3's eleven, `a804315` Term 4's eight.
- No vault session log written yet for this session. Worth one before the
  next session starts, covering the guide measurement work and the
  explain pour together.

## The guides: all four done, all cue times measured

T1 #04 was already built. This session added T2 #02, T3 #14 and T4 #02.

**T2 #02, the 12-bar blues counted.** `tools/loop.py`'s method extended to
search a 12-bar period (12-45s) instead of the 4-bar range the tool
shipped with — the CLI itself still only does the 4-bar case, this was a
one-off script using its `chroma()` and `triad()` functions directly, not
a change to the tool. Sweet Home Chicago (tonic F, 103.5 bpm as a 12-bar
chorus) and Pride and Joy (tonic **Eb**, not the E you'd expect from the
era, 126.8 bpm) both measured cleanly and both tempos are plausible for
their style. **Hoochie Coochie Man stays in `listen` only, not cued**: its
harmony is a riff-based vamp rather than a clean move through IV and V, so
a cue table there would have been guessed, not measured. Same shape as
T1's third work: a real reason to leave one out, not a downloading
failure this time.

Bar positions within each measured chorus (bar 5 for IV, bar 9 for V) use
the standard slow-change 12-bar convention, arithmetic against the
measured bar length and downbeat, not something separately measured
chord-by-chord — a chord-recognition pass at that grain was tried and was
too noisy to trust. Worth knowing if a future session wants to tighten
this further.

**T3 #14 and T4 #02 are not loop-form**, so `loop.py`'s method doesn't
apply at all — a protest ballad and two film/game cues don't repeat on a
short cycle the way a pop loop or a blues chorus does. Their cues come
from a **measured loudness envelope** instead (RMS energy against time,
computed the same way, from real downloaded audio): the swell-and-pull-
back, the sustained loud stretch, and the fade in *I Was Only 19*; the two
step-changes in level in each screen work where the same motif carries on
under more of the ensemble. This is a genuinely different measurement
method from `loop.py`'s, both grounded in the actual recording rather
than guessed, and it's worth documenting properly in `DESIGN.md` or a
`tools/` docstring if a fifth guide is ever built on non-loop material.

**YouTube downloads needed `--extractor-args "youtube:player_client=android"`**
this session — the default and `ios` clients both failed (403, or no
formats at all) against every one of the six works tried. `tools/loop.py`'s
own docstring command doesn't include this flag; add it if the plain
command starts failing again.

## The explains: 33 of 35 written

| Term | Written | Deferred |
| --- | --- | --- |
| Term 1 | 7 of 7 | — |
| Term 2 | 7 of 7 | — |
| Term 3 | 11 of 12 | #09 |
| Term 4 | 8 of 9 | #19 |

**#09 (Term 3) and #19 (Term 4) are not written.** The 17 August ruling
gives both a `worked` block instead of a 250-word explain, alongside T1
#26, and `worked` is designed (see the 17 August handoff, now folded into
this file's history) but does not exist in `build.py`, the CSS or
`site.js`. Writing prose explains for them now would mean throwing that
prose away once `worked` is built, so they wait.

**T3 #11 and #12 name no repertoire**, per the triage's own rule for that
input. Checked by rereading both before committing.

**T3 #14's explain is the promoted one** — it was Block B in the original
triage table and promoted to A on 17 August specifically because it's one
of the four guide inputs. It names *I Was Only 19* freely, because that
work is already named and embedded in the lesson's existing `listen`/
`guide` data; the "names no repertoire" rule is about the Aboriginal and
Torres Strait Islander consultation content in the Weeks 4–6 block (T3
#11, #12), not about this lesson, which sits in a different part of the
term.

One correction to earlier handoffs: an older version of this file's watch-
list named **T3 #16** as one of the three repertoire-blind inputs. #16 was
in the end rejected from the explain list entirely (see the final table in
`LESSON-DEPTH-TRIAGE.md` and its own "Rejected" line) — that mention was
carried over from an earlier draft of the triage and never fully
corrected. #16 has no explain and needs none. The actual third
repertoire-sensitive point in that stretch of the term is T3 #14's
neighbourhood, and #14 itself is fine to name, as above.

**One formatting bug worth remembering: italics need `_underscores_`, not
`*asterisks*`.** `*word*` renders as a literal asterisk in the built page,
not italic — README says so but it's easy to type the wrong one out of
habit. Caught once this session (T1 #11) by rendering the page and reading
it, not by rereading the source. Do that check on any future authoring
session: build, then actually look at a rendered page or two, not just the
JSON.

## What's left

1. **Design and build the `worked` block.** T1 #26, T3 #09 and T4 #19 are
   waiting on it — one exam question, one full-mark answer with the
   reasoning shown, one zero-mark answer that looks fine and isn't. Ruled
   yes on 17 August, not built. This is design work, not authoring, so it
   wants its own session rather than being folded into a content pour.
2. **Write those three `worked` blocks** once the shape exists.
3. **The four blueprint sheets still don't exist** (unchanged from the
   last few handoffs) — `data/course/term2/term.json` holds them at
   `built: false`, no other term has any, and four rejected explains now
   depend on them existing somewhere.
4. **No AT3 exam paper.** Also unchanged, and on the program thread, not
   this one.
5. **The third work in T2#02's `listen`, Hoochie Coochie Man, could still
   get its own guide entry later** if someone wants to work out its actual
   harmonic rhythm by ear rather than by chroma analysis — not urgent, it
   reads fine as a plain `listen` row.

## Decisions waiting on Matthew (unchanged from 17 August)

1. **The third work in T1 #04's cue sheet** still has no cue times (audio
   won't download). Four or five, set with the recording playing.
2. **Rewrite `year8-music`'s published history?** Recommendation: no.
3. **Home's four unit blocks, unequal weight.** Half a session with Opus.
4. **`DIRECTION.md` and the comp D sidecar name Matthew**, already in
   pushed history. Same question as Year 8, smaller.
5. **Should the player break out of the 240px listen block?** One line
   either way, Matthew's call since he's the one projecting it.

## The leak that keeps recurring

Same standing warning as every recent handoff: **this file is the one
place in the repo that has to discuss what must not be on the site, in
order to warn about it.** Swept before this commit: no school name, no
student names, no repertoire named in the T3 Weeks 4–6 sense, and the two
barred works are not named here either. The correction above about T3 #16
names an *input number*, not a work — that's fine, input numbers aren't
the leak, titles and artists are.

## The Year 8 repo

Unchanged from 17 August: the real leak (the teacher's first name baked
into 105 served pages) is fixed forward and pushed. Whether to rewrite the
31-commit published history for it is still open and still Matthew's call.
Recommendation stands: no, for the same reason as before — it's his own
name on his own resources at his own org.

## Watch out for

Everything in the 17 August handoff still applies: `SH_X` and
`--core-inset` both 5%, nothing below the sheet's bottom edge, `GHOST`
means the other three units and nothing else, contrast as a product
constraint, focus as tape-on-floor/ink-on-sheet, `assets/site.js` staying
small and working without it, two tape strips per page at most, the
stencil face never used as a heading face, elements of music not
"concepts of music", no school name or student data anywhere, never `git
stash` in this repo, the 390px-screenshot trap, `DESIGN.md` as the system
of record, sweep before committing not just before pushing, the register
being generated (never hand-edit `Music7-10_Y9_RepertoireRegister.md`),
and the `.serve/` symlink setup for local preview.

One addition from this session: **when downloading audio for cue
measurement, the `android` client is currently the one that works.** Try
it first rather than working through the tool's documented default
command and hitting the same 403 three times.

## Model and effort

**Sonnet, medium** for the `worked` block's authoring once it's designed —
routine writing against a fixed, small shape (one question, one good
answer, one bad one), same register as the explains just finished.

**Opus, medium** for designing `worked` into `build.py`, the CSS and
`site.js`. It is the third read block in a world that now has real
conventions for how a read block sits on the sheet, but a `worked` block's
internal layout (the two contrasting answers side by side or stacked, how
the ALARM rungs are marked) hasn't been drawn yet, so it's a composition
decision like the guide and explain build was, not a port.

**Opus, medium** for home's unequal-weight rebuild, unchanged from 17
August.

**Sonnet, medium** for the four blueprint sheets when they're written,
unchanged from 17 August.
