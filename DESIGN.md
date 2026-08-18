---
name: Year 9 Music 2027
description: A stage plot and input list for a year of music, drawn in chalk on a black floor and taped down.
colors:
  floor: "#111214"
  floor-grid: "rgba(242,241,236,.03)"
  chalk: "#F2F1EC"
  chalk-dim: "#8E8F8B"
  chalk-past: "#9A9B97"
  hair: "#63656A"
  ghost: "rgba(242,241,236,.26)"
  sheet: "#F4F3EE"
  ink: "#141517"
  ink-hover: "#2C2E31"
  ink-dim: "#5D5F63"
  rule: "rgba(20,21,23,.18)"
  tape-t1: "#E8FF3A"
  tape-t2: "#FF2D78"
  tape-t3: "#FF6A1F"
  tape-t4: "#3DFF7D"
typography:
  display:
    fontFamily: "Saira Stencil One, Chivo, sans-serif"
    fontSize: "clamp(2.1rem, 4.6vw, 3.7rem)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "normal"
  headline:
    fontFamily: "Chivo, system-ui, sans-serif"
    fontSize: "clamp(2rem, 4.4vw, 3.1rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Chivo, system-ui, sans-serif"
    fontSize: "clamp(1.35rem, 2.2vw, 1.72rem)"
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: "-0.018em"
  body:
    fontFamily: "Chivo, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "Chivo, system-ui, sans-serif"
    fontSize: "0.62rem"
    fontWeight: 800
    lineHeight: 1.5
    letterSpacing: "0.22em"
  mono:
    fontFamily: "Chivo Mono, ui-monospace, monospace"
    fontSize: "0.72rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0.14em"
    fontFeature: "tabular-nums"
rounded:
  none: "0"
spacing:
  grid: "48px"
  rail-gutter: "22px"
  plate-gutter: "34px"
  page-gutter: "40px"
  page-gutter-narrow: "16px"
components:
  nav-channel:
    textColor: "{colors.chalk-dim}"
    padding: "8px 14px"
    rounded: "{rounded.none}"
    typography: "{typography.label}"
  nav-channel-active:
    backgroundColor: "{colors.tape-t1}"
    textColor: "{colors.ink}"
    padding: "8px 14px"
    rounded: "{rounded.none}"
  rail-row:
    textColor: "{colors.chalk}"
    padding: "6px 22px"
    rounded: "{rounded.none}"
  rail-row-now:
    backgroundColor: "{colors.tape-t1}"
    textColor: "{colors.ink}"
    padding: "9px 12px"
    rounded: "{rounded.none}"
  rail-row-done:
    textColor: "{colors.chalk-past}"
    padding: "6px 22px"
  plate:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "34px 34px 32px"
  tape-strip:
    backgroundColor: "{colors.tape-t1}"
    textColor: "{colors.ink}"
    width: "124px"
    height: "32px"
    rounded: "{rounded.none}"
  plate-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sheet}"
    padding: "12px 20px"
    rounded: "{rounded.none}"
  plate-button-hover:
    backgroundColor: "{colors.ink-hover}"
    textColor: "{colors.sheet}"
  plate-button-alt:
    textColor: "{colors.ink}"
    padding: "12px 20px"
    rounded: "{rounded.none}"
  floor-button:
    textColor: "{colors.chalk}"
    padding: "10px 15px"
    rounded: "{rounded.none}"
  unit-chip:
    backgroundColor: "{colors.tape-t1}"
    textColor: "{colors.ink}"
    padding: "2px 11px"
    rounded: "{rounded.none}"
---

# Design System: Year 9 Music 2027

## Overview

**Creative North Star: "The Plot"**

The stage plot and input list a band hands a sound engineer. The whole year is one room drawn from above in chalk line on a black stage floor, and every lesson is a numbered input on a list beside it. Nothing here is decorated; everything is production paperwork, which is a genre that has to survive being read in a dark room by someone with both hands full. That is the same job the site has: it is projected in a daylit classroom and operated by a teacher holding an instrument.

The system's material logic is three surfaces stacked. The **floor** is black and gridded, and it carries drawn line, labels and lists. The **sheet** is a white panel laid on the floor and taped down, and it is where sustained reading happens. The **tape** is one fluoro colour per term, torn at the ends, used only as fill and marker and always carrying black ink. Long white prose never sits on the black field. Colour never sits as type on the black field. Every drawn thing is one of exactly two line weights.

