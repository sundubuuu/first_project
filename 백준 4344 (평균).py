#!/usr/bin/env python
# coding: utf-8

# In[4]:


c = int(input()) 
for i in range(c): 
    arr = list(map(int,input().split()))
    n = arr[0]
    sum = 0
    for j in arr[1:]:
        sum += j
    e = sum/n
    m = 0
    for i in arr[1:]:
        if i>e :
            m+=1
    b = m/n*100
    
    print("%.3f%%"%b)

