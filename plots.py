"""The paperwork, at hub scale. One document per unit.

The first version of this file drew all four units as the same floor plan with
different things standing on it. That was wrong, and it is worth recording how,
so it does not come back: a 12-bar blues is time, not floor space, so a band
standing on a chord progression taped across the floor is a picture no musician
has ever drawn. It read as music-adjacent and meant nothing. That is the failure
DIRECTION.md already names, the metaphor doing overtime.

What is shared is the frame, not the drawing. Every unit is one sheet of
production paperwork: bounded, named in its top corner, with the other three
stacked under it as ghost line and a 4px painted edge along the bottom that the
multicore plugs into. Inside that frame each unit is the document that unit's
musicians actually use.

    1 Like a Version      a stage plot, with the input numbers that tie each
                          source to a line on the input list
    2 Blues to Jazz       a chord chart, twelve bars in three systems, slashes
                          and chord symbols, roman numerals underneath because
                          this one is a teaching chart
    3 Sounds of Australia the listening set-up, the equilateral triangle every
                          stereo reference drawing uses
    4 Level Up            a cue sheet, timecode across the top, stems down the
                          side

Two line weights, as the world allows: a 1px chalk hairline for what is drawn
and a 4px painted keyline for what bounds. At this viewBox the page renders
about 1:1, so 1 and 4 here are 1px and 4px on the floor.
"""

# ---------------------------------------------------------------- the frame

VB_W, VB_H = 1200, 360

# The sheet is 5% in from each side, and --core-inset in site.css is the same
# 5%, so the multicore starts exactly under the sheet's left edge and ends under
# its right one. That alignment is the whole device: the channels have to look
# like they run out of the bottom edge, not like a row of boxes under a picture.
# Change one and you must change the other.
SH_X, SH_Y, SH_W, SH_H = 60, 92, 1080, 250
SH_R = SH_X + SH_W                # 1140
SH_B = SH_Y + SH_H                # 342, the edge the multicore plugs into

CHALK = "#F2F1EC"
DIM = "#8E8F8B"
INK = "#141517"
# The ghost line. Comp B drew the other units at 7 to 10 percent, which is about
# 1.1:1 on this floor and simply is not there. This is 26 percent, about 2.4:1,
# and the dash rather than the fade is what carries "not live" (rule 3: a state
# never rests on the contrast step alone).
GHOST = "rgba(242,241,236,.26)"

UNIT_SHORT = {1: "Like a Version", 2: "Blues to Jazz",
              3: "Sounds of Australia", 4: "Level Up"}
SHEET_NAME = {1: "STAGE PLOT", 2: "CHART", 3: "LISTENING SET-UP", 4: "CUE SHEET"}


def _ghosts(live_n):
    """The other three units, as the sheets left on the desk under this one.

    Each is a bracket rather than a whole rectangle: the top edge and the two
    side stubs running down to where the live sheet begins. That is what a stack
    of paper looks like from above, and it leaves the live sheet completely
    clear, which a full ghost rectangle does not.

    Stepped by unit distance, so the year is in order: the unit next to this one
    sits closest.
    """
    others = sorted((n for n in (1, 2, 3, 4) if n != live_n),
                    key=lambda n: abs(n - live_n))
    out = []
    for depth, n in enumerate(others, start=1):
        inset, top = 18 * depth, SH_Y - 20 * depth
        x1, x2 = SH_X - inset, SH_R + inset
        out.append(
            f'<path d="M{x1} {SH_Y} L{x1} {top} L{x2} {top} L{x2} {SH_Y}" '
            f'fill="none" stroke="{GHOST}" stroke-width="1" stroke-dasharray="5 5"/>'
            f'<text x="{x1 + 10}" y="{top - 7}" fill="{DIM}" '
            f'font-family="Chivo Mono, monospace" font-size="12" '
            f'letter-spacing="1.4">{n} {UNIT_SHORT[n]}</text>')
    return "".join(out)


def _sheet(n):
    """The bounded sheet, its name, and the 4px edge along the bottom.

    Production paperwork is always labelled with what it is, in a corner, so the
    person holding six sheets can find the right one. That is the job of the
    name in the top left; it is not a caption.
    """
    return (
        f'{_ghosts(n)}'
        f'<rect x="{SH_X}" y="{SH_Y}" width="{SH_W}" height="{SH_H}" '
        f'fill="none" stroke="{CHALK}" stroke-width="1"/>'
        f'<line x1="{SH_X}" y1="{SH_B}" x2="{SH_R}" y2="{SH_B}" '
        f'stroke="{CHALK}" stroke-width="4"/>'
        f'<text x="{SH_X + 14}" y="{SH_Y + 22}" fill="{DIM}" '
        f'font-family="Chivo, sans-serif" font-size="10" letter-spacing="2.6">'
        f'{SHEET_NAME[n]}</text>')


