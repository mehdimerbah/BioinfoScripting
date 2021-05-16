#!/usr/bin/env python3
import sys
import re
import os
import math



args = sys.argv
if len(args) == 1:
    print('Please Specify your Fasta filename\nUsage: ./script.py <path/to/fasta>')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()


def readFasta(filename):
	"""This function reads in a fasta file and stores the sequences in a dictionary
	seqDict = {'SeqID' : 'SEQ'}"""
	entries = {}
	for line in f:
	    if '>' in line:
	        seq_id = line.strip()[1:]
	        entries[seq_id] = []
	    else:
	        stripped = list(line.strip("\n").replace(" ",""))
	        entries[seq_id].extend(stripped)

	for key,val in entries.items():
		entries[key] = "".join(val)

	return entries

#Storing the read sequences in a dictionary variable
sequence_dict = readFasta(f)

#Printing the number of sequences available
print("\nThe number of sequences in the file: ", len(sequence_dict.keys()))


f.close()