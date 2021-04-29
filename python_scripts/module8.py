
# coding: utf-8

# In[5]:


# Referencing
x = 8
y = x
# Simple data types, defined by value
print(x, y)
x = 9
print(x, y)
y = y + 1
print(x, y)

# Check the following
# Notice how modifying the original or the copy changes both
# data structures are defined by reference
l0 = [2, 3, 4]
l1 = l0
# The following will change both lists because they point to the same 
#memory location, pointers set to same address
l1.append(2)
print(l1, l0)


# In[8]:


# Methods create local copies within their scope, they do not modify
#the passed values
def replaceString(the_string):
    the_string = "New string"
    print('Inner String:', the_string)

outer_string = 'Old String'
print('Outer string, before =', outer_string)
replaceString(outer_string)
print('Outer string, after =', outer_string)


# In[13]:


# On the other hand, with data-structures are defined by reference
#Any change to the values in a local scope, takes effect globally
#since the change is done to the value referenced memory address

def appendToList(list):
    list.append("New Element")

l = ['Old Element1', 'Old Element2']

print('Outer list, before =', l)
appendToList(l)
print('Outer list, after =', l)

print("\n-------- Concatenation --------\n")
def appendToList(list):
    list = list + ['New Element1', 'New Element2']
    print("Inner list", list)

l = ['Old Element1', 'Old Element2']
print('Outer list, before =', l)
appendToList(l)
print('Outer list, after =', l)

