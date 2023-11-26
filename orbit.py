#!/usr/bin/env python3

import subprocess
import sys

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
