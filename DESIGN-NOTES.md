# Design notes: the move to the shared shell

`DESIGN.md` is the system of record for this site. This file records why things are the way they are: the decisions made when the site moved onto the shared music shell (19 October 2026), and the one mistake from the original build that is worth never repeating.

The notes on the hub and home as they were designed in The Plot (16 to 18 August 2026: the multicore, the week ruler, the tape budget, the stencil face) are in this file's history up to commit `47576ad`. None of those devices exists now.

## The drawings, and the mistake worth keeping a record of

The first build drew all four units as the same floor plan with different things standing on it. The read on it from the teacher was that the pictures were "in that uncanny valley range of they look like they are related to music but also make no real sense at all. Like a person wouldn't do that." That was correct, and the worst was unit 2: a band standing on a 12-bar chord progression taped across the floor. A blues is time, not floor space. No musician has ever drawn that.

The cause was deciding the room-from-above had to apply to all four units and then forcing each unit into a floor plan whether or not it had anything to do with floors. The metaphor doing overtime.

**What is shared is the frame, not the drawing.** Each unit is the document that unit's musicians actually use: a stage plot, a chord chart, a listening set-up, a cue sheet. The lesson page's small drawing was changed the same way, from five circles with instrument names to a real stage plot in miniature. This survived the shell unchanged, because it was never about the look.

## Decisions made on the way across

**Lessons (increment 3).**

- The stage plot became a side card beside In class, "Stage plot", and "Patched in" became "You'll need". The rest of the old vocabulary went the same way: "Input" is "Lesson", "On the desk" is "Up to here".
- `small_stage()` was recoloured to ink on white and moved to Atkinson. It also lost its "STAGE PLOT" corner label, since the card says it, and "DOWNSTAGE EDGE" became "DOWNSTAGE" on the empty left of the floor, because at that size it ran through the right-hand wedge.
- `body.lead` is printed once, as the learning intention, because it is the same sentence as `intention` in every lesson.
- "Bring" moved to a chip on the head card, since it is the one thing a student acts on before the lesson.

**Term hubs (increment 4).**

- **The multicore strip retired**, with the week ruler and the 5% alignment that tied it to the drawing. The shell's schedule says the same thing in words, grouped by week. The 4px edge along the bottom of each unit drawing stays, as the frame's second line weight, though nothing plugs into it now.
- **Per-term tape colours retired.** One accent per year group replaces the four tapes.
- The four unit drawings were recoloured to ink, their corner names removed, and their lettering scaled up by 1.35 to read at card size. The ghost brackets stayed, at 34 percent on white, which is about the 2.4:1 the chalk version was tuned to.

**Home and the blueprint sheets (increment 5).**

- **Home** is a head card, "Up to here" with the lesson's lead and an "All 30 lessons" button, then the four units as `card_grid` cards on the ground (not inside a section card), the live one open. No year-scale drawing, which was already the ruling in The Plot: a third, year-sized drawing would say nothing the four units do not.
- **Closed `card_grid` cards place their four pieces explicitly** in the shell. Flowing kicker, title, text and meta into three columns scrambled them.
- **Blueprint sheets** are a head card, "The sheet", "How it works" and previous and next between sheets, with the term fold and the blueprint links under them as on lessons. Their drawings moved to Atkinson and lost their corner names, and were not type-scaled.
- Atkinson is wider than Chivo, so two drawings were adjusted: the progression's rows are 74 apart, and the drum pattern's labels start clear of the left rule.

## Still worth knowing

- **The data keeps its old field names** (`clauses`, `patched`, `plot`, `guide`). Renaming them would churn every term file and the extractor for no student benefit, so the words changed on the page only.
- **Contrast is still a product constraint.** The page is projected in a daylit room. The shell holds this for its own components; anything drawn in `plots.py` has to be checked by eye at card size, since the shell cannot see inside an SVG.
