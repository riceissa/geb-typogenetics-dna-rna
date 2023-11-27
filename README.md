# geb-typogenetics-dna-rna
Flashcards for the Typogenetics/DNA/RNA sections in Douglas Hofstadter's Gödel, Escher, Bach

Cards created while reading Douglas Hofstadter's _Gödel, Escher, Bach: an Eternal Golden Braid_ (GEB). Chapter XVI: Self-Ref and Self-Rep. pp. 504–532.

## Installation/generation

This section is only relevant if you want to compile the website locally for development purposes.

You will need the command-line programs `unzip` and `pandoc` in order to run the following commands.
If you don't have them, on Ubuntu you can just run `sudo apt install unzip pandoc`.
Also, you will need to install the `anki` Python Pip package. To do this,
you can run `python3 -m pip install -U anki`.

First download the `.apkg` file into the main directory, and name it `geb.apkg`. Then run the following commands:

```bash
# .apkg file is actually secretly a zip file. so unzip its contents to a directory called apkg/
unzip -d apkg/ geb.apkg

# Remove unneeded files
rm apkg/meta
rm apkg/collection.anki2

# Rename images/other media files to their correct locations
./media.py

# Generate the browse page
./proc.py > docs/browse/index.html

# Generate the Orbit pages
./orbit.py
```
