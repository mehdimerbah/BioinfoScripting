
# coding: utf-8

# In[25]:


# Opening the files and checking for s

f = open("test.txt")
import os
cwd = os.getcwd()
target = os.path.join(cwd, "test1.txt")
f2 = open(target, "a")


# In[26]:


for line in f:
    print(line.strip())

f2.write("Appended data")
f2.close()    


# In[27]:


# Reversing line by line
target = os.path.join(cwd, "test1.txt")
f2 = open(target, "r")
lines = f2.readlines()

for x in lines:
    print(x)


# In[2]:


f0 = open("test.txt")
lines = f0.readlines()

for line in lines:
    line = line.strip()
    tempLine = list(line)
    tempLine.reverse()
    print("".join(tempLine))

    


# In[4]:


# killing a program

import sys

sys.exit()


# In[6]:


# Exception handling

try:
    open("ThisIsDummyFile.txt")
except:
    print("An error has occured")
    
    


# In[8]:


# Reading a binary file requires specifying the "rb" flag for the open function
f1 = open("test.txt", "rb")
f1.read()



# In[11]:


import os
dirName = "testDir"

if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory ", dirName, " Created")
else: 
    print("Directory ", dirName, " already exists")
    


# In[12]:


# cd
os.chdir('/home/mehdimerbah/')
# pwd
print(os.getcwd())

