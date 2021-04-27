#!/usr/bin/python3

import sys
#file1_path = "/home/mehdimerbah/python_scripts/exam2/names.txt"
#file2_path = "/home/mehdimerbah/python_scripts/exam2/majors.txt"
while True:
    try:
        file1_path = input("Enter first file path: ")
        file1 = open(file1_path, 'rt')
        file2_path = input("Enter second file path: ")
        file2 = open(file2_path, 'rt')
        break
    except:
        print('File Not Found!\n Try again:')



header1 = file1.readline().strip("\n")
header1 = list(header1.split("\t"))
header2 = file2.readline().strip("\n")
header2 = list(header2.split("\t"))

column = input("Enter column to merge the files: ")
if column not in header1:
	print("Column not found in file1")
elif column not in header2:
	print("Column not found in file2")

# Column assumed to be StudentID
dict1 = {}
dict2 = {}
for line in file1:
	stripped = line.strip("\n").split("\t")
	dict1[stripped[0]] = stripped[1:]

for line in file2:
	stripped = line.strip("\n").split("\t")
	dict2[stripped[0]] = stripped[1:]

allKeys = list(dict1.keys())+ list(dict2.keys())
allKeys = set(allKeys)

mergedDict = {}

for i in allKeys:
	if i in list(dict1.keys()) and i in list(dict2.keys()):
		mergedDict[i] = dict1[i] + dict2[i]

outFile = open("mergedFiles.txt", "wt")
for key, val in mergedDict.items():
	print(key, ":", val)
	line = str(key) + ":" + str(val)
	outFile.write(line)


common = len(set(list(dict1.keys())).intersection(list(dict2.keys())))
print("The number of common elements: ", common)


userID = input("Enter an ID: ")
print(mergedDict[userID])


file1.close()
file2.close()