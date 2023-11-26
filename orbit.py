#!/usr/bin/env python3

import subprocess
import sys
import pathlib
from anki.collection import Collection

import util

def html_to_markdown(html_string):
    try:
        p = subprocess.run(["pandoc", "-f", "html", "-t", "markdown"],
                           input=html_string.encode('utf-8'), check=True,
                           capture_output=True)
        return p.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("Error running pandoc:",
              "error code:", e.returncode,
              "error message:", e.stderr.decode("utf-8"), file=sys.stderr)
        sys.exit()

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

with open("docs/orbit/index.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
      <link rel="stylesheet" href="../style.css">
    </head>
    <body>
    <div class="container">
    """)

    f.write("<ul>")

    for section in util.sections:
        if not section_map[section]:
            f.write(f"<li>{section} (no cards for this section)</li>\n")
        else:
            f.write(f'<li><a href="{util.slugify(section)}">{section}</a></li>\n')

            section_dir = f"docs/orbit/{util.slugify(section)}/"
            pathlib.Path(section_dir).mkdir(exist_ok=True)
            with open(section_dir + "index.html", "w") as g:
                pass

    f.write("</ul>")


    f.write("""
            </div>
            </body>
            </html>
    """)

