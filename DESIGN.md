# Design: Year 9 Music 2027

**This site is on the shared music shell**, since 19 October 2026. Every page, the 123 lessons, the four term hubs, the home page and the four blueprint sheets, is built by `shell.py` and styled by `assets/shell.css`. The look belongs to the shell, not to this repo, and is the same across the music sites apart from one accent per year group. Year 9's is green (`#1F7A3A`), set by `data-year="9"`.

So this file says where the look lives, how this site's data reaches the shell, and what is still Year 9's own: mainly the drawings in `plots.py` and the three read blocks. `DESIGN-NOTES.md` records the decisions made while moving the site across.

## Where the look lives

- **`../music-shell/README.md`**: what the shell is, what each file does, and its rules. The shell is a local repo beside this one and is never pushed, so it is not on GitHub.
- **`../.serve/proto/redesign/SHELL-PLAN.md`**: the plan the shell was built to, including the block mapping for this site and the five decisions Matthew accepted on 19 October 2026.
- **`shell.py`, `assets/shell.css`, `assets/shell.js` and the fonts in `assets/fonts/`** are copies. Never edit them here. Edit `music-shell/`, then run `python3 music-shell/sync.py year9-music-2027` from `Sites/`. `sync.py --check` reports a hand-edited copy.

The direction is **B, Stage Card**: a warm grey ground, every section a white card with an icon-and-word label, the title in one solid accent card. Type is Bricolage Grotesque for display and Atkinson Hyperlegible for reading, both self-hosted.

## How the data reaches the shell

The data did not move. `data/course/` is read exactly as before and `build.py` hands the pieces to shell functions.

### Lessons (123)

| Data | On the page |
| --- | --- |
| `title`, `week`, number | Head card. The kicker is the unit and week, led by "Up to here" on the current lesson |
| `contentCode`, `body.repertoire` | The head card's meta line, after "Lesson n of 30" |
| `body.bring` | A chip on the head card ("Bring: ..."), since it is the one a student acts on |
| `body.lead` | Learning intention. It is the same sentence as `intention` in every lesson, so it is printed once |
| `body.criteria`, `outcomes` | Success criteria, outcomes at the foot. `body.criteria` is the authored set; the lesson-level `criteria` differs in all 123 and is not used |
| `body.clauses` | In class, titled "What we do", each step tagged with its `kind`, which names where the doing happens ("In the room", "With the band", "In pairs", "On your own", "In flat.io", "Assessed") |
| `body.plot` (36 lessons) | "Stage plot" side card beside In class: `plots.small_stage()` |
| `body.patched` | "You'll need" side card beside In class |
| `body.listen` | Listen, the shell's player |
| `body.guide` (4) | Cue sheet |
| `body.explain` (33) | Learn, its `h` items as subheads |
| `body.worked` (3) | Worked example, full form, titled "Two takes", with Year 9's labels "The one that works" and "The one that doesn't" |
| `enduring` | Worth keeping, the closing card |

Under the lesson, standalone only: the term folded shut as "This term", then the blueprint links on Term 2.

### Term hubs (4)

Head card ("Term n · Unit n of 4"), the "Up to here" card (on a term that is not the live one it says the term is done or not started and points across), the unit's drawing at full size, the assessment card, then every lesson grouped by week as the shell's schedule. An assessment lesson says so in words.

### Home

Head card, then "Up to here" with the current lesson's lead and an "All 30 lessons" button, then the four units as `card_grid` cards on the ground, in teaching order, the live one open. Each says "Now", "Taught" or "Ahead" in words.

### Blueprint sheets (4, Term 2)

