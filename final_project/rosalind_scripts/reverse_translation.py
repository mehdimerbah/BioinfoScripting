#!/usr/bin/python3
import sys
from itertools import product


args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

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

protein = f.readline().strip()

reverse_dict = {} 

aa_keySet = set(trans_map.values())

for key in aa_keySet:
	reverse_dict[key] = []

for key, val in trans_map.items():
	reverse_dict[val].append(key)

#for key, val in reverse_dict.items():
#	print(key, ":", val)

#for aa in protein:
	#for codon in reverse_dict[aa]:

    ########################

f.close()
