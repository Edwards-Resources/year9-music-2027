# Design notes: the term hub and the home surface

Neither surface had a comp. Both were designed in the build on 16 August 2026.
This file records what they are and what was decided, so the finish review has
something to review against. It is not DESIGN.md, which is still owed.

## The term hub

**The shape.** Unit head and where the class is, then the unit's sheet of
paperwork at full width, then the multicore running out of its bottom edge, then
the assessment bar, the blueprint, and the full input list as a table.

**The multicore** is the one thing held from comp B, and this is its first build.
Every channel is the same width. On this surface that is the point rather than
the failing the thesis complains about: on a multicore the channels *are* equal,
and what separates them is what is patched into each.

**It is plugged in, not placed under.** `SH_X` in `plots.py` and `--core-inset`
in `site.css` are both 5%, so the strip starts exactly under the sheet's left
edge and ends under its right one. Nothing is drawn below the sheet's bottom
edge. Change one of those two numbers and you must change the other, or the
device quietly stops working.

**The week ruler** mirrors the strip's flex geometry exactly, so a week boundary
falls on a channel boundary. The word "Week" sits in the 5% gutter rather than in
the flex row, because a label in the row pushes every week off its channel.

## The ghost layer, rebuilt

Comp B drew the other three units at 7 to 10 percent opacity, which is about
1.1:1 on this floor. It was not weak, it was absent. Two changes:

1. **26 percent, about 2.4:1**, and the **dash** rather than the fade is what
   carries "not live". A state never rests on the contrast step alone.
2. **A bracket, not a rectangle.** Each ghost is the top edge and two side stubs
   running down to where the live sheet starts, which is what a stack of paper
   looks like from above. A full ghost rectangle crosses everything on the live
   sheet and turns the drawing to mud, which was the other half of why B's
   version did not work.

They are stepped by unit distance, so the year sits in order and the unit next to
this one is closest.

## The drawings, and the mistake worth keeping a record of

The first build drew all four units as the same floor plan with different things
standing on it. The read on it from the user was that the pictures were "in that uncanny
valley range of they look like they are related to music but also make no real
sense at all. Like a person wouldn't do that." That was correct, and the worst of
them was unit 2: a band standing on a 12-bar chord progression taped across the
floor. A blues is time, not floor space. No musician has ever drawn that.

The cause was mine and it is the failure `DIRECTION.md` already names: I decided
the room-from-above had to apply to all four units and then forced each unit into
a floor plan whether or not it had anything to do with floors. The metaphor doing
overtime.

**What is shared is now the frame, not the drawing.** Every unit is one sheet of
production paperwork: bounded, named in its own top corner the way real
paperwork is, ghosts above, painted edge below. Inside that frame each unit is
the document that unit's musicians actually use.

| Unit | Sheet | Why it is real |
| --- | --- | --- |
| 1 Like a Version | Stage plot | Kit drawn as a kit, amps upstage of the players who use them, mics as a head on a stand, every source carrying the input number that finds it on the list |
| 2 Blues to Jazz | Chord chart | Twelve bars as three systems of four, slashes for the beats, chord symbols above and roman numerals below, which is where analysis goes |
| 3 Sounds of Australia | Listening set-up | The equilateral triangle every stereo reference uses, speakers toed in, 60 degrees at the seat |
| 4 Level Up | Cue sheet | Timecode across the top, stems down the side, a bar where each stem plays. This one was already right |

The lesson page's small drawing was changed the same way, from five circles with
instrument names to a real stage plot in miniature, and its heading changed from
"The room" to "Stage plot". That is a content fix inside comp D's composition,
not a change to the composition.

## The home surface

Two jobs in this order: put the class on the lesson it is actually on, then show
the whole year as four units.

**The desk plate** is the page's one torn strip, on the one thing home certainly
has to do. The lead is a sentence, so it reads on a taped panel and never on the
black floor.

**No plan drawing on home.** The sheet is large on the hub and small on a lesson
page. A third, year-sized one would be the same device at a third scale saying
nothing the four unit blocks do not already say.

**The four units carry their tape colour as a chip on the unit number**, black
ink on it, not as a bar across the top of the block. Four coloured bars side by
side read as a rainbow, and a square-cut bar of gaffer colour is what rule 6
exists to refuse. Which unit is live is said by the 4px chalk keyline and by the
words in the corner, never by the colour.

## Rulings made in the build

- **The stencil face.** `DIRECTION.md` allows three places: the class mark, the
  input list head, and the lesson title. Read as the page's own subject name,
  that is the lesson title on a lesson page, the unit name on the hub, and on
  home the title of the lesson on the desk. Still one selector in the CSS. Widen
  it further and it stops being a display voice. **Flag for the finish review.**
- **The tape budget.** The hub spends two: the standing line and the taped
  channel. The input table's current row was a tape fill and is now the 4px
  keyline, because a third would have said nothing the first two had not.
- **Mobile.** The sheet and the strip scroll together inside one container at
  720px. Thirty channels across a phone is 11px each and a 1200-unit drawing in
  340 points cannot be read either; scrolling them separately would break the
  alignment that is the whole device. The full input list is underneath for
  anyone who would rather not drag.

## Settled at the finish review, 17 August 2026

The finish review ran on 17 August 2026 and `DESIGN.md` is written. **`DESIGN.md`
is now the system of record for this site's design**; this file stays as the
build record for the two surfaces that had no comp, and nothing below overrides
it.

- **The three pieces of torn tape are two acts.** A corner pair holds one object
  down, one strip marks the row. The approval sidecar's own wording is the
  reading. A fourth mark is a defect.
- **`--hair` is fixed.** `#313337` at 1.48:1 is now `#63656A` at 3.21:1. It draws
  only structural rules and control borders; the floor's background grid is a
  separate faint rgba and stayed where it was.
- **The ghost bracket stands as built.** The review first asked for the other
  three units' real drawings at 7 to 10 percent and withdrew it once this file
  was in front of it. The bracket at 26 percent with the dash carrying "not live"
  is the answer. The ghost labels are chalk-dim at 5.76:1 and are not ghosted.

## Still open

- ~~**Home's four unit blocks are equal weight.**~~ **Built 18 August 2026.**
  The live unit opens in place and carries its own thirty inputs on the
  multicore; the other three fold to a line each; the stack stays in unit order
  so nothing is lifted out of sequence. No year-scale drawing was added, which
  was the explicit half of the ruling. The strip's 5% inset is zeroed on this
  surface because there is no room here for it to align to.
- **The four blueprint sheets do not exist**, so half the STORY block is unmet.
  The rail and the hub bar now name them on one line instead of four dead
  labels, which is a smaller absence, not a filled one.
