#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 손익분기점 > 반복문 돌리면 용량부족

a,b,c = map(int,input().split())
if b<c :
    print(a//(c-b)+1)
else :
    print(-1)


# In[17]:


# 런타임 에러 코드 2292

num = int(input())
n = 1
d = []
for i in range(50): 
    n = n + 6*i
    d.append(n)
if num == 1 :
    print(1)
else: 
    for i in range(50) :
        if d[i]< num <= d[i+1] :
            print(i+2)
        


# In[24]:


# 2292
num = int(input())

if num == 1 : 
    print(1)
else :
    i = 0
    l = 1
    while l<num : 
        l = l+6*i
        i+=1
    print(i)

