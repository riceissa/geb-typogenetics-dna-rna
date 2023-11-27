#!/usr/bin/env python3

import sys
from anki.collection import Collection

import util

col = Collection("apkg/collection.anki21")

section_map = {}

for section in util.sections:
    section_map[section] = []

for note_id in col.find_notes(""):
    note = col.get_note(note_id)
    try:
        section_map[note["Section"]].append(note)
    except KeyError:
        print(f"Card has section name {note['Section']}, but this section isn't in the sections list!", file=sys.stderr)
        sys.exit()

print("""<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
      <link rel="stylesheet" href="../style.css">
    </head>
    <body>
    <div class="container">
    """)

for section in util.sections:
    print(f'<h2>{section}</h2>')
    if not section_map[section]:
        print("<p>There are no cards for this section.</p>")
    for note in section_map[section]:
        print('<div class="card">')

        print('<div class="front">')
        print(note["Front"])
        print("</div>")

        print("<hr/>")

        print('<div class="back">')
        print(note["Back"])
        print("</div>")

        print('<div class="notes">')
        print(note["Notes"])
        print("</div>")

        print("</div>")

print("""
        </div>
        </body>
        </html>
""")