def _tag(x, y, num):
    """An input number in a box: how a stage plot ties a source on the drawing
    to a line on the input list."""
    return (f'<rect x="{x}" y="{y}" width="19" height="16" fill="none" '
            f'stroke="{CHALK}" stroke-width="1"/>'
            f'<text x="{x + 9.5}" y="{y + 12}" fill="{CHALK}" '
            f'font-family="Chivo Mono, monospace" font-size="11" '
            f'text-anchor="middle">{num}</text>')


def _lbl(x, y, text, anchor="middle", size=10):
    return (f'<text x="{x}" y="{y}" fill="{DIM}" font-family="Chivo, sans-serif" '
            f'font-size="{size}" text-anchor="{anchor}" letter-spacing="2.2">{text}</text>')


# ------------------------------------------------------------- the four units


def unit1():
    """A stage plot for the five-piece covering a song.

    Drawn the way a plot is drawn: the kit as a kit rather than one circle, amps
    as boxes behind the players who use them, mics as a head on a stand, wedges
    on the edge pointing back, and every source carrying the input number that
    finds it on the list.
    """
    o = [_sheet(1)]
    st = f'fill="none" stroke="{CHALK}" stroke-width="1"'

    # the kit, upstage centre: kick, snare, two toms, hats, two cymbals, throne
    o.append(f'<g {st}>'
             f'<circle cx="600" cy="170" r="21"/>'          # kick
             f'<circle cx="570" cy="142" r="12"/>'          # snare
             f'<circle cx="596" cy="133" r="11"/>'          # rack tom
             f'<circle cx="630" cy="148" r="14"/>'          # floor tom
             f'<circle cx="547" cy="165" r="10"/>'          # hats
             f'<circle cx="560" cy="117" r="13"/>'          # crash
             f'<circle cx="639" cy="120" r="14"/>'          # ride
             f'<path d="M586 198 h28"/></g>')               # throne
    o.append(_lbl(600, 216, "DRUM KIT"))
    o.append(_tag(487, 118, 1) + _tag(487, 140, 2) + _tag(487, 162, 3))

    # backline upstage: bass rig stage left, guitar amp stage right. An amp
    # goes behind the player who uses it; a plot with the guitar cab downstage
    # of the guitarist is a plot nobody could set up from.
    o.append(f'<g {st}><rect x="160" y="128" width="88" height="34"/></g>')
    o.append(_lbl(204, 182, "BASS RIG"))
    o.append(_tag(258, 136, 5))
    o.append(f'<g {st}><rect x="952" y="128" width="88" height="34"/></g>')
    o.append(_lbl(996, 182, "GTR AMP"))
    o.append(_tag(925, 136, 6))

    # keys mid-stage left, on a stand
    o.append(f'<g {st}><rect x="180" y="210" width="126" height="30"/>'
             f'<path d="M204 240 v12 M282 240 v12"/></g>')
    o.append(_lbl(243, 268, "KEYS"))
    o.append(_tag(316, 216, 4))

    # three vocal mics downstage: a head and a stand
    for x, num, lab in [(470, 7, "BASS / VOX"), (700, 8, "LEAD VOX"),
                        (900, 9, "GTR / VOX")]:
        o.append(f'<g {st}><circle cx="{x}" cy="262" r="9"/>'
                 f'<path d="M{x} 271 v13 M{x - 11} 284 h22"/></g>')
        o.append(_lbl(x, 300, lab))
        o.append(_tag(x + 16, 252, num))

    # wedges on the edge, pointing back at the band
    o.append(f'<g {st}><path d="M430 312 L500 312 L486 338 L444 338 Z"/>'
             f'<path d="M700 312 L770 312 L756 338 L714 338 Z"/></g>')
    o.append(_lbl(422, 330, "WEDGE 1", anchor="end", size=9))
    o.append(_lbl(778, 330, "WEDGE 2", anchor="start", size=9))
    return "".join(o)


