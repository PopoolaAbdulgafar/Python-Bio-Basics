print("week 2:")

DAY 7 CONDITION

seq = "ATGCGCATTAAGCGT"
GC = 7
total = 15
per = (GC/total)*100
print(round(per, 1))
if per > 60:
    print("GC-rich")
elif per > 40:
    print("AT-rich")
else:
    print("GC is betw 40 and 60")





DAY 8 FILE WRITE & READING

with open("sequence.txt") as f:
    for x in f:
        seq = x.strip()
        print(f"sequence: {seq}, length: {len(seq)}")




DAY 9 FUNCTION

def gc_content(seq):
        count = 0
    
        for base  in  seq:
            if base == "G":
                count += 1
            elif base == "c":
                count += 1
        return count
print(gc_content("ATGCCGTCAGGC"))




DAY 10 - ERROR HANDLING

try:
    print(x)
except:
    print("wow")
finally:
    print("the 'try except' is finished")



# DAY 11 - MODULES
import math

print(math.sqrt(16))



# DAY 12
# Practice the same codes inside Jupyter Notebook



