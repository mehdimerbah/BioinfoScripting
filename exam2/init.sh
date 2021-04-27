#!/bin/bash


FILENAME="$1.py"

touch $FILENAME

printf "#!/usr/bin/python3\n" > $FILENAME
printf "import sys\n\n

args = sys.argv
if len(args) == 1:
    print('Please Specify filename')
    sys.exit()

try:
    f = open(args[1], 'rt')
except:
    print('File Not Found!')
    sys.exit()\n
    ######## Script ########
    
    
    ########################

f.close()\n" >> $FILENAME

chmod u+x $FILENAME

