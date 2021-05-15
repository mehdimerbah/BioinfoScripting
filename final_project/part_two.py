#!/usr/bin/env python3
import sys
import re
import os
import math



#args = sys.argv
#if len(args) == 1:
#   print('Please specify path to a file containing peptide sequence:\nUsage: ./script.py <path/to/peptide_seq.txt>')
#    sys.exit()

try:
    #f = open(args[1], 'rt')
    f = open('peptide_seq.txt', 'rt')
except:
    print('File Not Found!')
    sys.exit()

# Testing is done on a short peptide sequence.
# The full-length peptide sequence would take a very (VERY) long time. (execution time increases at factorial rate)

# To use on the sequence selected in part one, uncomment next line and comment-out the one after it. 
#protein = f.readline().strip() #Assumes peptide seq is on a single line, no spaces in-between AAs.
#protein = 'MSLMVVSMACVGVHRK'
protein = 'MFNSW'

def aaToCodonList(Protein):
  """
  This method generates a list of repective codons given a peptide sequence.
  """
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

  # We define a reverse translation dictionary to go from AA to Codon
  reverse_dict = {} 
  # We initialize the reverse dictionry keys with an amino acid name set
  aa_keySet = set(trans_map.values())
  for key in aa_keySet:
      reverse_dict[key] = []

  # Now we attribute for each amino acid its list of codons
  for key, val in trans_map.items():
      reverse_dict[val].append(key)

  # We append our results in a list to use later for getting the cartesian product of the all codon sets
  aa_list = []
  for aa in Protein:
      aa_list.append(reverse_dict[aa])


  return aa_list


def cartesianTwoAA(codon_list_x, codon_list_y):
  """
  This method take the cartesian product of two sets of codons, one for each amino acid.
  The idea is to take the cartesian product of all sets in a pairwise fashion, so this
  will be a helper method for the cartesianProtein method.
  """
  result =[]
  #for all elements in the first codon list
  for i in range(0, len(codon_list_x)):
      #for all codons in the second codon list
      for j in range(0, len(codon_list_y)):
          # For all codons in first codon list, we store them in a temp list
          tmp_list = [codon_list_x[i]] 
          #  Append codon in second list to the temp list      
          tmp_list.append(codon_list_y[j])   
          # Now we append the temporary list to the resulting cartesian product list          
          result.append("".join(tmp_list))  
  
  return result


def cartesianProtein(aa_list):
	"""
	This method works to get the cartesian product of all the codon sets pertaining to all amino acids in the protein sequence.
	To do this we just call the helper method cartesianTwoAA on all the amino acids in the sequence two-by-two.
	"""
	n = len(aa_list)
	mRNA_list = aa_list[0]

	for i in range(1, n):
		mRNA_list = cartesianTwoAA(mRNA_list, aa_list[i])

	return mRNA_list


codons_list = aaToCodonList(protein)
mRNA_list = cartesianProtein(codons_list)

def getGC():
	"""
	This function takes the list of possible mRNAs generated from the cartesianProtein function and computes the GC content of each.
	The sequence with the GC content closest to 50% is chosen as the most probable one.
	"""
	rna_dict = {}
	most_probable = ""
	deviation = 100
	
	for mRNA in mRNA_list:
		g_count = mRNA.count("G")
		c_count = mRNA.count("C")
		gc_content = 100*(g_count+c_count)/float(len(mRNA))
		rna_dict[mRNA] = gc_content
		if abs(50-gc_content) < deviation:
			deviation = abs(50-gc_content)
			most_probable = mRNA
	
	# Defining a key for the sort function
	#since the items are stored as (key, value) tuples in rna_dict.items() in the form: (mRNA, %GC). we make a function that sets the sorting key to the %GC, i.e. the second element.
	
	def sortKey(item):
		return item[1]

	rna_sequence_list = list(rna_dict.items())
	rna_sequence_list.sort(key = sortKey)
	# Quick hack to escape the % sign in the formatting. I just stored it in a variable.
	percent = '%'
	counter = 1
	print("\nPossible mRNA Sequences: \n")
	for item in rna_sequence_list:
		print("mRNA Sequence %d : %.2f %sGC\n%s\n"%(counter, item[1], percent, item[0]))
		counter += 1

	print("Most Probable mRNA Sequence Based on GC content: \n%s\nGC Content: %.2f%s"%(most_probable, rna_dict[most_probable], percent))


print("Protein: ", protein)
getGC()

# Current timing on 3 amino acid peptide sequence:

## real	0m0.057s
## user	0m0.051s
## sys	0m0.004s



# Current timing for: MSLMVVSMAC
# Number of mRNA Sequences: 27648

## real	0m0.418s
## user	0m0.218s
## sys	0m0.091s


# For the sequence: MSLMVVSMACVGVHRK (16 AA)

## Number of mRNA Sequences: 42,467,328
## Most Probable mRNA Sequence Based on GC content: 
## AUGUCUUUAAUGGUUGUUUCUAUGGCUUGCGUCGGCGUCCACCGCAAG
## GC Content: 50.00% (Normally, many sequences have 50% GC content so I just take the first)

## real	10m32.145s
## user	3m27.942s
## sys	2m23.052s

# Running this code for a full-length peptide sequence from part one would probably melt the CPU


##################################################################################################################################

f.close()

