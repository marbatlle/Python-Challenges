# Translating RNA into Protein
## http://rosalind.info/problems/prot/

from Bio import Seq

with open('Bioinformatics Stronghold/rosalind_prot.txt', 'r') as f:
    seq = Seq.Seq(f.readline())

result = seq.translate(to_stop=True)
print(result)