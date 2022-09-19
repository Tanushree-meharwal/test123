#!/usr/bin/env python
# coding: utf-8

# In[3]:


""" Q - 1 Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)"""
num = int(input("enter any value:"))
num_2 =num//10
print(num_2)


# In[4]:


""" Q - 2 Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)"""
num = int(input("enter any value:"))
num_2 = num%10
print(num_2)


# In[ ]:


# Q - 3 Write a python script to swap data of two variables
num_1 = int(input("enter first value: "))
num_2 = int(input("enter second value: "))
num_1,num_2 = num_2,num_1
print(" first new number is :" , num_1)
print(" second new number is :" , num_2)


# In[ ]:


#Q - 4 Write a python script to find x power y, where values of x and y are given by user.
x = eval(input("enter your base value: "))
y = eval(input("enter your power value: "))
c = x**y    # y is power of x
print(c)


# In[ ]:


""" Q - 5 Write a python script which takes a three digit number from the user and displays
only its first digit."""
num = int(input("enter three digit number : "))
num_2 = int(num/100)
print(num_2)


# In[ ]:


""" Q - 6 Write a python script which takes a three digit number from the user and displays
only its middle digit."""
num = int(input("enter three digit number : "))
num_2 = int(num/10)
num_3 = num_2%10
print(num_3)


# In[ ]:


""" Q - 7 Write a python script which takes a three digit number from the user and displays
only its last digit."""
num = int(input("enter three digit number : "))
num_2 = num%10
print(num_2)


# In[ ]:


# Q - 8 Write a python script to use IN operator to display the data present in the list
l1 = [23,34,40,45,455,45,56,67,68,89,25,634]
c = int(input("enetr value: "))
print(c in l1)


# In[ ]:


# Q - 9 Write a python script to use NOT IN operator to display the data not present in list.
l = [23,34,40,45,455,45,56,67,68,89,25,634]
c = int(input("enetr value: "))
print(c not in l)


# In[ ]:


""" Q - 10 Write a python script to use IS operator to display if both variables are the same
object or not?"""
l = int(input("enter value : "))
a = int(input("enter another value: "))
print(l is a)


# In[ ]:




