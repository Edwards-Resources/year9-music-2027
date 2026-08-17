#!/usr/bin/env python3
"""Measure a repeating chord loop: how long it is, and where each pass starts.

A cue time in a guide block is a claim about a recording. A wrong one fails in
front of a class, so they are measured here rather than remembered.

Not a general chord recogniser. It answers one question: given a recording that
sits on a repeating loop, where does each pass of that loop begin?

    yt-dlp -x --audio-format wav --postprocessor-args "-ar 22050 -ac 1" \
        -o "ID.%(ext)s" "https://www.youtube.com/watch?v=ID"
    python3 tools/loop.py ID.wav D

The second argument is the tonic the loop starts on, with a trailing `m` for a
minor tonic. Method:

1. **Chroma.** STFT, folded onto the twelve pitch classes, over 65 Hz to 2 kHz,
   which leaves out the bass mud and the cymbal wash.
2. **Period.** Cosine self-similarity of the chroma at every lag from 3 to 20
   seconds. A repeating loop makes the recording most like itself exactly one
   loop later, so the lag that maximises it is the loop length.
3. **Phase.** Fold every frame's similarity to the tonic triad onto that period.
   The loop begins on chord I, so the fold's peak is where chord I sits in the
   cycle, and every restart is that phase plus a whole number of periods.

The check that it worked is the tempo: four bars of 4/4 at the reported period
should land on the recording's published tempo. Term 1 input 04 measured With or
Without You at 8.73s (110.0 BPM) and Someone Like You at 7.11s (135.0 BPM), both
of which do.

The reported peak is the middle of chord I rather than its downbeat, so a pass
**starts** about an eighth of a period earlier. That correction is printed.

Audio is downloaded to work on and thrown away. Nothing under this repo holds a
recording; the site embeds from the host. Some official uploads refuse to be
fetched at all, in which case the cues wait for someone with the recording and
an ear rather than being guessed at.

Needs numpy and scipy, which is why it lives here and not in build.py. The build
has no dependencies and keeps none.
"""
import sys

import numpy as np
from scipy.io import wavfile
from scipy.ndimage import uniform_filter1d

NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
HOP, WIN = 1024, 4096


def chroma(path):
    sr, x = wavfile.read(path)
    x = x.astype(np.float64)
    if x.ndim > 1:
        x = x.mean(axis=1)
    x /= (np.abs(x).max() or 1)

    n = 1 + (len(x) - WIN) // HOP
    frames = np.lib.stride_tricks.as_strided(
        x, shape=(n, WIN), strides=(x.strides[0] * HOP, x.strides[0]))
    S = np.abs(np.fft.rfft(frames * np.hanning(WIN), axis=1))

    freqs = np.fft.rfftfreq(WIN, 1 / sr)
    keep = (freqs > 65) & (freqs < 2000)
    pc = np.round(12 * np.log2(freqs[keep] / 440.0) + 69).astype(int) % 12

    band = S[:, keep]
    C = np.column_stack([band[:, pc == k].sum(axis=1) for k in range(12)])
    return sr, C / (C.sum(axis=1, keepdims=True) + 1e-9)


def triad(root, minor=False):
    t = np.zeros(12)
    t[[root, (root + (3 if minor else 4)) % 12, (root + 7) % 12]] = 1
    return t / np.linalg.norm(t)


def analyse(path, tonic, minor=False, lo=3.0, hi=20.0):
    sr, C = chroma(path)
    fps = sr / HOP
    N = C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-9)

    best, period = -1.0, None
    for lag in range(int(lo * fps), int(hi * fps)):
        s = float((N[:-lag] * N[lag:]).sum(axis=1).mean())
        if s > best:
            best, period = s, lag

    tone = uniform_filter1d(N @ triad(tonic, minor), size=int(0.4 * fps))
    fold = np.array([tone[k::period].mean() for k in range(period)])
    phase = int(fold.argmax())

    secs = period / fps
    # The fold peaks in the middle of chord I. A pass starts an eighth of a loop
    # earlier, chord I being the first of four bars.
    start = phase / fps - secs / 8
    passes = [(start + i * secs, float(tone[k]))
              for i, k in enumerate(range(phase, len(tone), period))]
    return secs, best, [(t, s) for t, s in passes if t >= 0]


if __name__ == "__main__":
    path, root = sys.argv[1], sys.argv[2]
    secs, sim, passes = analyse(path, NAMES.index(root.rstrip("m")), root.endswith("m"))
    print(f"loop {secs:.2f}s   self-similarity {sim:.3f}   "
          f"{16 * 60 / secs:.1f} BPM as four bars of 4/4")
    print("check that BPM against the recording's published tempo before using any of this\n")
    for t, score in passes:
        print(f"  {int(t) // 60}:{t % 60:05.2f}   tonic {score:.3f}")