def unit2():
    """A 12-bar blues chart: three systems of four bars, slashes and chord
    symbols, roman numerals underneath.

    Three by four rather than twelve across, because that is how a blues chart
    is written and it is how you learn to feel where bar 5 and bar 9 arrive. The
    roman numerals are an analysis layer a teacher adds; a working chart would
    not carry them, and this one is a teaching chart.
    """
    chords = ["F7", "F7", "F7", "F7", "B♭7", "B♭7",
              "F7", "F7", "C7", "B♭7", "F7", "F7"]
    romans = ["I", "I", "I", "I", "IV", "IV", "I", "I", "V", "IV", "I", "I"]
    o = [_sheet(2)]
    # A chart is written at reading width and centred on the page, not stretched
    # to the full sheet. Bars this wide stop reading as bars.
    left, right = 200, 1000
    o.append(f'<text x="{left}" y="{SH_Y + 40}" fill="{CHALK}" '
             f'font-family="Chivo, sans-serif" font-size="16" font-weight="700" '
             f'letter-spacing="1.2">12-bar blues in F</text>')
    o.append(f'<text x="{right}" y="{SH_Y + 40}" fill="{DIM}" '
             f'font-family="Chivo Mono, monospace" font-size="12" '
             f'text-anchor="end" letter-spacing="1.4">swing &#183; 4/4</text>')

    barw = (right - left) / 4
    for row in range(3):
        y = SH_Y + 80 + row * 64          # the line this system is written on
        o.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" '
                 f'stroke="{CHALK}" stroke-width="1"/>')
        for b in range(4):
            i = row * 4 + b
            bx = left + barw * b
            o.append(f'<line x1="{bx:.1f}" y1="{y - 15}" x2="{bx:.1f}" y2="{y + 15}" '
                     f'stroke="{CHALK}" stroke-width="1"/>')
            o.append(f'<text x="{bx + 10:.1f}" y="{y - 23}" fill="{CHALK}" '
                     f'font-family="Chivo, sans-serif" font-size="15" '
                     f'font-weight="700">{chords[i]}</text>')
            o.append(f'<text x="{bx + barw / 2:.1f}" y="{y + 29}" fill="{DIM}" '
                     f'font-family="Chivo Mono, monospace" font-size="11" '
                     f'text-anchor="middle" letter-spacing="1">{romans[i]}</text>')
            # four beats, written as slashes, which is what a chart puts there
            for s in range(4):
                sx = bx + barw * (s + 1) / 5
                o.append(f'<line x1="{sx - 4:.1f}" y1="{y + 7}" x2="{sx + 4:.1f}" '
                         f'y2="{y - 7}" stroke="{CHALK}" stroke-width="1"/>')
        o.append(f'<line x1="{right:.1f}" y1="{y - 15}" x2="{right:.1f}" y2="{y + 15}" '
                 f'stroke="{CHALK}" stroke-width="1"/>')
        if row == 2:                      # final double bar
            o.append(f'<line x1="{right - 6:.1f}" y1="{y - 15}" x2="{right - 6:.1f}" '
                     f'y2="{y + 15}" stroke="{CHALK}" stroke-width="1"/>')
    return "".join(o)


def unit3():
    """The listening set-up: the equilateral triangle.

    The drawing every stereo reference uses, and the right sheet for a listening
    unit because where you sit decides what you can hear. Both speakers the same
    distance from the seat as they are from each other, toed in, sixty degrees
    at the seat.
    """
    lx, rx, sy = 336, 864, 158            # the speakers
    px, py = 600, 300                     # the listening position
    st = f'fill="none" stroke="{CHALK}" stroke-width="1"'
    o = [_sheet(3)]

    o.append(f'<path d="M{lx} {sy} L{rx} {sy} L{px} {py} Z" {st}/>')
    # equal sides, ticked the way a plan marks them
    for x1, y1, x2, y2 in [(lx, sy, rx, sy), (lx, sy, px, py), (rx, sy, px, py)]:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o.append(f'<path d="M{mx - 5:.0f} {my - 6:.0f} l10 12" {st}/>')

    # the speakers, each a cabinet rotated to face the seat with its driver on
    # the face. Toe-in is the whole point of the drawing, so it has to be
    # visible that they are aimed rather than merely placed.
    import math
    for x in (lx, rx):
        a = math.degrees(math.atan2(py - sy, px - x))
        o.append(f'<g {st} transform="translate({x},{sy}) rotate({a:.1f})">'
                 f'<rect x="-30" y="-19" width="56" height="38"/>'
                 f'<circle cx="14" cy="0" r="10"/></g>')
    o.append(_lbl(lx - 17, sy - 40, "LEFT"))
    o.append(_lbl(rx + 17, sy - 40, "RIGHT"))

    # the seat, and the sixty degrees at it
    o.append(f'<rect x="{px - 16}" y="{py - 14}" width="32" height="28" fill="{CHALK}"/>')
    o.append(f'<text x="{px}" y="{py + 6}" fill="{INK}" '
             f'font-family="Chivo Mono, monospace" font-size="14" '
             f'text-anchor="middle">1</text>')
    o.append(f'<path d="M{px - 26} {py - 46} A 52 52 0 0 1 {px + 26} {py - 46}" {st}/>')
    o.append(f'<text x="{px}" y="{py - 54}" fill="{CHALK}" '
             f'font-family="Chivo Mono, monospace" font-size="13" '
             f'text-anchor="middle">60&#176;</text>')
    o.append(_lbl(px, py + 34, "THE SEAT YOU LISTEN FROM"))
    o.append(_lbl(px, sy - 40, "ALL THREE SIDES THE SAME LENGTH", size=9))
    return "".join(o)


