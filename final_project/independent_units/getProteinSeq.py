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


def spliceSeq(sequence_ID):
	"""
	@params: sequence_ID: the ID of the sequence
	This function extracts the spliced exons from a raw sequence read from a fasa file
	"""
	seq = sequence_dict[sequence_ID]
	match_seq = seq_pattern.search(seq)
	stripped_seq = match_seq.group(2)
	exon_match_list = exon_pattern.findall(stripped_seq)
	spliced_exons = "".join(exon_match_list)

	return spliced_exons
	# Current function timing:
	#real	0m0.085s
	#user	0m0.072s
	#sys	0m0.013s

def transcribeSeq(sequence_ID):
	global mRNA
	spliced = spliceSeq(sequence_ID)
	mRNA = spliced.replace('T','U')
	
	return mRNA

	# Current function timing:
	#real	0m0.084s
	#user	0m0.072s
	#sys	0m0.013s

def translateRNA(mRNA):
	"""
	@params: mRNA sequence to translate to protein
	This function takes in an mRNA sequence then uses a translation hash to translate each
	codon to an amino acid.
	"""
	aaSeq = []
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

	idx = re.search("AUG", mRNA).span()[0]

	while idx <= (len(mRNA)-3):
		codon = mRNA[idx:idx+3]
		idx+=3
		if trans_map[codon] == "STOP":
			break
		else:
			aaSeq.append(trans_map[codon])
	
	aaSeq = "".join(aaSeq)

	# We can write the aaSeq to a file to use in part2
	try:
		#Opening the destination file
		protein_dest_file = open("peptide_seq.txt", 'wt')
		protein_dest_file.write(aaSeq)
	except:
		print('Error with Destination File!')
		sys.exit()

	return aaSeq

	# Current Independent function timing:
	#real	0m0.033s
	#user	0m0.033s
	#sys	0m0.001s

mRNA = transcribeSeq(hit_seq_ID)
protein = translateRNA(mRNA)
print("The mRNA for the selected sequence:\n%s"%mRNA)
print("The peptide sequence translated from the mRNA:\n%s"%protein)