The world refuses two things by name. It refuses the course-site default of equal-weight lesson cards in a grid, where week one and week nine look identical, and it refuses the light paper ground shared by the three sibling teaching sites. Year 8's Tour Tee is the sharpest anti-reference because this cohort has just spent a year inside it.

**Key Characteristics:**
- Black stage floor with a faint 48px drawn grid; white taped panels for anything longer than a list
- Two line weights only: 1px chalk hairline, 4px painted keyline
- Four fluoro tape colours, one per term, always with black ink, always torn at the ends
- Square corners everywhere; no shadows, no gradients, no radii
- Stencil display face in three places per page and no more
- Position is stated twice: by a marker or keyline and by a word, never by colour alone
- No motion authored anywhere

## Colors

A near-black stage floor, a chalk white line on it, a warm white sheet laid over it, and exactly one fluoro gaffer tape colour live at a time.

### Primary
- **Gaffer Yellow, Term 1** (`{colors.tape-t1}`): the live term's tape on every Term 1 surface. Fills the rail's current row, the hub's standing strip and its live channel, the plate's corner strips, the active nav channel, the unit chip and the focus ring.
- **Gaffer Magenta, Term 2** (`{colors.tape-t2}`): the same slot on Term 2 surfaces.
- **Gaffer Orange, Term 3** (`{colors.tape-t3}`): the same slot on Term 3 surfaces.
- **Gaffer Green, Term 4** (`{colors.tape-t4}`): the same slot on Term 4 surfaces.

The four are never in play at once except on home's year stack, where they appear as four chips on unit numbers, the open unit's larger than the three folded ones. `--tape` resolves from `body[data-term]`, so every component reads "the term's colour" and never a named term.

### Neutral
- **Stage Floor** (`{colors.floor}`): the page ground on every surface.
- **Floor Grid** (`{colors.floor-grid}`): the 48px repeating graph-paper ruling on the body. Texture, not structure; it is deliberately below the contrast floor and must stay there.
- **Chalk** (`{colors.chalk}`): everything drawn or written on the floor, and the 4px painted keyline.
- **Chalk Dim** (`{colors.chalk-dim}`): labels, eyebrows, meta lines, week rulers, inactive nav, deck text. Also the ghost drawing's labels at 5.76:1.
- **Chalk Past** (`{colors.chalk-past}`): a lesson already taught, in the rail and the input table, at 6.7:1. Never used alone: the strike marker travels with it.
- **Hairline** (`{colors.hair}`): every 1px structural rule and control border on the floor at 3.21:1. The 1px weight of the world.
- **Ghost** (`{colors.ghost}`): the other three units' sheets, drawn as dashed brackets in SVG at about 2.4:1.
- **Sheet** (`{colors.sheet}`): the taped white panel.
- **Ink** (`{colors.ink}`): all type on sheet and on tape; also the plate's 2px section dividers and the solid plate button.
- **Ink Dim** (`{colors.ink-dim}`): field labels, channel numbers and secondary lines inside the sheet.
- **Sheet Rule** (`{colors.rule}`): every 1px rule drawn inside the sheet.

Two colours sit outside this palette on purpose, both in the print block only:
`#fff` for the ground and `#000` for type and the plate's border. Print is paper
and ink rather than a floor and a sheet, and the screen palette does not carry
over to it. They are not available anywhere else.

### Named Rules

**The Black Ink Rule.** Type on a tape colour is always ink, never white, and a tape colour is never used as type on the floor. The four fluoros are fills and markers only.

**The Never-Colour-Alone Rule.** No state is carried by colour by itself. The current row is taped *and* carries the word marking the position *and* the channel number. A taught lesson is dimmed *and* struck with a × glyph. The live unit is chalk-keylined *and* says so in its corner.

**The Two Grounds Rule.** A paragraph belongs on the sheet. The floor carries labels, lists, numbers, drawn line and nothing that needs sustained reading. This is the daylit-projector constraint before it is a style rule.

**The Structure-Not-Texture Rule.** `--hair` at #63656A (3.21:1) draws structure and must clear the 3:1 non-text floor; `--floor-grid` at rgba(242,241,236,.03) is texture and stays faint. They are separate tokens and neither may be tuned to the other. *Watch item:* at 3.21:1 the hub input table reads more ruled than before. If it tips toward a spreadsheet, thin the rules' extent, never dim the token back.

## Typography

**Display Font:** Saira Stencil One (self-hosted, 400 only)
**Body Font:** Chivo (self-hosted variable, 300–900)
**Label/Mono Font:** Chivo Mono (self-hosted variable, 300–800, tabular figures)

