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



    ######################## Script ###########################

# Setting regex match patterns for reusability: 

#Set the sequence pattern we want to match in the following order:
	# (primer)((EXON)((intron)(EXON))*)(downstreamseq)
	# the compile function from the re module is just a nice aesthetic and to save time
seq_pattern = re.compile("^([agct]+)(([AGCT]+)(([agct]+)([AGCT]+))*)([agct]+)$")


#Defining a regex pattern to match exons and introns
exon_pattern = re.compile("([AGCT]+)")
intron_pattern = re.compile("([agct]+)")

# QUESTION 1:
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


# QUESTION 2:
def generateDNAStats(seq):
	"""
	@params: seq: A DNA Sequence from a Fasta File to analyze
	This function generates basic statistics from the DNA sequence.
	"""
	# Fir any raw sequence passed we must match the sequence pattern we predefined
	match_seq = seq_pattern.search(seq)
	#When we strip the adapter sequence and the downstream sequence, 
	# we are left with just exons and introns
	stripped_seq = match_seq.group(2)

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
   

def printStats():
	'''
	This method prints the sequence statistics to the user on the console
	'''
	stats_dict = {}
	for seqID, sequence in sequence_dict.items():
		stats_dict[seqID] = generateDNAStats(sequence)
	print('')
	print('%100s'%"################ Sequence Stats ################")
	print("%s%10s%10s%13s%15s%12s%12s%12s%12s%13s%13s%13s%13s"%('SeqID','#Exons','#Introns','AvgExonLen','AvgIntronLen','%A in Exon','%C in Exon','%G in Exon','%T in Exon','%A in Intron','%C in Intron','%G in Intron','%T in Intron'))
	for seqID, stats in stats_dict.items():
		print ('%-12s'%seqID, end='') 
		print ('%d %9d %14.2f %14.2f %11.2f %11.2f %11.2f %11.2f %11.2f %11.2f %11.2f %11.2f'%stats)

def writeStats():
	'''
	This function writes the statistics generated by the generateDNAStats function into a tab-delimited
	file DNAstats.txt
	'''
	#Create a statistics dictionary for ease of use 
	stats_dict = {}
	for seqID, sequence in sequence_dict.items():
		#For each sequence we have, we call the generateDNAStats method to get the statistics
		#The stats are then stored in the stats dictionary
		stats_dict[seqID] = generateDNAStats(sequence)


	# QUESTION 3:
	try:
		#Opening the destination file
		dest_file = open("DNAstats.txt", 'wt')
		#Writing the statistics to the destination file
		dest_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%('SeqID','#Exons','#Introns','AvgExonLen','AvgIntronLen','%A in Exon','%C in Exon','%G in Exon','%T in Exon','%A in Intron','%C in Intron','%G in Intron','%T in Intron'))
		for seqID, stats in stats_dict.items():
			dest_file.write('%s\t'%seqID)
			dest_file.write('%d\t%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n'%stats)
		#Inform the user that the stats have been written
		path = os.getcwd()+"/DNAstats.txt"
		print("\nStats Succesfully Written to: ", path)
		dest_file.close()
	except:
		print('Error with Destination File!')
		sys.exit()

	
printStats()
writeStats()	

## Current Timing:
#real	0m0.125s
#user	0m0.112s
#sys	0m0.013s

# QUESTION 4:
def retrieveStats(sequence_ID):
	"""
		@params: sequence_ID: ID of a sequence from DNAstats file
		This function retrieves statistics for a specific sequence
		It opens the DNAstats file, searches for the sequence and print itse information on the console.
	"""
	stats_file_path = os.getcwd()+"/DNAstats.txt"
	try:
		stats = open(stats_file_path, "rt")
	except:
		print('Error reading DNAstats File!')
		sys.exit()

	#if re.match(str(sequence_ID), str(stats)):
	for line in stats:
		if sequence_ID in line:
			print("%s%10s%10s%13s%15s%12s%12s%12s%12s%13s%13s%13s%13s"%('SeqID','#Exons','#Introns','AvgExonLen','AvgIntronLen','%A in Exon','%C in Exon','%G in Exon','%T in Exon','%A in Intron','%C in Intron','%G in Intron','%T in Intron'))
			line = line.strip()
			line = tuple(line.split("\t"))
			print('%s%9s%8s%15s%15s%12s%12s%12s%12s%12s%12s%12s%12s'%line)
			global hit_seq_ID
			hit_seq_ID = sequence_ID
			return 
	
	new_sequence_ID = input("Sequence Not found!\nPlease enter a new ID:\t")
	retrieveStats(new_sequence_ID)
	# Current function timing:
	#real	0m0.053s
	#user	0m0.041s
	#sys	0m0.013s


prompt_seq_ID = input("Enter Sequence ID to Retrieve Stats: ")
#prompt_seq_ID = "HCN1"
retrieveStats(prompt_seq_ID)


# QUESTION 5:
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
		protein_dest_file = open("protein_seq.txt", 'wt')
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


# QUESTION 6:
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


# Current part_one timing with no Sequence prompt:
#real	0m0.184s
#user	0m0.130s
#sys	0m0.013s

# Current part_one timing with Sequence prompt:
#real	0m3.939s
#user	0m0.153s
#sys	0m0.012s


#TBD:
# Add validation function to make sure the functions are working properly
# Verify function logic



		#############################################################
f.close()
