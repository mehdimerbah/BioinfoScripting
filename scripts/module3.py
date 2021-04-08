
# coding: utf-8

# In[1]:


# For loops
for char in "RACECAR":
    print(char)
    


# In[2]:


for i in range(1,9):
    print(i)


# In[10]:


# Dice throwing
import random
die_res = 0
total = 0
maximum = 0
minimum = 6
for i in range(6):
    die_res = random.randrange(1, 6)
    total += die_res
    maximum = max(maximum, die_res)
    minimum = min(minimum, die_res)
    print("Die's value: ", die_res)

print('Sum of all throws: %5d\nLargest die throw: %5d\nSmallest die throw: %4d' % (total, maximum, minimum))


# In[13]:


# While loop
c = 0
while True:
    c += 1
    
    if c == 4:
        c += 1
        print('Just skipped a step!')
        continue
    
    if c == 8:
        print(c)
        break


# In[16]:


# Using the in operator
if "ba" in "Benedict Cumberbatch":
    print("Found")
else:
    print("Not Found")    
    


# In[17]:


# index() and find()

print("Benedict Cumberbatch".index('t'))
# rindex also returns the first occurrence
print("Benedict Cumberbatch".rindex('t'))

# find()
print("Benedict Cumberbatch".find('Cu'))

