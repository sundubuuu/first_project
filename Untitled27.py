#!/usr/bin/env python
# coding: utf-8

# In[3]:


a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
for i in range(1,1000000) :
    if i%a ==0 and i%b==0 and i%c==0 : 
        print(i)
        break


# In[2]:


a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 1
while d%a != 0 or d%b != 0 or d%c != 0 :
    d += 1
print(d)


# In[10]:


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
    
lst = []

for i in a :
    lst.append(i)
    
for i in range(1,24):
    d = lst.count(i)
    print(d,end= " ")
    


# In[18]:


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])    

lst = []

for i in a :
    lst.append(i)
    
print(lst[::-1])


# In[19]:


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])   
    
for i in range(n-1,-1,-1):
    print(a[i],end=" ")


# In[23]:


n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])    

lst = []

for i in a :
    lst.append(i)
    
min = min(lst)
print(min)


# In[29]:


a = []
for i in range(20) :
    a.append([])
    for j in range(20):
        a[i].append(0)
        
n = int(input())
for i in range(0,n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    a[x][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j], end = " ")
    print()
        


# In[30]:


d = [0 for i in range(20)]
print(d)


# In[32]:


d =[[0 for i in range(20)] for j in range(20)]
print(d)


# In[33]:


d =[[0 for i in range(20)] for j in range(20)]
        
n = int(input())
for i in range(0,n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    d[x][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end = " ")
    print()


# In[36]:


N,K = map(int,input().split())
n = 0
a =[]
for i in range(N):
    a.append(int(input()))
    
for i in a[::-1]:
    n += K//i
    K%=i
print(n)


# In[39]:


A,B = map(int, input().split())
if A>B :
    print(">")
elif A<B :
    print("<")
elif A==B :
    print("==")


# In[42]:


s = int(input())
if s>=90 and s<=100 :
    print("A")
elif s>=80 and s<=89 :
    print("B")
elif s>=70 and s<=79 :
    print("C")
elif s>=60 and s<=69 :
    print("D")
else : 
    print("F")


# In[45]:


y=int(input())
if ((y%4==0 and y%100!=0) or y%400==0) :
    print(1)
else :
    print(0)


# In[48]:


x = int(input())
y = int(input())
if x>0 and y>0 :
    print(1)
elif x<0 and y>0 :
    print(2)
elif x<0 and y<0 :
    print(3)
elif x>0 and y<0 :
    print(4)


# In[49]:


print("3421"[input()>"0"::2][input()>"0"])


# In[52]:


a,b,c = map(int, input().split())
if a==b and b==c and a==c :
    print((a*1000)+10000)
elif a==b or a==c or b==c : 
    if a==b or a==c :
        print((a*100)+1000)
    elif b==c :
        print((b*100)+1000)
else :
    if a>b>c or a>c>b :
        print(a*100)
    elif b>a>c or b>c>a :
        print(b*100)
    elif c>a>b or c>b>a :
        print(c*100)


# In[54]:


a,b,c = sorted(map(int, input().split()))
print(a)
print(b)
print(c)

