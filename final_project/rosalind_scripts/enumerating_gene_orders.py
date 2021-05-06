#!/usr/bin/python3
import sys
import math


args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()


integer = int(f.readline())
num_list = []
for i in range(1,integer+1):
    num_list.append(i)


def permute(my_list):
    if len(my_list) <=1:
        yield my_list
        #If the length of the current state of the list as a passed
        #argument is less than one, we just return it
    else:
        for permutation in permute(my_list[1:]):
            for j in range(len(my_list)):
                yield permutation[:j] + my_list[0:1] + permutation[j:]

print(math.factorial(integer))

for itr in permute(num_list):    
    for element in itr:
        print(element, end=" ")
    
    print("")

f.close()
