#!/usr/bin/env python3
import sys
import re
import os




def retrieveStats(sequence_ID):
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
			print(line)
			return
	
	new_sequence_ID = input("Sequence Not found!\nPlease enter a new ID:\t")
	retrieveStats(new_sequence_ID)

retrieveStats("HCN2")

