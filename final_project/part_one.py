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



    ######################## Script ###########################

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


sequence_dict = readFasta(f)

# On test.fasta:
## real	0m0.055s
## user	0m0.033s
## sys	0m0.021s


def generateDNAStats(seq):
	"""
	@params: seq: A DNA Sequence from a Fasta File to analyze
	This function generates basic statistics from the DNA sequence.
	"""
	#Set the sequence pattern we want to match in the following order:
	# (primer)((EXON)((intron)(EXON))*)(downstreamseq)
	# the compile function from the re module is just a nice aesthetic and to save time
	seq_pattern = re.compile("^([agct]+)(([AGCT]+)(([agct]+)([AGCT]+))*)([agct]+)$")
	match_seq = seq_pattern.search(seq)

	#When we strip the adapter sequence and the downstream sequence, 
	# we are left with just exons and introns
	stripped_seq = match_seq.group(2)

	#Defining a regex pattern to match exons and introns
	exon_pattern = re.compile("([AGCT]+)")
	intron_pattern = re.compile("([agct]+)")

	#The findall function helps us get all the matches for both patterns
	# it returns a list with all matches
	exon_match_list = exon_pattern.findall(stripped_seq)
	intron_match_list = intron_pattern.findall(stripped_seq)

	#The number of exons/introns is simply the length of the lists
	exon_count = len(exon_match_list)
	intron_count = len(intron_match_list)

	#We can now join the lists to get a single sequence string
	spliced_exons = "".join(exon_match_list)
	spliced_introns = "".join(intron_match_list)

	#Average exon/intron length calculation
	avg_exon_len = round(len(spliced_exons)/len(exon_match_list),1)
	avg_intron_len = round(len(spliced_introns)/len(intron_match_list),1)

	#Calculating base proportions
	exon_base_proportion = {}
	for base in set(spliced_exons):
		exon_base_proportion[base] = round(spliced_exons.count(base)/len(spliced_exons)*100, 2)

	intron_base_proportion = {}
	for base in set(spliced_introns.upper()):
		intron_base_proportion[base] = round(spliced_introns.upper().count(base)/len(spliced_introns)*100, 2)
	#Return the sequence statistics as a tuple

	seq_stats = (exon_count, intron_count, avg_exon_len, avg_intron_len, exon_base_proportion['A'], exon_base_proportion['C'], exon_base_proportion['G'], exon_base_proportion['T'],
	 			intron_base_proportion['A'], intron_base_proportion['C'], intron_base_proportion['G'], intron_base_proportion['T'])

	return seq_stats
   


def writeStats():
	stats_dict = {}
	for seqID, sequence in sequence_dict.items():
		stats_dict[seqID] = generateDNAStats(sequence)

	print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%('SeqID','#Exons','#Introns','AvgExonLen','AvgIntronLen','\%A in Exon','\%C in Exon','\%G in Exon','\%T in Exon','\%A in Intron','\%C in Intron','\%G in Intron','\%T in Intron'))
	for seqID, stats in stats_dict.items():
		print ('%s %10d %10d %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f'%(seqID, stats))



writeStats()	


f.close()
