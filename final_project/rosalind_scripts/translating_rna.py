#!/usr/bin/python3
import sys



args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

protein = []

    ######## Script ########
trans_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
   "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
   "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
   "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
   "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
   "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
   "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
   "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
   "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
   "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
   "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
   "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
   "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
   "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
   "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
   "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

rna = f.readline().strip()
i = 0
while i <= (len(rna)-3):
	codon = rna[i:i+3]
	i+=3
	if trans_map[codon] == "STOP":
		break
	else:
		protein.append(trans_map[codon])
		

protein = "".join(protein)
print(protein)

    
    ########################

f.close()
