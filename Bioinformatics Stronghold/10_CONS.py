# Consensus and Profile
## http://rosalind.info/problems/cons/

## Consensus String: is a string formed by taking the most common symbol at each position


## Consensus String: is a string formed by taking the most common symbol at each position

# Fasta File to list of sequences
from Bio import SeqIO
import numpy as np

def fasta_to_seqlist(path):
    with open(path, "r") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
        seq_list = []
        for read in list(range(0,len(records))):
            seq = records[read].seq
            seq_list.append(seq)
    return seq_list

seq_list = fasta_to_seqlist("Bioinformatics Stronghold/10_CONS.txt")

# Seq list to matrix
matrix = []
for i in seq_list:
    matrix.append([j for j in i])
M = np.array(matrix).reshape(len(matrix),len(matrix[0]))

# Seq Matrix to Profile Matrix
A,C,G,T = [],[],[],[]
for i in range(len(matrix[0])):
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for j in M[:,i]:
        if j == "A":
            A_count += 1
        elif j == "C":
            C_count += 1
        elif j == "G":
            G_count += 1
        elif j == "T":
            T_count += 1
    A.append(A_count)
    C.append(C_count)
    G.append(G_count)
    T.append(T_count)

profile_matrix = {"A": A, "C": C, "G": G, "T": T}


# Profile Matrix to Consense Sequence
P = []
P.append(A)
P.append(C)
P.append(G)
P.append(T)
profile = np.array(P).reshape(4, len(A))
consensus = []
for i in range(len(A)):
    if max(profile[:,i]) == profile[0,i]:
        consensus.append("A")
    elif max(profile[:,i]) == profile[1,i]:
        consensus.append("C")
    elif max(profile[:,i]) == profile[2,i]:
        consensus.append("G")
    elif max(profile[:,i]) == profile[3,i]:
        consensus.append("T")


# Print Results

out_file = open('/home/marbatlle/Documents/rosalind/Bioinformatics Stronghold/10_CONS_Out','w')

out_file.write("".join(consensus)+'\n')
out_file.write("A: "+" ".join([str(i) for i in A])+'\n')
out_file.write("C: "+" ".join([str(i) for i in C])+'\n')
out_file.write("G: "+" ".join([str(i) for i in G])+'\n')
out_file.write("T: "+" ".join([str(i) for i in T])+'\n')


out_file.close()