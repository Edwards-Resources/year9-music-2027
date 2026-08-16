# Approval: comp D, The Desk

**Approved by Matthew, 16 August 2026**, as the governing composition for the Year 9 site.

## What was chosen and why

Comp D is a fusion, not a fresh comp. Matthew was shown A, B and C on the same lesson and chose **"C's plate on A's rail"**, which comp D renders so that what is approved is a page rather than a description.

- **From A**: the input list as a permanent left rail carrying all 30 channels of the term, with the current lesson struck by a torn strip of the term's tape.
- **From C**: the lesson itself as one document plate taped to the floor, with the stencil title block and the five-field meta row.
- **From B**: nothing on this surface. B's multicore strip is held for the term hub, where the plan drawing earns its space.

## What each comp was, for the record

| Comp | Composition | Verdict |
| --- | --- | --- |
| A, The Patch Bay | Input list leads, plan reduced to a corner plate | Best working page; its rail topology is structurally On Air's, which was the argument against it |
| B, The Plan | Plan view leads, 30 lessons as a multicore along the downstage edge | Freshest device; the plan does not earn the first viewport on a lesson page. **Hold the multicore for the term hub** |
| C, The Rider | The lesson as one document plate, stencil title block | Most character; the black floor recedes almost entirely, so the world's ground is lost |
| D, The Desk | C's plate on A's rail | **Approved** |

## Approved, and binding on the build

- The **left rail is permanent** and carries every lesson of the term, not a window onto it.
- The **plate is the reading surface**. Long prose never sits on the black floor.
- The **stencil face is the display voice**, and it appears in three places only: the class mark in the floor bar, the input list head, and the lesson title. It is not a heading face for the plate's interior.
- The **torn tape appears twice per page at most**: once on the rail's current row, once holding the plate down. A third strip is a defect.
- The **plan drawing is small and lives in the spec column** on a lesson page. It is only large on the term hub.

## Not approved and not yet decided

- **B's ghost plans** of the other three terms rendered weakly at 7 to 10 percent opacity. The rule in DIRECTION.md stands, but the device needs rebuilding on the term hub before it is trusted.
- **The term hub itself has no approved comp.** B is the starting point, not the approval.
- **The home surface has no comp at all.**
- **Mobile is unverified.** The comps were rendered at 1440 only; the preview pane serves these as static snapshots and its viewport emulation did not apply, so no mobile claim is made here. Responsive is a build concern and the first build must prove it.

## Defect found and fixed in the comp round

The rail's "already taught" state was set at `#6C6E72` on `#111214`, about 3.4:1, which fails AA for body text. Raised to `#9A9B97` (about 7.4:1) with the strike marker kept, so the state still reads as past without depending on the contrast step alone.
