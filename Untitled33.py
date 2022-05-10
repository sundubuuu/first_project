#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = int(input())

for i in range(n):
    arr = list(input())
    score = 0
    sum = 0
    for j in arr :
        if j == "O":
            score+=1
            sum += score
        else :
            score = 0
    print(sum)

