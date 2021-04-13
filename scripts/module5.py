
# coding: utf-8

# In[3]:


# Concatenation using the join function
my_list = ["This", "is", "just", "a", "test"]
" ".join(my_list)


# In[6]:


# The concatenation with join only works with str so
#we must cast any data types

nums = [str(x) for x in range(1,9)]
print("This is the number list:\n", "-".join(nums))


# In[9]:


# We can reverse lists and join them w/ the built-in functions
l0 = ["This", "is", "list", "0"]
l0.reverse()
"-".join(l0)


# In[16]:


# Dictionaries are essentially hashmaps

dic = {
    'key0': 0,
    'key1': 1,
    'key2': 2
}
dic['key3'] = 3
dic['key0'] = 'modified'
dic


# In[20]:


# We can create a small address book
addressBook = {}
addressBook['Jack'] = "Jackson Ville"
addressBook['George'] = "Washington"
addressBook['Thomas'] = "Jefferson City"

x= input("Who are you looking for?\n")
print(addressBook[x])


# In[24]:


# Print out the key value pairs

for key, val in addressBook.items():
    print(key,":", val)


# In[26]:


# To avoid any issues with non-existent keys, check for them first
y = input("Who are you looking for?\n")
if y in addressBook:
    print(addressBook[x])
else:
    print("Does not exist")


# In[34]:


Data = {'Actinobacteria': 'GATCCGA...TCA', 'subtilis sp.': 'ATCGATT...ACT'}
dataSet = set(Data.keys())
names = {'Actinobacteria': '8924342'}
nameSet = set(names)


for name in dataSet.intersection(nameSet):
    print(name, names[name])
    print(name, Data[name])

