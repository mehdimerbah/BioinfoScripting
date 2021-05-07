#!/usr/bin/env python3
import sys
import re



#Here we will use a dummy sequence then apply on all seqs in Fasta
seq = "ccgtgctgcagctacgcagtcatggACACGTCAGCGTACGacgatcgactgcagACGAGTCGACGTTAGCcacaaccgctcggcAGCTTCTTCGCAacaaccgctcggc"
   
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


print(exon_match_list)
print(intron_match_list)
print(spliced_exons)
print(spliced_introns)

print("Exon props: ")
for key, val in exon_base_proportion.items():
	print(key, ":", val)

print("intron props: ")
for key, val in intron_base_proportion.items():
	print(key, ":", val)

seqID = 'Rosa'
seq_stats = (seqID, exon_count, intron_count, avg_exon_len, avg_intron_len, exon_base_proportion['A'], exon_base_proportion['C'], exon_base_proportion['G'], exon_base_proportion['T'],
 			intron_base_proportion['A'], intron_base_proportion['C'], intron_base_proportion['G'], intron_base_proportion['T'])

print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(seqID, exon_count, intron_count, avg_exon_len, avg_intron_len, exon_base_proportion['A'], exon_base_proportion['C'], exon_base_proportion['G'], exon_base_proportion['T'],
 			intron_base_proportion['A'], intron_base_proportion['C'], intron_base_proportion['G'], intron_base_proportion['T']))


print ('%s %10d %10d %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f %14.2f'%seq_stats)