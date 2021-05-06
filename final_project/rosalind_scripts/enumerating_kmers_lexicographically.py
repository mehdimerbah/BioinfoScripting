#!/usr/bin/python3
import sys



args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()

    ######## Script ########
alpha = list(f.readline().strip().replace(" ", ""))
n = int(f.readline())
curr = ""



## The following is to get permutations of distinct characters
# No putting back after draw
def get_permutations(a, left, right):
    if left == right:
        print(''.join(a))
    
    else:
        for i in range(left, right+1):
            a[left], a[i] = a[i], a[left]
            get_permutations(a, left+1, right)
            a[left], a[i] = a[i], a[left]

#get_permutations(alpha, 0, len(alpha)-1)


def get_combinations(alphabet, n, curr = ''):
    if n == 0:
        print(''.join(curr))
    else:
        for c in alphabet:
            get_combinations(alphabet, n - 1, curr + c)


get_combinations(alpha, n)



    ########################

f.close()
