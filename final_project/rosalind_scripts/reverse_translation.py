#!/usr/bin/python3

import sys

#protein = input("Enter an AA Seq: ")
protein = "MFN"

def aaToCodonList(Protein):
  """
  This method generates a list of codons given an amino acid sequence.
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

          # Running this for the first time would
          #create an error if the element is not a list
          # To fix this: First time the function is called on a single element
          #we convert that element into a list
          # Bug result: [['A', 'U', 'G', 'UUU', 'AAU'], ['A', 'U', 'G', 'UUU', 'AAC'], ['A', 'U', 'G', 'UUC', 'AAU'], ['A', 'U', 'G', 'UUC', 'AAC']]
          if type(codon_list_x[i]) != list:         
              codon_list_x[i] = [codon_list_x[i]]
                
          # For all codons in first codon list, we store them in a temp list
          tmp_list = [codon for codon in codon_list_x[i]]
            
          #  Append codon in second list to the temp list      
          tmp_list.append(codon_list_y[j])   
          # Now we append the temporary list to the resulting cartesian product list          
          result.append(tmp_list)  
            
  return result


def cartesianProtein(aa_list):
  """
  This method works to get the cartesian product of all the codon sets pertaining to all amino acids in the protein sequence.
  To do this we just call the helper method cartesianTwoAA on all the amino acids in the sequence two-by-two.
  """
  n = len(aa_list)
  global mRNA_list
  mRNA_list = aa_list[0]

  for i in range(1, n):
      mRNA_list = cartesianTwoAA(mRNA_list, aa_list[i])

  for mRNA in mRNA_list:
      print("".join(mRNA))




codons_list = aaToCodonList(protein)
print("Protein: ", protein)
print("Equivalent codons: ", codons_list)
print("Possible mRNAs: ")
cartesianProtein(codons_list)