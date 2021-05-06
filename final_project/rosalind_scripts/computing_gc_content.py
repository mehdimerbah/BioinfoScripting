#!/usr/bin/python3
import sys

args = sys.argv
if len(args) == 1:
    print("Please Specify filename")
    sys.exit()

f = open(args[1], 'rt')

entries = {}
for line in f:
    if '>' in line:
        seq_id = line.strip()[1:]
        entries[seq_id] = []
    else:
        stripped = list(line.strip("\n"))
        entries[seq_id].extend(stripped)


max_gc = 0
max_gc_key = ""
for key, val in entries.items():
    g_count = val.count("G")
    c_count = val.count("C")
    gc_content = 100*(g_count+c_count)/float(len(val))
    if gc_content > max_gc:
        max_gc = gc_content
        max_gc_key = key

print("%s\n%.6f" %(max_gc_key, max_gc))
f.close()
