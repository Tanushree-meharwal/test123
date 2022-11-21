#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python script to print MySirG N times on the screen.
num = int(input("enter the number: "))
for i in range(num):
    print("MySirG")


# In[ ]:


#2. Write a python script to print first N natural numbers.
num = int(input("enter the number: "))
for e in range(num):
    print(e+1)


# In[ ]:


#3. Write a python script to print first N natural numbers in reverse order.
num = int(input("enter the number: "))
while num>0:
    print(num)
    num-=1


# In[2]:


#4. Write a python script to print first N odd natural numbers.
num = int(input("enter the number:"))
for i in range(num*2):
    if i%2!= 0:
        print(i)


# In[1]:


#5. Write a python script to print first N odd natural numbers in reverse order.
num = int(input("enter the Number: "))
for i in range(num*2,0,-1):
    if i%2!=0:
        print(i)


# In[5]:


#6. Write a python script to print first N even natural numbers.
num = int(input("enter the number: "))
for i in range(0,num*2):
    if i%2== 0:
        print(i)


# In[4]:


#7. Write a python script to print first N even natural numbers in reverse order.
num = int(input("enter the Number: "))
for i in range(num*2,0,-1):
    if i%2==0:
        print(i)


# In[ ]:


#8. Write a python script to print squares of first N natural numbers.
num = int(input("enter the number: "))
for i in range(1,num+1):
    print(i**2)


# In[ ]:


#9. Write a python script to print cubes of first N natural numbers.
num = int(input("enter the number: "))
i = 1
while(i<num+1):
    print(i**3)
    i += 1


# In[ ]:


#10. Write a python script to print first 10 multiples of N.
num = int(input("enter the number: "))
i = 1
while(i<11):
    print(i*num)
    i += 1


# In[ ]:




