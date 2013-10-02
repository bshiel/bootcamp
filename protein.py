protein = open('uniprot_sprot.fasta')
count = 0
for line in protein:
    if line.startswith('>') and 'Homo sapien' in line:
        count = count + 1
        
print count 
#change
#more change
