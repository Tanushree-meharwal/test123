#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python script to print the first 10 multiples of 5.
for i in range(1,11):
    print(i*5)


# In[ ]:


#2. Write a python script to print first 10 multiples of N.
num = int(input("enter the table number:"))
for i in range(1,11):
    print(i*num)


# In[ ]:


#3. Write a python script to print first M multiples of N.
M = int(input("how many multiple you wants: "))
N = int(input("enter the number: "))
for i in range(1,M+1):
    print(i*N)


# In[ ]:


#4. Write a python script to print the first 10 multiples of N in reverse order.
N = int(input("enter the number: "))
for i in range(10,0,-1):
    print(N*i)


# In[ ]:


#5. Write a python script to print table of user’s choice.
num = int(input("enter the table number:"))
for i in range(1,11):
    print(i*num)


# In[ ]:


#6. Write a python script to print first N even natural numbers.
n = int(input("enter the number: "))
for i in range(0,n*2):
    if i%2== 0:
        print(i)


# In[ ]:


#7. Write a python script to print first N odd natural numbers.
num = int(input("enter the number:"))
for i in range(num*2):
    if i%2!= 0:
        print(i)


# In[ ]:


#8. Write a python script to print squares of first N natural numbers.
num = int(input("enter the number: "))
for i in range(1,num+1):
    print(i**2)


# In[ ]:


#9. Write a python script to print cubes of first N natural numbers.
num = int(input("enter the number: "))
for i in range(1,num+1):
    print(i**3)


# In[32]:


#10. Write a python script to display all prime numbers within a range. range start = 15 ,end = 45
for i in range(15,45):
    for j in range(2,i):
        if i%j == 0:
            break;
    else:
        print(i)
            


# In[ ]:




