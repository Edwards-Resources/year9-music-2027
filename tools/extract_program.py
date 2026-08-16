#!/usr/bin/env python3
"""Extract the lesson skeleton from the four registered unit programs.

    python3 tools/extract_program.py

Reads the .docx unit programs, writes data/course/termN/term.json. Standard
library only, same reason as build.py.

What it takes, per learning-experience row:

    week            from the "Week N: " prefix on the CONTENT cell
    title           the rest of that first line
    contentCode     the dot point code that follows, e.g. L10, P15, C5
    contentPoint    the dot point's own wording
    enduring        the ENDURING UNDERSTANDING cell
    intention       the LI, from the "LI/SC:" line
    criteria        the SC, from the same line, split on " I can "
    steps           the learning-experience paragraphs, teacher-facing
    resources       the "Resources:" line

What it deliberately leaves behind:

    the LEARNING ADJUSTMENTS column. Adjustments are teacher-side only
    (PRODUCT.md, confirmed 16 August 2026); none of it reaches the site.
    the REGISTRATION column, the school name, and everything in the front
    matter that names the school.

`steps`, `intention` and `criteria` come out of the program in the teacher's
voice and are NOT student-facing prose. A lesson only gets a page once its
`body` has been authored; the extractor never writes `body`. It also never
overwrites an existing lesson's authored fields: rerun it as often as you like.
"""

import json
import os
import re
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "course")
PROGRAMS = os.path.join(
    os.path.expanduser("~"),
    "Claude/Projects/School Master/Year 9 (2027)/Program and Assessment/Unit Programs",
)

UNITS = [
    ("term1", "Music7-10_Y9_UnitProgram_Term1_LikeAVersion.docx"),
    ("term2", "Music7-10_Y9_UnitProgram_Term2_BluesToJazz.docx"),
    ("term3", "Music7-10_Y9_UnitProgram_Term3_SoundsOfAustralia.docx"),
    ("term4", "Music7-10_Y9_UnitProgram_Term4_LevelUp.docx"),
]

# The dot point prefix says which strand the row is delivering, and the strand
# says which pair of outcome codes it sits under. Only the ten real codes exist
# (PRODUCT.md), so this map is exhaustive by design.
STRAND_OUTCOMES = {
    "P": ["MU5-PER-01", "MU5-PER-02"],
    "L": ["MU5-LIS-01", "MU5-LIS-02"],
    "C": ["MU5-COM-01", "MU5-COM-02"],
}

# Authored fields the extractor must never clobber on a rerun.
AUTHORED = ("body", "listen", "plot", "bring", "repertoire")


def cell_paras(tc):
    out = []
    for p in tc.iter(W + "p"):
        t = "".join(n.text or "" for n in p.iter(W + "t")).strip()
        if t:
            out.append(t)
    return out


def tables(path):
    root = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml"))
    for tbl in root.find(W + "body").iter(W + "tbl"):
        yield [[cell_paras(tc) for tc in tr.findall(W + "tc")] for tr in tbl.findall(W + "tr")]


def is_lesson_table(rows):
    return bool(rows) and rows[0] and rows[0][0] and rows[0][0][0].strip().upper() == "CONTENT"


def split_li_sc(line):
    """'LI – We are learning to X. SC – I can A. I can B.' into its two halves.
    The programs use an en dash after LI and SC throughout."""
    m = re.search(r"LI\s*[–-]\s*(.*?)\s*SC\s*[–-]\s*(.*)$", line, re.S)
    if not m:
        return "", []
    intention = m.group(1).strip()
    sc = m.group(2).strip()
    # Success criteria are written as one run of "I can ..." sentences.
    parts = [p.strip() for p in re.split(r"(?<=\.)\s+(?=I can )", sc) if p.strip()]
    return intention, parts or ([sc] if sc else [])


def assessment_event(title):
    """True only for the lessons where the task is actually done or handed in,
    which are the rows the input list marks with a square.

    The unit programs also title the lesson that *issues* a task "AT2 issued,
    both parts at once", and lessons about a task ("AT1 repertoire locked",
    "AT3 feedback"). Those are ordinary teaching and the comp does not mark
    them, so the rule needs both halves: an AT code, and a word that means the
    doing of it rather than the talking about it.
    """
    if not re.match(r"AT\d", title):
        return False
    if "issued" in title.lower():
        return False
    return bool(re.search(r"\b(due|performances?|sat)\b", title, re.I))


def parse_content(cell):
    """['Week 1: The 12-bar blues, heard and counted', 'L10 How genre ... '] ->
    (1, title, 'L10', dot point wording)."""
    head = cell[0] if cell else ""
    m = re.match(r"\s*Week\s+(\d+)\s*:\s*(.*)$", head)
    week, title = (int(m.group(1)), m.group(2).strip()) if m else (None, head.strip())
    code, point = "", ""
    if len(cell) > 1:
        m = re.match(r"\s*([PLC]\d+)\s+(.*)$", cell[1], re.S)
        if m:
            code, point = m.group(1), m.group(2).strip()
        else:
            point = cell[1].strip()
    return week, title, code, point


def parse_experiences(cell):
    steps, intention, criteria, resources = [], "", [], []
    for para in cell:
        if para.startswith("LI/SC:"):
            intention, criteria = split_li_sc(para[len("LI/SC:"):])
        elif para.startswith("Resources:"):
            resources = [r.strip() for r in re.split(r"(?<=\.)\s+", para[len("Resources:"):].strip()) if r.strip()]
        else:
            steps.append(para)
    return steps, intention, criteria, resources


def extract(term_id, filename):
    path = os.path.join(PROGRAMS, filename)
    lessons, number = [], 1
    for rows in tables(path):
        if not is_lesson_table(rows):
            continue
        for row in rows[1:]:
            week, title, code, point = parse_content(row[0])
            steps, intention, criteria, resources = parse_experiences(row[1])
            lessons.append({
                "number": number,
                "week": week,
                "title": title,
                "contentCode": code,
                "contentPoint": point,
                "assessmentEvent": assessment_event(title),
                "outcomes": STRAND_OUTCOMES.get(code[:1], []),
                "intention": intention,
                "criteria": criteria,
                "steps": steps,
                "resources": resources,
                "enduring": (row[2][0] if row[2] else ""),
            })
            number += 1
    return lessons


def merge(existing, fresh):
    """The program is the spine, so its fields win on a rerun. Anything authored
    into the lesson by hand is carried across untouched."""
    by_number = {l["number"]: l for l in existing.get("lessons", [])}
    out = []
    for l in fresh:
        old = by_number.get(l["number"], {})
        for k in AUTHORED:
            if k in old:
                l[k] = old[k]
        out.append(l)
    return out


def main():
    for term_id, filename in UNITS:
        path = os.path.join(DATA, term_id, "term.json")
        if not os.path.exists(path):
            raise SystemExit(f"missing {path}: write the term's own header fields first")
        with open(path, encoding="utf-8") as f:
            term = json.load(f)
        fresh = extract(term_id, filename)
        term["lessons"] = merge(term, fresh)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(term, f, ensure_ascii=False, indent=2)
            f.write("\n")
        authored = sum(1 for l in term["lessons"] if l.get("body"))
        weeks = sorted({l["week"] for l in term["lessons"] if l["week"]})
        print(f"{term_id}: {len(term['lessons'])} lessons, weeks {weeks[0]} to {weeks[-1]}, "
              f"{authored} with an authored body")


if __name__ == "__main__":
    main()
