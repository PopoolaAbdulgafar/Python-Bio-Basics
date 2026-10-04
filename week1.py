"""Week 1: Learning basic Python for bioinformatics."""

# DAY 1 - VARIABLES
isage_int = 14
isfigure_float = 4.0
iscoming_str = "I am coming"
iscoding_bool = True

print(isage_int)
print(isfigure_float)
print(iscoming_str)
print(iscoding_bool)


# DAY 2 - STRINGS
gene = "brca1"

print(gene.upper())
print(gene.lower())
print(len(gene))


# DAY 3 - BIOLOGICAL STRINGS
gene_name = "TP53"
sequence = "ATGCGCTA"

sequence_length = len(sequence)
gc_ratio = (sequence.count("G") + sequence.count("C")) / sequence_length

print(f"Gene: {gene_name}")
print(f"Length: {sequence_length}")
print(f"GC Ratio: {gc_ratio}")


# DAY 4 - LISTS AND INDEXING
fruits = ["apple", "banana", "mango"]
print(fruits)

# APPEND
fruits.append("pen")
fruits.append("pencil")
fruits.append("eraser")

print(fruits)


# DAY 5 - LOOPING
dna = ["GTTA", "TTGA", "TTGG", "AATG"]

for sequence in dna:
    print(sequence)


# DAY 6 - DICTIONARIES
myfamily = {
    "child1": {"name": "ayo", "year": 2023},
    "child2": {"name": "fatimo", "year": 2005},
    "child3": {"name": "muye", "year": 2013}
}

for child, details in myfamily.items():
    print(child)
    for key, value in details.items():
        print(f"{key}: {value}")
    for y in obj:
        print(y + ':', obj[y])


