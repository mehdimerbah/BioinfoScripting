
# coding: utf-8

# In[27]:


import time
def fib(n):
    if n==1 or n== 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# In[28]:


start = time.process_time()
print("Fib(5) is: %d \nExecution time: %f" % (fib(5), (time.process_time() - start)))


# In[29]:


start = time.process_time()
print("Fib(24) is: %d \nExecution time: %f" % (fib(24), (time.process_time() - start)))


# In[30]:


start = time.process_time()
print("Fib(40) is: %d \nExecution time: %f" % (fib(40), (time.process_time() - start)))


# In[31]:


def fib2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n== 2:
        return 1
    else:
        result = fib2(n-1, memo) + fib2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None]*(n+1)
    return fib2(n, memo)




start = time.process_time()
print("Fib(40) is: %d \nExecution time: %f" % (fib_memo(40), (time.process_time() - start)))

