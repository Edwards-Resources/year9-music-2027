# Next session: Year 9 Music 2027

## Where this stands, 20 October 2026

**The site is finished and on the shared music shell.** All 123 lessons, the four term hubs, the home page and the four blueprint sheets are built by `shell.py` (direction B, Stage Card, green accent). The Plot is gone: no `legacy.css`, no multicore, no tape colours, no Saira Stencil or Chivo. Pushed 19 October 2026 at `47576ad`.

- 132 pages. Parity 0 missing, sweep 0 hits, `sync.py --check` clean, no sideways page scroll at 375. Both build asserts pass.
- `DESIGN.md` says how the data reaches the shell and what is still this site's own: the drawings in `plots.py` and the three read blocks. `DESIGN-NOTES.md` records the decisions made moving across. The look itself is documented in `../music-shell/README.md` and `../.serve/proto/redesign/SHELL-PLAN.md`.

## Next task

Nothing is owed on the build. Pick from:

1. **A content review** now that the site is complete. Worth Matthew's eyes before students see it: the drum pattern, the voicings and the walking bass excerpt on the blueprint sheets are musically standard but were written from the term's own lesson text, not from a lesson plan or notation he supplied. Week 4 (lesson 12, walking bass) and Week 5 (lesson 13, comping and voicings) are where they are taught.
2. **No AT3 exam paper.** Program work, not this repo's. Needs Matthew's AT3 materials first.
3. **Hoochie Coochie Man's harmonic rhythm** (Term 2 lesson 02's Listen). Not urgent; it reads fine as a plain row.

## Decisions waiting on Matthew

1. **The blueprint content itself**, as above.
2. **The third work in Term 1 lesson 04's cue sheet** has no cue times, because the audio would not download. Four or five, set with the recording playing.
3. **`DIRECTION.md`'s old history and the comp D sidecar name Matthew**, already in pushed history. Same question as Year 8, smaller.

The old question about breaking the player out of the 240px listen block is closed: the 240px column went with The Plot, and the shell plays each recording in its own 16:9 tile, at least 15rem wide and up to 30rem when it is the only one.

## Watch out for

- **Never edit this repo's copy of the shell** (`shell.py`, `assets/shell.css`, `assets/shell.js`, the fonts). Edit `music-shell/` and run `python3 music-shell/sync.py year9-music-2027` from `Sites/`. Run `sync.py --check` at the start of any session that touches the site.
- **`site.css` styles furniture only** (the drawings' scroll and widths). Never restyle a shell class here.
- **URLs stay exactly as they are.** Canvas frames point at them.
- **Sweep before every commit**: `python3 music-shell/tools/sweep.py year9-music-2027` from `Sites/`, then parity after every build: `python3 music-shell/tools/parity.py year9-music-2027`. The sweep never prints what it matched; keep notes the same.
- **Build with `/usr/bin/python3`** (3.9). The shell has to import on it.
- **Preview** through the `course-sites` launch config, which serves all the sites from `Sites/.serve/` on port 8820.
- **A drawing's colour comes from where it sits, not from the file it lives in.** Every drawing is ink on a white card now. A font change in `plots.py` means re-checking every drawing for collisions, as the move to Atkinson showed.
- **Editing `data/*.json` by round-tripping through `json.dump` reformats the whole file.** Insert new keys with a text edit at the existing indent, validate with `python3 -c "import json; json.load(open(path))"`, then rebuild.
- **Italics need `_underscores_`**, not `*asterisks*`.
- **Elements of music, never "concepts of music".**
- **Never `git stash` in this repo.**
- **No school name or student data anywhere.** This file is the one place that has to discuss what must not be on the site in order to warn about it. Swept before this commit: no school name, no student names, and the two works barred from the site are not named here.

## Model and effort

**Sonnet, low** for the content review: reading and flagging, not building. **Opus, medium** only if it turns up a musical or teaching correction that needs rethinking rather than a wording fix. Anything that changes how a page looks is shell work, done in `music-shell/`, not here.

## Last commit

`47576ad` Home and blueprint sheets on the shared shell; the old Plot layout is gone (pushed). The docs rewrite for the shell follows it.
