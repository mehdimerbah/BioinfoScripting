
# coding: utf-8

# In[3]:


x = 5

if x < 10:
    print("Hellow")
else:
    print("Bye")

    
if x < 10:

    if x < 5:

        print("Less than 5")

    else:

        print("Greater than 5, but less than 10")

else:

        print("Greater than 10")


# In[5]:


sum = 50

if sum%2==0:
    print("Even")
else:
    print("Odd")

sum = 75

if sum%2==0:
    print("Even")
else:
    print("Odd")


# In[7]:


import random

randomNum = random.randrange(100)
guessedNumber = input("Guess the number that was generated?")
guessedNumber = int(guessedNumber)

if randomNum == guessedNumber:
    print("Correctly guessed!")
else:
    print("The number generated was", randomNum)

print("The difference is", randomNum - guessedNumber)


# In[8]:


# ASCII Compare chars

if "A" > "z":
    print("A iz greater than z")
else:
    print("It is not")

print("A" > "z", "A" == "z", "A" < "z")


# In[9]:


# Shorthand notation for if

x = "Greater" if "A" > "z" else "Smaller"
print("A is %s than z" %x)

