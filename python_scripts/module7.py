
# coding: utf-8

# In[3]:


# Defining methods

def foo():
    print("Foo foo! bar!")
    
foo()


# In[5]:


def method1(variable):
    # Local copy of variable created
    print("This method is called with variable "+str(variable))


    method1("Var0")


# In[7]:


# Setting default values for variables in case nothing is passed
def method2(var = "def0", var1 = "def1"):
    print(var, var1)

method2()


# In[9]:


# You can use assignment to specifiy for which variable you want to assign a value
method2(var = "NewDef0")
method2(var = "NewDef0", var1 = "NewDef1")
method2("NewDef0", "NewDef1")


# In[12]:


# Methods can return anything
# Tuple
def getTuple():
    return(0,1)
print(getTuple())

# List
def getList():
    return[2,3]
print(getList())

# Result of operation
def multiply(x,y,z):
    return x*y*z
print(multiply(1,2,3))

# Pass different data types
print(multiply("n",2,3))


# In[26]:


# Defining and accessing global variables within a local function scope
globalv = 4

def method3():
    print(globalv)
method3()

def method4():
    global glob_v 
    glob_v = 5
    print("Globally defined: ", globalv, "\tLocally defined but global: ", glob_v)    
method4()

# Now the variable that we defined locally in method4 is accessible in the global scope
print("Locally defined in method4():\t",glob_v)