**Character:** A stencilled crate mark over a grotesque built for signage. Chivo and Chivo Mono are one superfamily, so the site is two families rather than three, and the stencil is a voice used sparingly enough to stay a voice. A third face is a defect.

### Hierarchy
- **Display** (Saira Stencil One 400, clamp 2.1–3.7rem, line-height .96, uppercase, max 15ch): the page's own subject name. The lesson title on a lesson page, the unit name on a hub, the desk lesson's title on home. Also the class mark (1.2rem) and the input list head (.98rem) at their own sizes.
- **Headline** (Chivo 900, clamp 2–3.1rem, line-height 1, letter-spacing -.03em, uppercase): home's h1 only. Home is the one surface whose heading is not the stencil.
- **Title** (Chivo 700, clamp 1.35–1.72rem, line-height 1.22, max 26ch): the lesson's lead sentence on the plate, and home's desk lead.
- **Body** (Chivo 400, 16px, line-height 1.5, max 66ch in clauses, 58ch in success criteria): everything read at length, always on the sheet.
- **Label** (Chivo 800, .60–.72rem, letter-spacing .20–.22em, uppercase): field names, section heads, week markers, position lines, table headers. The site's most-used voice by count.
- **Mono** (Chivo Mono, .72–.78rem, tabular figures): channel numbers, durations, dates, codes and any figure that has to line up in a column.

### Named Rules

**The Three Places Rule.** The stencil face appears in exactly three places on any page: the class mark, the input list head, and the page's own subject name. On a lesson page those are the mark, the rail head and the h1. On a hub the unit name occupies the slot the rail head holds elsewhere, so the count is three there too. *Cited deviation from DIRECTION.md's literal list, kept because the per-page count never rises.* The CSS selector that enforces it is a single rule and is not to be extended again.

**The One Selector Rule.** The stencil is granted by one CSS selector. Any new surface that wants the display voice takes one of the three existing slots; it does not add a fourth.

## Layout

**The frame.** Every page is a floor bar across the top (class mark, year, term nav) and a footer, both hairline-bounded, with the surface between them.

**The lesson page** is a two-column grid: a fixed 312px left rail and a fluid stage area. The rail is permanent and carries all thirty channels of the term, not a window onto them. The stage area holds one plate at max 960px, taped at its two top corners, and a row of floor buttons under it. Inside the plate, a title block, then a meta row ruled into as many cells as the lesson has fields (three, four or five via `tbgrid c3/c4/c5`, so an assessment lesson carrying no repertoire keeps even cells), then a rider grid of a fluid clause column beside a fixed 300px spec column, then **the read** where the lesson has one, then the keep-this block.

**The plate's sections** are the document's own divisions and each is opened by the 2px ink rule: title block, rider, read, keep. The read is where a `guide`, an `explain` and a `worked` sit, in that order and fixed in `build.py` rather than by the data, because the teaching order is that you hear a thing before you are told what it is, and you are shown it done after you have been told. Each read block takes the plate's own left edge, and its content sits in a 66ch column under a full-width rule, so the section divider spans the document and the paperwork inside it does not.

**The term hub** is the one surface where the room is large: max 1180px, unit head and standing line, then the unit's full-width SVG sheet, then the multicore strip running out of its bottom edge, then the assessment bar, the blueprint bar and the full input table. The multicore's `--core-inset` (5%) must equal `SH_X/ROOM_X` in `plots.py` (60 of 1200) or the strip stops reading as plugged into the sheet. Change one and you change the other.

**Home** is max 1180px: heading, the desk plate at max 820px, then the year as a single stack of four rows with a 1px hairline gap doing the ruling. The rows are **not** equal. The three units that are not live fold to one line on a five-track grid (chip, name, focus, assessment meta, status); the live one opens in place and carries its own thirty inputs on the multicore, under a 4px chalk keyline inset on its left edge. The stack stays in unit order, so the open block travels down the page as the year runs and the shape of the surface is itself a position statement. On home the multicore's `--core-inset` is zeroed and replaced by a 38px left gutter for the ruler's own label: the 5% inset exists to line the strip up with the room's two walls, and there is no room on this surface to line it up with.

**Rhythm.** Gutters run 40px at page level, 34px inside the plate, 22px in the rail, 16px at narrow widths. The body grid is 48px, which is the drawing's own unit.

