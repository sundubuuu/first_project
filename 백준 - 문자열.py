#!/usr/bin/env python
# coding: utf-8

# In[17]:


c = input()
c = ord(c)
print(c)


# In[25]:


n = int(input())
c = list(input())
sum = 0
           
for i in c :
    i = int(i)
    sum += i
print(sum)


# In[26]:


n = int(input())
l = int(input())
c = 0
for i in str(l):
    c+=int(i)
print(c)


# In[32]:


s = list(input())
d=[]

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alpha :
    if i in s :
        print(s.index(i),end = " ")
    else :
        print(-1,end = " ")


# In[33]:


from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
word_list = list(input())

for i in alphabet_list:

    if i in word_list:
        print(word_list.index(i), end=' ')

    else:
        print(-1, end=' ')


# In[40]:


c = int(input())

for i in range(c) : 
    a, b = input().split()
    a = int(a)
    b = list(b)
    for i in b :
        print(i*a, end ="")
    print()


# In[44]:


#단어공부
s = str(input())
s = s.upper()

st = set(s)


print(s)


# In[47]:


c = list(input().split())
print(len(c))


# In[49]:


a,b = input().split()
a = a[::-1]
b = b[::-1]
a = int(a)
b = int(b)
if a> b :
    print(a)
else :
    print(b)


# In[72]:


a = input()
sum = 0

for i in a : 
    if i == "A" or i == "B" or i == "C" :
        sum = sum + 3
    elif i == "D" or i == "E" or i == "F" :
        sum = sum + 4
    elif i == "G" or i == "H" or i == "I" :
        sum = sum + 5
    elif i == "J" or i == "K" or i == "L" :
        sum = sum + 6
    elif i == "M" or i == "N" or i == "O" :
        sum = sum + 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        sum = sum + 8
    elif i == "T" or i == "U" or i == "V" :
        sum = sum + 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z" :
        sum = sum + 10

print(sum)


# In[79]:


list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV","WXYZ" ]

a = input()
sum = 0
for i in range(len(a)):
    for j in list :
        if a[i] in j :
            sum += list.index(j)+3
print(sum)


# In[90]:


a = input()

a = a.replace("c=","c") 
a = a.replace("c-","c")
a = a.replace("dz=","c")
a = a.replace("d-","d")
a = a.replace("lj","l")
a = a.replace("nj","n")
a = a.replace("s=","s") 
a = a.replace("z=","z")

print(len(a))


# In[92]:


croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
d = input()

for i in croatia:
    if i in d:
        d = d.replace(i, '#')

print(len(d))

