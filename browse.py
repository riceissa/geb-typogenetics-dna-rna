#!/usr/bin/env python3

import sys

import util

with open("docs/browse/index.html", "w") as f:

    f.write("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <link rel="stylesheet" href="../base.css">
  </head>
  <body>
    <div class="container">\n""")

    for section in util.sections:
        anchor_link = f'<a href="#{util.slugify(section)}" title="Link to this section" class="heading-marker">#</a>'
        f.write(f'<h2 id="{util.slugify(section)}">{section} {anchor_link}</h2>\n')
        if not util.section_map[section]:
            f.write("<p>There are no cards for this section.</p>\n")
        for note in util.section_map[section]:
            f.write('<div class="card">\n')

            f.write('<div class="front">\n')
            f.write(note["Front"] + "\n")
            f.write("</div>\n")

            f.write("<hr/>\n")

            f.write('<div class="back">\n')
            f.write(note["Back"] + "\n")
            f.write("</div>\n")

            f.write('<div class="notes">\n')
            f.write(note["Notes"] + "\n")
            f.write("</div>\n")

            f.write("</div>\n")

    f.write("""
    </div>
  </body>
</html>\n""")