**Responsive.** Three breakpoints, all build work; the comps were rendered at 1440 only.
- **1100:** the rider collapses to one column and the spec blocks lay out side by side at their column width rather than spreading full-width, because a full-width plan drawing would break the rule that the room is small on a lesson page.
- **980:** the rail moves above the plate and becomes a disclosure. It stays in the DOM and open, capped at 42vh with contained scroll, so the disclosure state and what a screen reader is told never disagree. On the hub, the sheet and the multicore pan together inside one contained horizontal scroller at min-width 720px, deliberately: a week boundary must land on a channel boundary, and scrolling them apart would break the alignment that is the whole device.
- **620:** the outcomes column of the input table is dropped, header cell included. It is the first thing a phone can lose because it is on the lesson page and the table's job is finding a lesson.

Mobile is proven at 390: `documentElement.scrollWidth` equals `clientWidth` on home, hub and lesson. No document overflow.

**Print** strips the floor to white, hides rail, floor bar, floor buttons and tape, and gives the plate a 1px black border in place of its torn clip-path.

**Motion.** None is authored anywhere in the system, on purpose: the page is operated with hands busy and there is nothing for an animation to tell it. `prefers-reduced-motion` still nulls animation and transition as a guard.

## Elevation & Depth

**No shadows, no gradients.** Depth is stated three ways and only three ways.

1. **Ground change.** The sheet is a lighter panel physically laid on the floor. That is the only figure/ground step in the system.
2. **Tape.** A torn strip holds something down or marks a row. It is the one thing that reads as attached rather than drawn.
3. **The ghost layer.** On a hub, the other three units are drawn as dashed brackets stepped back by unit distance: a top edge and two side stubs running down to where the live sheet starts, which is what a stack of paper looks like from above.

`box-shadow` appears in the system only as a flat inset keyline, never as a cast shadow.

### Named Rules

**The Ghost Bracket Rule.** A non-live unit is a bracket at 26% (about 2.4:1) with a 5-5 dash, not a faded rectangle. 7 to 10 percent was tried and is about 1.1:1 on this floor, which is absent rather than weak; a full ghost rectangle crosses the live sheet and turns the drawing to mud. The **dash** carries "not live", not the fade. The ghost's *labels* are chalk-dim at 5.76:1 and are not ghosted: the line is the ghost, the label is not.

**The Keyline-Not-Tape Rule.** "The one you have open" is the 4px painted chalk keyline, always: inset on the rail's reading row, top and bottom inset on the hub table's current row, a left inset on home's open unit. Tape says where the class is; the keyline says where you are.

## Shapes

Square corners everywhere. `border-radius` is zero across the entire stylesheet and there is no radius scale to draw from.

Form comes from tearing rather than rounding. Four hand-authored `clip-path` polygons carry it, each tuned to its own size:
- the plate's near-straight torn sheet edge (a document, so the tear is subtle)
- the `--torn-tape` polygon on the plate's 124×32 corner strips
- the rail's current-row strip, torn on all four sides
- the multicore channel, about 30px wide, torn on the **top and bottom edges only**, because tearing all four sides at that width is not a torn strip, it is a jagged blob