At `term2/blueprint/{slug}/`: a head card, "The sheet" (the drawing), "How it works" (the sheet's `deck` and `rules`), and previous and next between sheets. The term fold and the blueprint links sit under it, as on a lesson. A blueprint has no week, no content code and no intention, so it has none of those cards.

## What is still this site's own

### The drawings (`plots.py`)

Year 9 is the year the scaffold starts coming away, and the drawings are why: a stage plot is the sheet a band hands the sound engineer so that strangers can play together without rehearsing the logistics, which is Term 2's own enduring understanding about form. So each unit gets the document that unit's musicians actually use.

| Unit | Drawing | Where |
| --- | --- | --- |
| 1 Like a Version | Stage plot, every source carrying its input number | Hub |
| 2 Blues to Jazz | Chord chart, twelve bars in three systems, roman numerals underneath | Hub |
| 3 Sounds of Australia | Listening set-up, the equilateral triangle | Hub |
| 4 Level Up | Cue sheet, timecode across the top, stems down the side | Hub |
| Any lesson with `plot: "band"` | The stage plot reduced (`small_stage()`) | Lesson side card |
| Term 2 blueprints | Progression, voicings, drum pattern, walking bass (`blueprint(slug)`) | Blueprint sheet |

Rules for them:

- **Each drawing has to be a real document.** The first build drew all four units as the same floor plan, and a band standing on a 12-bar progression taped across the floor is a picture no musician has ever drawn. A blues is time, not floor space. What the unit drawings share is the frame (a bounded sheet, the other three units as dashed brackets above it, a 4px edge below), never the drawing. Do not force a new drawing into a floor plan because the first one was one. `DESIGN-NOTES.md` has the full account.
- **Ink on white.** Since the shell every drawing sits on a white card, so every drawing is dark ink (`#141517`, labels `#5D5F63`) in Atkinson Hyperlegible. In the unit drawings the constants keep their old names (`CHALK` is the line, `DIM` the labels) so the code did not churn. The rule that survives from the old world is that the ground decides the ink: check where the `<svg>` will sit before choosing colours, never copy the nearest function's.
- **The other three units are a dashed bracket at 34 percent.** About 2.4:1 on white, and the dash, not the fade, carries "not live", so the state never rests on contrast alone.
- **No names in the corners.** The card's own label names the drawing ("Stage plot", "The sheet"), so the drawing would say it twice.
- **Unit drawings are drawn at 1200 wide and their lettering is scaled up by `TYPE_SCALE` (1.35)** to read at card size. The blueprint sheets are drawn at 900 and are not scaled: a card already shows them a little larger than the old plate, and their key letters sit too close to the next line's numerals to take more.
- **On a phone a drawing scrolls sideways inside its card**, never the page. Unit drawings hold a 46rem minimum, blueprint sheets 36rem (`assets/site.css`). Shrinking a 1200-wide drawing to 340 points turns it to a smudge.
- **Atkinson is wider than the Chivo the drawings were first set in**, so two were adjusted when they moved: the progression's rows are 74 apart, and the drum pattern's labels start clear of the left rule. A font change in `plots.py` means re-checking every drawing for collisions.

### The three read blocks

`explain`, `guide` and `worked` are this site's authored depth, and `LESSON-DEPTH-TRIAGE.md` governs which lessons get one. Their data shapes are in `README.md`. Rules that live in the data and the build rather than the look:

- **A work in the cue sheet is not also a row in Listen** on the same page. `assert_no_doubled_work()` fails the build.
- **Two takes means two.** `assert_worked_complete()` fails the build if the question, the model or either half of the failing take is missing. The failing take is written at the length students actually write, and is one that looks fine.
- **Cue times are measured, never remembered.** A timestamp is a claim about a recording. `tools/loop.py` measures a chord loop's length and where each pass starts; anything it cannot reach waits for someone with the recording and an ear.
- **One player on the page at a time**, across Listen and the cue sheet both. The shell holds this.

### The rest

- **`site.css` styles furniture only** (the drawings' scrolling and widths). Restyling a shell class here is how the sites drift apart, and `sync.py --check` warns about it.
- **The live position** is `currentTerm` and `currentLesson` in `data/course/course.json`, updated from the daily debriefs. It decides "Up to here", the done and now states in the schedules, and which unit is open on home.
- **URLs stay exactly as they are**: `term2/02/`, `term2/blueprint/{slug}/`. Canvas frames point at them.

## Words

One vocabulary across the music sites, plain words over the old metaphors (decision 2 in `SHELL-PLAN.md`). The data keeps its old field names, but the page says:

| Old world | On the page now |
| --- | --- |
| Input 02 of 30 | Lesson 2 of 30 |
| On the desk | Up to here |
| Patched in | You'll need |

Furniture keeps its real names: the stage plot, the blueprint.

## Known gaps

- **No AT3 exam paper**, so no examination-paper page exists. Needs Matthew's AT3 materials first.
- **Term 1 lesson 04's third work has no cue times.** The recording could not be fetched, so it stays in Listen until someone sets four or five times with it playing.
- **Hoochie Coochie Man's harmonic rhythm** (Term 2 lesson 02's Listen) is not written. It reads fine as a plain row without it.

## The look this replaced

The site was built in its own world, **The Plot** (the year as the room drawn from above, stage-floor black, one fluoro tape colour per term, a multicore strip of the term's lessons, Saira Stencil and Chivo), from 16 August to 19 October 2026. It retired with the shell, along with the multicore strip and the per-term colours (decision 3 in `SHELL-PLAN.md`). Its full design record is this file as it stood at commit `47576ad`, and the comps are in `.impeccable/mocks/`. `.impeccable/design.json` still describes The Plot and is not the current system. Before-shots of the old pages are in `../music-shell/shots/before/`.
