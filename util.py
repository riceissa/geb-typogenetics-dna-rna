#!/usr/bin/env python3

from anki.collection import Collection

sections = [
    "Typogenetics",
    "Strands, Bases, Enzymes",
    "Copy Mode and Double Strands",
    "Amino Acids 1",
    "Translation and the Typogenetic Code",
    "Tertiary Structure of Enzymes",
    "Punctuation, Genes, and Ribosomes",
    "Puzzle: A Typogenetical Self-Rep",
    "The Central Dogma of Typogenetics",
    "Strange Loops, TNT, and Real Genetics",
    "DNA and Nucleotides",
    "Messenger RNA and Ribosomes",
    "Amino Acids 2",
    "Ribosomes and Tape Recorders",
    "The Genetic Code",
    "Tertiary Structure",
    "Reductionistic Explanation of Protein Function",
    "Transfer RNA and Ribosomes",
    "Punctuation and the Reading Frame",
    "Recap",
    "Levels of Structure and Meaning in Proteins and Music",
    "Polyribosomes and Two-Tiered Canons",
    "Which Came First – The Ribosome or the Protein?",
    "Protein Function",
    "Need for a Sufficiently Strong Support System",
    "How DNA Self-Replicates",
    "Comparison of DNA’s Self-Rep Method with Quining",
    "Levels of Meaning of DNA",
]

col = Collection("apkg/collection.anki21")

section_map = {}

for section in sections:
    section_map[section] = []

for note_id in col.find_notes(""):
    note = col.get_note(note_id)
    try:
        section_map[note["Section"]].append(note)
    except KeyError:
        print(f"Card has section name {note['Section']}, but this section isn't in the sections list!", file=sys.stderr)
        sys.exit()

# By default, the cards are ordered by the note ID, rather than the "New #"
# that appears in the Anki browse window.  So here we get the card that would
# be generated by the note, find its "New #", and order by that number. This
# way, the website's ordering of cards will match that shown in the Anki deck.
for section in sections:
    section_map[section].sort(key=lambda note: note.cards()[0].due)

def slugify(s):
    '''
    "Slugify" the string s as follows: keep only the characters that are
    alphabetic or numerical, and group them together; all other characters are
    replaced by "-" and squeezed together.
    '''
    s = s.lower()
    s = "".join(c if (c.isalpha() or c.isdigit()) else "-" for c in s)
    s = "-".join(filter(bool, s.split("-")))
    return s

def navbar(levels):
    return (f"""
        <nav>
            <a href="{'../' * levels}">Back to home</a>
        </nav>
    """)
