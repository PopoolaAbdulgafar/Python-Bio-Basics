"""Week 2: Basic Python concepts for bioinformatics."""

# DAY 7 - CONDITIONS

seq = "ATGCGCATTAAGCGT"
gc_count = seq.count("G") + seq.count("C")
total = len(seq)
gc_content = (gc_count / total) * 100

print(f"GC content: {round(gc_content, 1)}%")

if gc_content > 60:
    print("GC-rich")
elif gc_content > 40:
    print("AT-rich")
else:
    print("GC content is between 0 and 40%")


# DAY 8 - FILE WRITING AND READING

with open("sequence.txt") as file:
    for sequence in file:
        sequence = sequence.strip()
        print(f"Sequence: {sequence}, Length: {len(sequence)}")


# DAY 9 - FUNCTIONS

def gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    gc_count = sequence.upper().count("G") + sequence.upper().count("C")
    return (gc_count / len(sequence)) * 100


print(gc_content("ATGCCGTCAGGC"))


# DAY 10 - ERROR HANDLING

try:
    print(x)
except NameError:
    print("The variable 'x' is not defined.")
finally:
    print("The try-except block is finished.")


# DAY 11 - MODULES

import math

print(math.sqrt(16))


# DAY 12 - JUPYTER NOTEBOOK PRACTICE
# Practice the same Python concepts inside a Jupyter Notebook.




