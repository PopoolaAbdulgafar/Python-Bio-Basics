print(week 1: "learning basic python for bioinformatics"

# DAY 1 - VARIABLES
isage_int = 14
isfigure_float = 4.0
iscoming_str = "I am coming"
iscoding_bool = True

print("isage_int")
print("isfigure_float")
print("iscoming_str")
print("iscoding_bool")



# DAY 2 - STRINGS
gene = "brca1"

print(gene.upper())
print(gene.lower())
print(len(gene))


# DAY 3 - BIO STRINGS
gene_name = "TP53"
sequence = "ATGCGCTA"

sequence_length = len(sequence)
gc_ratio = (sequence.count("G") + sequence.count("C")) / sequence_length

print(f"Gene: {gene_name}")
print(f"Length: {sequence_length}")
print(f"GC Ratio: {gc_ratio}")


# DAY 4 - LISTING & INDEXING

This_list = ["apple", "banana", "mango"]
print(This_list)

#APPEND
list = ["apple", "banana", "mango"]
mention = ["pen", "pencil", "erraser"]
list.append(mention)
print(list)


# DAY 5 LOOPING
dna = ["GTTA", "TTGA", "TTGG", "AATG"]
for x in dna:
 print(x)

DAY 6 - DICTIONARY

myfamily = {"child1": {"name": "ayo", "year": 2023}, "child2": {"name": "fatimo", "year": 2005},"child3": {"name": "muye", "year": 2013}}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])


