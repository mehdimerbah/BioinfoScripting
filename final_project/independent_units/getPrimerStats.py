#!/usr/bin/env python3

import sys
import re
import os
import math

    ######################## Script ###########################

# Setting regex match patterns for reusability: 

#Set the sequence pattern we want to match in the following order:
	# (primer)((EXON)((intron)(EXON))*)(downstreamseq)
	# the compile function from the re module is just a nice aesthetic and to save time
seq_pattern = re.compile("^([agct]+)(([AGCT]+)(([agct]+)([AGCT]+))*)([agct]+)$")


#Defining a regex pattern to match exons and introns
exon_pattern = re.compile("([AGCT]+)")
intron_pattern = re.compile("([agct]+)")



def getPrimer(sequence_ID):
	"""
	@params: sequence_ID: the ID of the sequence
	This function extracts the primer from raw sequence read from a Fasta file
	"""
	seq = sequence_dict[sequence_ID]
	match_seq = seq_pattern.search(seq)
	primer = match_seq.group(1)

	return primer

	# Current function timing:
	#real	0m0.074s
	#user	0m0.062s
	#sys	0m0.012s


def getPrimerTm():
	primer = getPrimer(hit_seq_ID)
	idx = 0
	min_Tm = math.inf
	max_Tm = 0
	Tm_sum = 0

	while idx < len(primer)-20:
		window = primer[idx:idx+21]
		Tm = (window.count('a')+window.count('t'))*2 + (window.count('g')+window.count('c'))*4
		Tm_sum += Tm
		min_Tm = min(min_Tm, Tm)
		max_Tm = max(max_Tm, Tm)
		idx+=1
		#print("Primer %d: %s"%(idx,window))
		#print("Min. Melting Temperature: %d\nMax. Melting Temperature: %d"%(min_Tm, max_Tm)) 
		
	avg_Tm = Tm_sum/idx

	print("Primer Melting Temperature:\nAverage Primer-Tm: %.2f\nPrimer Melting Temperature Range: [%d - %d]"%(avg_Tm, min_Tm, max_Tm)) 

getPrimerTm()