Lines come in two weights and no others. 1px is chalk hairline (`--hair` on the floor, `--rule` on the sheet, `stroke-width="1"` in the drawings), 4px is the painted keyline (`border-bottom: 4px solid var(--chalk)` on section heads, inset box-shadows on current rows, `stroke-width="4"` on the sheet's downstage edge). The plate's internal section dividers are 2px solid ink, an in-sheet weight that belongs to the document rather than to the floor.

### Named Rules

**The Torn Ends Rule.** Every edge of tape is torn. A square-cut bar of gaffer colour reads as a rectangle with a colour in it, which is the card this world exists to refuse. The tear polygon is authored per size; do not reuse the 124px polygon on a 30px element.

**The Two Weights Rule.** 1px for what is drawn, 4px for what bounds. A third weight on the floor is a defect.

## Components

### Floor bar and term navigation
The site's one persistent chrome: class mark in stencil, year in dim label caps, then the four terms as bordered channels pushed right. **Style:** hairline border, dim label type, square, transparent. **Hover:** text to chalk, border to chalk-dim. **Active:** filled with the term's tape, ink type at weight 800, border matched to the fill. At narrow widths the nav drops to its own full-width row.

### The rail (input list)
Character: a channel list on a patch bay. Every lesson of the term, numbered from 01, grouped under dim week headers. A row is a 34px number column beside the title.
- **Default:** chalk title, dim number. A lesson with no page yet is *not* dimmed; it is a real lesson in the term and what it lacks is the link, not the standing.
- **Hover (linked rows):** a 5% chalk wash.
- **Taught:** chalk-past type plus a ` ×` after the number.
- **Assessment:** a filled ▪ after the number.
- **Now (where the class is up to):** the term's tape as a torn strip inset from the rail edges, ink type at 800.
- **Reading (the page you are on):** a 4px chalk keyline inset on the left edge, flipping to ink when the row is also taped.
- **Narrow:** becomes a disclosure with a Show/Hide affordance in the head, capped at 42vh with contained scroll.

### The plate
Character: a document taped to the floor.
- **Shape:** square, torn sheet edge via clip-path, no shadow.
- **Background:** sheet; all interior type is ink or ink-dim.
- **Tape:** two corner strips, top left rotated -3.5° and top right rotated 2.5°, sized 124×32 (96×26 below 980).
- **Internal padding:** 34px, dropping to 20px below 980.
- **Rules:** 2px ink under the title block and above the keep block; 1px sheet-rule everywhere else.

### The meta row
A grid ruled into as many cells as the lesson has fields, in three sizes (3, 4 or 5). Dim label caps over a 600-weight value. Below 980 it goes two-up. Never one double-width cell.

### The listen block
A bordered list of tracks: work in 600, artist under it in dim, the locating fact in mono at the right. **The artist line prints only where the meta field has not already said it.** `build.py`'s `by()` suppresses it when a word of the artist appears in the meta string. For authors: `title` is the work, `meta` is the locating fact (an era in some terms, an artist in others), and `artist` renders only when it adds a name the row does not already carry.

**The name of the work is the player**, added 17 August 2026 with the verified repertoire ids. A triangle hangs to the left of the name, and pressing it unfolds the recording on a second grid row directly under that work, as a `youtube-nocookie` frame at 16:9 bounded by a 1px sheet rule. The mark becomes a stop square while it is open, one player at a time in a block, and the row's name is a real link to the recording so the block still works with scripting off.

Three rulings inside that, in the order they were forced:

- **Not permanent frames.** Term 3 input 01 and Term 4 input 08 both carry three works. Embedded outright that is about 500px of another company's chrome sitting on the sheet and the block stops being a list. Folded away, the block is unchanged until a student asks for a track, and nothing is requested from the host until they do.
- **Not a button in its own column.** A 24px control column was built first and cost the work's name 34px in a block that is 240 wide, which put all three of Term 4 input 08's titles onto two lines each. The mark inside the name costs one line's indent and nothing on the rest, and it makes the whole title the target, which is what a tracklist does everywhere else these students have met one.
- **The player is the block's width**, 210px inside the 240px block inside the 300px spec column. Small, and deliberately not broken out of the column: the recording belongs under the work it names. If the room needs it bigger, that is one rule, and it is a decision about the spec column rather than about this block.

### The read: the cue sheet, the long version and the two takes

Added 17 August 2026, joined by a third on 18 August. The blocks in this world that are **read rather than done**, which is the fact that decides everything about them.

None of them is a fourth clause. Every clause carries a `kind` and every kind names where the doing happens (In the room, With the band, On your own, In flat.io); there is no doing in any of these, so none can take one. They are sections of the document instead, siblings of the title block and the keep block, and they take that structure's furniture: the plate's own left edge, and the 2px ink rule that already divides this sheet.

All three are on the sheet rather than the floor because all three are paragraphs. That is the Two Grounds Rule, not a preference.

**The long version** (`explain`) is one block of about 250 words on an input that introduces something a student writes in their book. `LESSON-DEPTH-TRIAGE.md` governs which inputs get one. A label in caps, the explain's own title at the 1.1rem step, then prose at 66ch with optional caps subheads and a list. The list marker is the success criteria's dash, which is now the sheet's one list marker, but without the rule under each item: the criteria are a checklist and are ruled like one, and this is a set inside a paragraph's argument.

**The cue sheet** (`guide`) is a work and the times in it worth stopping at. Four in 123 inputs, one per term. It is a list of works rather than one work with a list under it, because three of the four walk more than one. A work's name is the control that plays it, its locating fact sits in mono at the end of its line, and its cues hang under it: **the time in the 46px gutter the clause numbers use directly above, so one column of figures runs down the whole plate**. Works are separated by a 1px sheet rule; cues are not ruled from each other, because ruling every row of a short list inside an already-ruled section turns the sheet into a spreadsheet.

Four rulings inside it:

- **Only the time is a link.** The cue text stays text, so it can be read off a projector and copied into a book without being pressed by accident. The time is a real `watch?t=` link before site.js makes it a seek, which is the same progressive-enhancement rule the listen block was built on.
- **The player opens above that work's own cues**, so pressing a cue leaves the rest of the list where it was. It is capped at 480px rather than run to the block's width: this sits on a document, and half a metre of another company's chrome is not a document. That cap is a decision about this block and deliberately does not answer the open question about the listen block's 210px player, which is a question about the spec column.
- **Held to 66ch, not to the plate.** Full width throws the artist out to the right margin half a plate from the work it names, and leaves the rule under each work crossing empty sheet.
- **A cue is never a toggle.** Pressing 1:04 has one obvious meaning and closing the player is not it.

**The name of a work is the control, on both blocks that name one.** The listen block established this on 17 August and the guide inherits it rather than inventing a second way to start a player, so `.play` is no longer scoped to `.listen` and `build.py`'s `play_link()` is written once. A student who has learned the control on one block does not meet a button on the next.

**One player at a time on the page**, not one per block. The listen block's original rule was per block, which was complete for every case that existed and wrong for the first new one: two tracks playing over each other in a classroom is the whole room's problem, and it is just as much the room's problem when one is in the cue sheet and the other is in the listen block.

`assets/site.js` is the only script on the site and this is all it does.

**Held by the build:** a work walked through in the cue sheet may not also be a row in the listen block on the same page. All four guide inputs already carry a listen block holding exactly the works their guide walks, so the default outcome of authoring a guide is the same names printed twice on one plate. `assert_no_doubled_work()` fails the build, proven by mutation.

**The two takes** (`worked`) is the same task answered twice, once so it earns and once so it
does not. Added 18 August 2026 for the three inputs the depth triage found where the taught
distinction is a difference between two pieces of writing that look alike on the page: a log
entry against a diary entry, a dot point that earns a mark against one that does not, a
rationale that names its decisions against one that describes its feelings. None of those
survives being described, which is why none of the three took an explain. All three are seen
in one look or not at all.

So the block is a comparison and every part of it is built to be read across. It invents no
furniture:

- **The label row carries the mark value**, joined by a middot, which is what the plate's own
  header line already does with a count and a status (Input 09 of 30, on the desk). Set after
  the question it reads as part of the sentence; right-aligned it lands in the middle of the
  plate, because the reading measure stops at 66ch while the section rule above runs the
  document's full width. A figure out there alone is an orphan, not a column.
- **The question takes the read block's own h3**, the step the explain's title already uses,
  held to 48ch because it is a sentence to read rather than a title to scan.
- **Both specimens are marked, and the two marks are the world's own two line weights.** The
  take that works is bound by the 4px painted keyline; the take that does not is drawn with
  the 1px sheet rule, at the same 18px inset. That is the Two Weights Rule used as an
  argument: 4px bounds what is kept, 1px draws what is not. No fill, no tint and no colour,
  which the sheet does not take anyway, and the label above each says it in words as well, so
  nothing here is carried by a mark alone.
- **A rung is a clause.** A named move with a sentence under it, in the same 46px gutter the
  clause numbers and the cue times use, so one column of figures runs down the whole plate and
  the rungs land on it exactly. Ruled 1px per row like a clause and unlike a cue, because each
  rung carries its own head and unruled they run together. The moves are ALARM's where the
  task is a dot point and the task's own where it is not; what carries is the shape, not the
  vocabulary.
- **The rungs' rules stop at the reading measure**, with the specimen, so neither crosses empty
  sheet. That is the same fault the cue sheet was held to 66ch to avoid.

Two rulings inside it:

- **The failing take is not dimmed and is not folded away.** It is the half a student has to
  study closely, and the page is projected while the room compares the two. Year 10's version
  of this block greys its zero-mark answer; this one does not, because a greyed paragraph on a
  projector in a daylit room is a paragraph nobody reads.
- **Two takes means two.** `assert_worked_complete()` fails the build if the question, the
  model or either half of the failing take is missing, proven by mutation. One answer with its
  reasoning shown is an explain with a quotation in it, and it would print under a heading
  saying two takes with one take under it.

**No script.** Nothing in this block is pressed, so `assets/site.js` is unchanged and still
does one thing. The block is the first read block that needs nothing from it.

### Focus on the sheet
The term's tape is the focus colour, which holds on the floor: every tape reads between 5.26 and 16.78 to 1 against it. **On the sheet it does not.** Tape on cream runs 1.01 to 1 (Term 1), 1.20 (Term 4), 2.58 (Term 3) and 3.20 (Term 2), so in two of the four units a keyboard user would get no visible ring at all. **Inside the plate the ring is ink**, same 3px at the same 2px offset, 16.44 to 1.

This is the ground deciding the mark exactly as it already decides the type: chalk on the floor, ink on the sheet. It is not a second focus token and there is still no separate focus colour. Nothing focusable sat on the sheet at all until the listen block gained a control on 17 August 2026, which is why the gap only surfaced then.

### Buttons
Two families, one per ground.
- **Plate button (primary):** solid ink on sheet, sheet-coloured label caps at 800, 12×20 padding, square. **Hover:** ink lightens to #2C2E31.
- **Plate button (alt):** transparent with a 1px sheet-rule border and ink type. **Hover:** border to full ink, no fill.
- **Floor button:** transparent with a 1px hairline border and chalk type, 10×15 padding. **Hover:** border to chalk-dim. This is the row under the plate.
- **Focus (all interactive elements):** a 3px outline at 2px offset, in the term's tape on the floor and in ink on the sheet. There is no separate focus token; the term colour is the focus colour and the ground supplies it. See **Focus on the sheet** below for why the plate differs and the numbers behind it.

### The multicore (signature)
The term's thirty lessons as one line of equal-width channels running out of the sheet's downstage edge, with a week ruler mirroring its flex geometry exactly so a week boundary lands on a channel boundary. Every channel is the same width and on this surface that is the point: on a multicore the channels *are* equal, and what separates them is what is patched into each. Hairline-bounded cells, mono numbers, a ▪ under an assessment, chalk-past for taught, and the term's tape (torn top and bottom) on the current channel. The "Week" label sits in the 5% gutter, outside the flex row, because a label in the row pushes every week off its channel.

### The unit sheets (signature)
Four SVG drawings, one per unit, all built by `plots.py` on one shared frame: a 1080×250 sheet bounded by a 1px chalk rule, named in its own top corner the way production paperwork is, ghost brackets stepped above it, a 4px painted downstage edge below. **What is shared is the frame, not the drawing.** Inside the frame each unit is the document that unit's musicians actually use: a stage plot, a chord chart, a listening set-up, a cue sheet. Do not force a fifth unit into a floor plan because the first one was one.

### Input table
The full term list as a ruled table: hairline rules, dim mono numbers, dim label headers, week rows as spanning sub-headers. Taught rows go chalk-past; the current row takes the 4px chalk keyline top and bottom plus a ◀ after its number, never a third tape fill.

### The year stack (home)
Four rows on a hairline-gap stack, unequal by design, because equal-weight blocks in a grid are the arrangement the THESIS names and refuses. The three units that are not live fold to a line each: chip, name, focus, assessment meta, and Taught or Ahead at the right. The live unit opens in place and carries its own thirty inputs on the multicore, with the assessment line under a hairline below it. Each row carries its own term colour as a **chip on the unit number** with ink on it, never as a bar across the row. Four coloured bars side by side read as a rainbow. Which unit is open is said three ways and never by the colour: by the size of the block, by the 4px chalk keyline inset on its left edge, and by the words in its corner.

The multicore is reused here rather than a second device being invented, and it is not the room at a fourth scale: a stage box is a real object on its own and does not need the plot drawn above it. Home spends the same two tape acts a hub spends, the desk plate's corner strip and the live channel.

## Do's and Don'ts

### Do:
- **Do** put anything longer than a list on the sheet. Labels, numbers, drawn line and short lists live on the floor; a paragraph does not.
- **Do** state every position and status twice: a marker or keyline plus a word. Colour is never the only carrier.
- **Do** keep the tape budget at two acts per page. A lesson page's three strips are two acts: the corner pair holds one object down, the rail's row marks the row. A hub spends its two on the standing line and the live channel. A fourth mark is a defect.
- **Do** draw structure at `--hair` (3.21:1) and leave texture at `--floor-grid`. If a surface reads over-ruled, shorten the rules' extent.
- **Do** author a torn polygon per element size.
- **Do** treat `--core-inset` in the stylesheet and `SH_X` in `plots.py` as one number in two files.
- **Do** keep `bring` to its closed set of seven: the six instrument, log and headphone values plus "Pens", which comes from the school's own assessment task notification and is used only where a paper is sat under examination conditions. An eighth has to be argued for.
- **Do** self-host every face. Nothing loads from a CDN.

### Don't:
- **Don't** put white type on a tape colour, or a tape colour as type on the floor.
- **Don't** introduce a third line weight on the floor, a corner radius, a gradient, or a cast shadow.
- **Don't** widen the stencil selector. Three places per page; a new surface takes one of the three slots.
- **Don't** add a fourth face. Chivo and Chivo Mono are one superfamily and that is the budget.
- **Don't** cut tape square. A square-cut bar of gaffer colour is the card this world exists to refuse.
- **Don't** render a non-live state as a fade alone. The dash carries "not live"; the fade only accompanies it, and ghost labels stay at full AA.
- **Don't** dim a lesson that has no page yet. It lacks the link, not the standing.
- **Don't** draw the room at a third scale. It is large on the hub, small in a lesson page's spec column, and absent on home.
- **Don't** add motion. The page is operated hands-busy.
- **Don't** add a decorative element to the eyebrow line (see below). It survives on the argument that it is pure state.

### Cited deviations, carried knowingly

**The eyebrow above the heading.** `INPUT 02 OF 30 · ON THE DESK` on a lesson page and `UNIT 2 OF 4 · 30 INPUTS` on a hub sit above the h1, which the craft floor bans. Kept because the line is not decorative: it carries the input number and the live position state, which is the site's core job and the STORY's one promise; it restates nothing in the heading; it is native to production paperwork; and it is in the composition the user approved. The hub's descriptive clause was cut from this line and now reads under the h1 as a deck, because a description above a heading is decoration. **This is a deviation kept for these specific reasons on these two surfaces, not a licence for eyebrows on new surfaces.** Nothing decorative may join the remaining line.

**The stencil on the hub.** DIRECTION.md's literal list is class mark, input list head, lesson title. The hub has no rail head, so the unit name takes that slot. Per-page count stays at three. The selector is closed.

### Known gaps in the system

- **The blueprint sheets do not exist.** `data/course/term2/term.json` carries four sheets flagged `built: false`; no other term carries any. PRODUCT.md lists the composing blueprints under must-carry and the STORY block promises a student can get back to the blueprint, the progression, the voicings and the rules without asking twice. **That half of STORY is unmet.** The rail's foot and the hub's blueprint bar name the missing sheets on one line rather than one dead label each, which is a smaller absence, not a filled one.
- ~~**Home's four unit blocks are equal weight.**~~ **Closed 18 August 2026.** The finish review's ruling was unequal weight, and home was rebuilt to it: the live unit takes the block and carries its own inputs on the multicore, the other three fold to a line each, and the stack stays in unit order. No year-scale drawing was added, which was the explicit part of the ruling.
- **No AT3 exam paper**, so no examination-paper surface exists in the system yet.
- **The type ramp is looser than six roles.** The six above are the roles the
  system reasons in, but `assets/site.css` carries sixteen literal font sizes,
  most of them small steps inside the label and mono bands (.66 to .90rem) plus
  four one-off display sizes. Nothing is broken by it and no size is far from a
  role, but it is a ramp held by hand rather than by tokens. New work takes the
  nearest existing step; it does not add a seventeenth.
- **Rules with no enforcement.** The tape budget, the two line weights, the three stencil places and the closed `bring` set are all conventions held by review, not by the build. `build.py` and `plots.py` validate none of them; only the stencil rule has a single CSS selector that makes widening it a visible act, and only the doubled-work rule has a build guard.
- **Thirty-three explains, four guides and three worked blocks exist.** All three block types are built, documented and rendered, and every input the triage named now carries its content. Term 3 input 09 carries the worked exemplar; Term 1 input 26 (a log entry against a diary) and Term 4 input 19 (naming a decision against describing a feeling) were authored 18 August 2026 against that exemplar's shape. Neither carries `marks`: no AT4 criteria figure was to hand for input 19, and input 26's task has no mark value at all.
- **Cue times have to be measured, and all but one work's are.** Term 1 input 04's cue times were measured off the recordings rather than remembered: chroma against the 24 triads gives the chord grid, self-similarity at every lag from 3 to 20 seconds gives the loop length, and folding tonic-ness onto that period gives where each pass starts. With or Without You measures an 8.73s loop at 110.0 BPM and Someone Like You a 7.11s loop at 135 BPM, both matching the published tempo, which is the check that the method works. **Let It Be could not be fetched**, so it has no cues and stays in the listen block. A guide's cue times are a claim about a recording; they are measured or they wait for an ear. The other three guides were measured on 18 August 2026 and are documented in the handoff: Term 2 input 02 by the same method extended to a 12-bar period, and Term 3 input 14 and Term 4 input 02 by a measured loudness envelope instead, because neither is loop form and `loop.py`'s method does not apply to them at all.
