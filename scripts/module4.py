
# coding: utf-8

# In[7]:


my_tuple = ("test", 123, ("Hellow", 555))

print(my_tuple)


# In[11]:


print(my_tuple[0], my_tuple[1], my_tuple[2])
print(my_tuple[2][0])


# In[19]:


print(my_tuple[-2])


# In[22]:


print(len(my_tuple))
print(len(my_tuple[2]))


# In[24]:


## Concatination
concat = (1,2,3)+(4,5,6)
print(concat)


# In[28]:


## Create a tuple differently

numbers = tuple(range(1,11))
print(numbers)


# In[45]:


# Get a tuple using a generator, and build it with a comprehension
oddNumbers = tuple(i for i in numbers if i% 2 == 1)
evenNumbers = tuple(i for i in numbers if i% 2 == 0)
print("Odd\n", oddNumbers)
print("Even\n", evenNumbers)


# In[53]:


l3 = list("13")
print(l3)


# In[61]:


## Appending Elements to lists

array = ['List', 5,4,3,2,0 ]
array.append('List')
print(array)

## Change the Value at specific index

array[1] = "NewVal"
print(array)
## Reverse Array

array.reverse()
print(array)


# In[66]:


## Popping elements: Just like a stack
## We use popping for memory optimization
array = ['List', 0, 2, 3, 4, 'NewVal', 'List']
array.pop(2)
print(array)

array.remove("NewVal")


# In[69]:


print(array)


# In[71]:


## The sort function

array1 = [1, 19, 2, 34, 18]
array1.sort()
print(array1)


# In[73]:


## Sort works the same for strings
names=["George","Tony","Maria","Joseph","Rami"]
names.sort()
print(names)


# In[76]:


"This is just a test, to see if this works".split(" ")


# In[79]:


## Working with For loops
Audios=["Title1 1999 Artist1"]
Audios=Audios+["Title2 2000 Artist2"]
Audios.append("Title3 2001 Artist3")
Audios.append("Title4 2002 Artist4")
Audios.append("Title5 2003 Artist5")

for entry in Audios:
    result = entry.split(" ") 
    print("Title:", result[0])
    print("Release Date:", result[1])
    print("Artist:", result[2])
    


# In[80]:


## using the index and the element itself
for i, entry, in enumerate(Audios):
    result = entry.split(" ")
    print("Entry number"+str(i),"Title:", result[0],"Release Date:", result[1], "Artist: ", result[2])