def unit4():
    """A cue sheet: timecode across the top, stems down the side.

    The one unit whose paperwork really is a grid, because what is being laid
    out is time. The four sections are the picture the music has to land on, and
    a bar in a row means that stem is playing there.
    """
    stems = ["DRUMS", "BASS", "PAD", "LEAD"]
    plays = {0: (2, 3), 1: (1, 2, 3), 2: (0, 1, 2), 3: (2,)}
    times = ["0:00", "0:15", "0:30", "0:45", "1:00"]
    gutter, head = 132, 44
    gx, gw = SH_X + gutter, SH_W - gutter
    rowh = (SH_H - head) / len(stems)
    o = [_sheet(4)]

    o.append(f'<line x1="{gx}" y1="{SH_Y}" x2="{gx}" y2="{SH_B}" '
             f'stroke="{CHALK}" stroke-width="1"/>')
    o.append(f'<line x1="{SH_X}" y1="{SH_Y + head}" x2="{SH_R}" y2="{SH_Y + head}" '
             f'stroke="{CHALK}" stroke-width="1"/>')

    for i, t in enumerate(times):
        x = gx + gw * i / 4
        anchor = "start" if i == 0 else "end" if i == 4 else "middle"
        o.append(f'<text x="{x + (4 if i == 0 else -4 if i == 4 else 0):.1f}" '
                 f'y="{SH_Y + 20}" fill="{CHALK}" '
                 f'font-family="Chivo Mono, monospace" font-size="11" '
                 f'text-anchor="{anchor}">{t}</text>')
        if 0 < i < 4:
            o.append(f'<line x1="{x:.1f}" y1="{SH_Y + 26}" x2="{x:.1f}" y2="{SH_B}" '
                     f'stroke="{CHALK}" stroke-width="1"/>')
    for i, lab in enumerate(["ESTABLISH", "BUILD", "HIT", "FALL"]):
        o.append(_lbl(gx + gw * (i + 0.5) / 4, SH_Y + head - 12, lab, size=9))

    for i, s in enumerate(stems):
        y = SH_Y + head + rowh * i
        if i:
            o.append(f'<line x1="{SH_X}" y1="{y:.1f}" x2="{SH_R}" y2="{y:.1f}" '
                     f'stroke="{CHALK}" stroke-width="1"/>')
        mid = y + rowh / 2
        o.append(_tag(SH_X + 16, mid - 8, i + 1))
        o.append(f'<text x="{SH_X + 46}" y="{mid + 4:.1f}" fill="{DIM}" '
                 f'font-family="Chivo, sans-serif" font-size="11" '
                 f'letter-spacing="2.2">{s}</text>')
        for q in plays[i]:
            x = gx + gw * q / 4
            o.append(f'<rect x="{x + 9:.1f}" y="{mid - 5:.1f}" '
                     f'width="{gw / 4 - 18:.1f}" height="10" fill="{CHALK}"/>')
    return "".join(o)


LARGE = {1: unit1, 2: unit2, 3: unit3, 4: unit4}

