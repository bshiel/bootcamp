sequence= ('AGGCTAGGTTCCAATGCAGTAGCAGT')
A = sequence.count('A')
G = sequence.count('G')
T = sequence.count('T')
C = sequence.count('C')
my_dictionary={'A':A,"G":G,"T":T,'C':C}
print my_dictionary
sequence_length= len(sequence)
GC_content= G + C
percent= GC_content/float(sequence_length)
print percent
