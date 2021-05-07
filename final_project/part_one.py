#!/usr/bin/env python3
import sys
import re


args = sys.argv
if len(args) == 1:
    print('Please Specify your Fasta filename\nUsage: ./script.py <path/to/fasta>')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

    ######## Script ########
def readFasta(filename):
	"""This function reads in a fasta file and stores the sequences in a dictionary
	seqDict = {'SeqID' : 'SEQ'}"""
	entries = {}
	for line in f:
	    if '>' in line:
	        seq_id = line.strip()[1:]
	        entries[seq_id] = []
	    else:
	        stripped = list(line.strip("\n"))
	        entries[seq_id].extend(stripped)

	for key,val in entries.items():
		entries[key] = "".join(val)

	return entries


dictionary = readFasta(f)

# On test.fasta:
## real	0m0.055s
## user	0m0.033s
## sys	0m0.021s

#for key, val in dictionary.items():
#	print(key, ":", val)
 

    ########################

f.close()