ALT = {
    1: ("Stage plot for a five-piece band: drum kit upstage centre on inputs 1 "
        "to 3, keys on input 4, bass rig on 5 and guitar amp on 6, and three "
        "vocal mics downstage on inputs 7 to 9, with two monitor wedges on the "
        "front edge. The other three units are stacked behind it as dashed line."),
    2: ("A 12-bar blues chart in F, written as three systems of four bars with "
        "slash marks for the beats: four bars of F7, two of B flat 7, two of "
        "F7, then C7, B flat 7, F7 and F7, with the roman numerals one, four "
        "and five underneath. The other three units are stacked behind it as "
        "dashed line."),
    3: ("The listening set-up drawn as an equilateral triangle: left and right "
        "speakers toed in toward one listening position, all three sides the "
        "same length, sixty degrees at the seat. The other three units are "
        "stacked behind it as dashed line."),
    4: ("A cue sheet: timecode from 0:00 to 1:00 across the top over four "
        "sections, establish, build, hit and fall, and four numbered stems down "
        "the side, drums, bass, pad and lead, with a bar showing where each one "
        "plays. The other three units are stacked behind it as dashed line."),
}


def large(n):
    """The sheet for unit n, at hub scale."""
    return (f'<svg class="plot-large" viewBox="0 0 {VB_W} {VB_H}" '
            f'role="img" aria-label="{ALT[n]}">{LARGE[n]()}</svg>')


# ----------------------------------------------------------- the small plate
# comp D puts a small drawing in the lesson page's spec column and keeps the
# large one for the hub. Same rule about being a real document applies: this is
# the stage plot reduced, not a diagram of circles with instrument names on it.


SMALL_ALT = ("Small stage plot: drum kit upstage centre on inputs 1 to 3, keys "
             "on 4, bass rig on 5 and guitar amp on 6, three vocal mics "
             "downstage on 7 to 9, and two wedges on the front edge.")


def small_stage():
    """The plot, reduced to fit a 240px column and still be read across a room.

    Everything that survives the reduction is load-bearing: the kit still has
    more than one drum in it, the amps are still upstage of their players, and
    every source still carries its input number, because the number is what the
    drawing is for.
    """
    ink, dim = "#141517", "#5D5F63"
    st = f'fill="none" stroke="{ink}" stroke-width="1"'
    n = (f'<g fill="{ink}" font-family="Chivo Mono, monospace" font-size="8" '
         f'text-anchor="middle">')
    o = [f'<rect x="8" y="8" width="204" height="118" {st}/>',
         f'<line x1="8" y1="126" x2="212" y2="126" stroke="{ink}" stroke-width="2"/>']
    # the kit
    o.append(f'<g {st}><circle cx="110" cy="44" r="11"/><circle cx="95" cy="30" r="6"/>'
             f'<circle cx="109" cy="26" r="6"/><circle cx="126" cy="33" r="7"/>'
             f'<circle cx="88" cy="42" r="5"/></g>')
    o.append(f'{n}<text x="110" y="47">1</text></g>')
    # backline, upstage of its players
    o.append(f'<g {st}><rect x="26" y="24" width="30" height="14"/>'
             f'<rect x="164" y="24" width="30" height="14"/></g>')
    o.append(f'{n}<text x="41" y="34">5</text><text x="179" y="34">6</text></g>')
    # keys
    o.append(f'<g {st}><rect x="26" y="62" width="40" height="12"/></g>')
    o.append(f'{n}<text x="46" y="71">4</text></g>')
    # three mics on stands
    for x, num in [(104, 7), (140, 8), (176, 9)]:
        o.append(f'<g {st}><circle cx="{x}" cy="88" r="5"/><path d="M{x} 93 v7"/></g>')
        o.append(f'{n}<text x="{x}" y="{108}">{num}</text></g>')
    # wedges on the edge
    o.append(f'<g {st}><path d="M84 112 h26 l-5 12 h-16 Z"/>'
             f'<path d="M150 112 h26 l-5 12 h-16 Z"/></g>')
    # One label, on the left where the floor is empty. The drawing carried
    # "STAGE PLOT" in its own corner as well as in the heading above it, and
    # "DOWNSTAGE EDGE" ran straight through the right-hand wedge at this size.
    o.append(f'<g fill="{dim}" font-family="Chivo, sans-serif" font-size="7" '
             f'letter-spacing="1.1"><text x="14" y="121">DOWNSTAGE</text></g>')
    return (f'<svg viewBox="0 0 220 134" width="100%" role="img" '
            f'aria-label="{SMALL_ALT}">{"".join(o)}</svg>')
