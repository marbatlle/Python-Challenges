# Computing GC Content
## http://rosalind.info/problems/gc/


from Bio import SeqIO

def max_GC(file_path):

    with open(file_path, "r") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
        GC_dict = {}
        GC_cont = 0

        for read in list(range(len(records))):
            seq_read = records[read].seq
            GC = 0
            for i in seq_read:
                if i == "G" or i =="C":
                    GC +=1
                else:
                    continue
            GC_cont = (GC/len(seq_read))*100
            GC_dict[records[read].id] = round(GC_cont,6)

        GC_dict_list = GC_dict.values()
        for key,val in GC_dict.items():
            if val == max(GC_dict_list):
                return (key +'\n' + str(val))
                 
       
print(max_GC("Bioinformatics Stronghold/5_GC.fasta"))
    