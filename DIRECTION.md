# Direction contract

The contract below is emitted verbatim as an HTML comment, as the first child of `<body>`, by `build.py`'s `layout()`. It survives the build and can be audited in any page under `docs/`. Do not reword it to match what got built; if the build diverges, the build is wrong.

```html
<!--
THESIS: The year is the room drawn from above, and every lesson is a numbered input on the list. It refuses the course-site default of equal-weight lesson cards in a grid, where week one and week nine look identical, and it refuses the paper ground all three sibling sites share.
OWN-WORLD: Stage-floor black (#111214), chalk white line (#F2F1EC) for everything drawn on the floor, one fluoro gaffer-tape colour per term (#E8FF3A, #FF2D78, #FF6A1F, #3DFF7D) always carrying black ink. Sustained reading happens inside taped white panels laid on the floor, never as long white prose over the black field. Square corners, no shadows, no gradients, two line weights: a 1px chalk hairline and a 4px painted keyline. Tape ends are torn, never cut square.
STORY: A student sees the room, finds their own position in it, reads what they are doing this lesson off a taped panel, and can get back to the blueprint, the progression, the voicings and the rules, without asking for it twice.
FIRST VIEWPORT: The plan view of the room fills the field, positions numbered and drawn in chalk line. Beside it the input list runs as a ruled channel table, one row per lesson, numbered from 01. The current lesson is the only row with a torn strip of the term's tape across it. The term's own tape colour bounds the plate at the head; the other three terms sit under the plan as ghost line at low opacity.
FORM: The Plot, the stage plot and input list a band hands the sound engineer. Candidate 6 of the grounded list, seed key 8d99cc59. Re-rolled once by the user, then pinned back to The Plot by the user, 16 August 2026; a user-pinned direction beats the roll.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
```

## Why this world, in one paragraph

Year 9 is the year the scaffolding starts coming away: the student is handed a frame in Term 1, a smaller one in Term 2, a smaller one again in Term 4, and what they supply is the music. A stage plot is exactly that artefact. It is the sheet a band hands the sound engineer so that strangers can make something together without rehearsing the logistics, and Term 2's own registered enduring understanding is word for word the same claim: **a form can be a shared agreement that lets strangers play together.** The 12-bar blues is a stage plot. So is a chord chart, so is a timing sheet, and so is the AT2 blueprint pack.

## How each term stays on the plot

The plot must abstract past the band room or it becomes a metaphor doing overtime. It does so by staying what it actually is, a plan of who is doing what and what they are plugged into.

| Term | The plan view is | The input list is |
| --- | --- | --- |
| 1 Like a Version | the band on the floor, positions and parts | the lessons, numbered, plus the chart for each |
| 2 Blues to Jazz | the same band, now with the blues form marked out on it | the lessons, plus the blueprint pack as its own numbered inputs |
| 3 Sounds of Australia | the listening room: what is playing and what to listen for | the works and the writing frame for each |
| 4 Level Up | the cue: the scene along the top, the stems down the side | the layers, which are literally channels |

## Rules this world establishes

1. **Black ink on every tape colour, never white**, and never a coloured type on the black field. The four fluoro tapes are fills and markers only.
2. **Long reading lives in a taped white panel.** White prose over the black floor is for labels and lists, never for a paragraph. This is the projector-in-a-daylit-room rule as much as a style rule.
3. **Position is never carried by colour alone.** The torn tape strip always travels with the word marking the position and with the channel number.
4. **The other three terms are always present as ghost line.** The student is standing on the whole year, and only one set of lines is live. Dropping the ghost layer removes the world's one argument.
5. **Two line weights only.** A 1px chalk hairline for what is drawn, a 4px painted keyline for what bounds. A third weight is a defect.
6. **Tape is torn.** Square-cut ends read as a rectangle with a colour in it, which is the card this world exists to refuse.
7. **No school identity, and no sport.** The court, the scoreboard and the team are not this world. It is a stage, and the reference is production paperwork.

## Anti-references

Year 8's **Tour Tee** is the sharpest, because this cohort has just spent a year inside it. Then Year 10's **Marker Zine**, Year 11's **On Air**, the superseded **Liner Notes / Billing** comps, and the `sample/` **Rehearsal Marks** world rejected during the Year 8 build.

Shown and rejected on the way to this decision, 16 August 2026, and not to be mined for parts: The Select Rail, The Course Overlay, The Struck Numeral (round one); The Court, The Box Wall, The Hoarding, The Exposure Record (round two).

## What was approved, and what was not

- **Comp D (`.impeccable/mocks/comp-d-thedesk.html`) is the governing composition** for every lesson page. Approved by Matthew on 16 August 2026 as "C's plate on A's rail". Its approval sidecar carries what is binding and what is still open.
- **Comps A and C are superseded by D**, which fuses them. Keep them as the record of what was traded away, not as parts bins.
- **Comp B is not approved.** One thing is held from it: its multicore strip, thirty lessons as a single line along the downstage edge, is the starting point for the term hub. Nothing else from B carries.
- **The term hub and the home surface have no approved comp.** They are the first design work of the build session.

## Fonts

Self-host, as all three sibling sites do. Nothing loads from a CDN; the comps use Google Fonts links because they are mocks.

- **Saira Stencil One** is the display voice, in three places only: the class mark, the input list head, and the lesson title.
- **Chivo** carries everything else.
- **Chivo Mono** carries channel numbers, meta fields and any tabular figure.

Two families, since Chivo and Chivo Mono are one superfamily. A third face is a defect.
