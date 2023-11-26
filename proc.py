#!/usr/bin/env python3

from anki.collection import Collection

col = Collection("apkg/collection.anki21")

print("""<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
    """)

for note_id in col.find_notes(""):
    note = col.get_note(note_id)
    print('<div class="card">')
    print(note["Front"])
    print("<hr/>")
    print(note["Back"])
    print(note["Notes"])
    print("</div>")

print("""
        </body>
        </html>
""")
