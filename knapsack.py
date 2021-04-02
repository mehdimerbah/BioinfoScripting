#!/usr/bin/python3



# This is an implementation of the naive approach to solving the
#Knapsack Problem. 
#Table for the problem is two sets of weights and values as follows

w = [0,2,1,3,2]
v = [0,12,10,20,15]


dp = [[None]*(6)]*(6)

def Knapsack(n, C):
    if dp[n][C] is not None:
        return dp[n][C]
    #If we are at index 0 or have no more space 
    if n == 0 or C == 0:
        result = 0
    #if the weight of the item is greater than the current capacity
    elif w[n] > C:
        result = Knapsack(n-1, C)
    #We either take the item or not. 
    #if we do take it, we add its value and decrease capacity
    #if we don't, then check the next element 
    else:
        no_take_item = Knapsack(n-1, C)
        take_item = v[n] + Knapsack(n-1, C - w[n])
        result = max(no_take_item, take_item)
    dp[n][C] = result
    return result



print(Knapsack(4, 5))
print(dp)
