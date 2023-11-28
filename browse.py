#!/usr/bin/env python3

import sys

import util

with open("docs/browse/index.html", "w") as f:

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

    for section in util.sections:
        f.write(f'<h2 id="{util.slugify(section)}">{section}</h2>')
        if not util.section_map[section]:
            f.write("<p>There are no cards for this section.</p>")
        for note in util.section_map[section]:
            f.write('<div class="card">')

            f.write('<div class="front">')
            f.write(note["Front"])
            f.write("</div>")

            f.write("<hr/>")

            f.write('<div class="back">')
            f.write(note["Back"])
            f.write("</div>")

            f.write('<div class="notes">')
            f.write(note["Notes"])
            f.write("</div>")

            f.write("</div>")

    f.write("""
            </div>
            </body>
            </html>
    """)
