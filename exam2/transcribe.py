#!/usr/bin/python3


stripped = input("Please enter a sequence: ")

trans = []

for x in stripped:
    if x == "T":
        trans.append("U")
    else:
        trans.append(x)

trans = "".join(trans)

print(trans)



