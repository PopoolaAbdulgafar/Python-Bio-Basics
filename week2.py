print("week 2: working with DNA sequence")

def gc_content(seq):
g = seq.count("G")
c = seq.count("C")
return(g + c) / len(seq) * 100
print(gc_content("AATTGGCC"))
