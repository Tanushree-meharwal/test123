#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python script to create a list of first N natural numbers.
num = int(input("How many number u wants in series: "))
list1 = []
for i in range(1,num+1):
    list1.append(i)
print(f"This is your {num} Number list:",list1)    


# In[ ]:


#2. Write a Python script to create a list of first N odd natural numbers.
num = int(input("How many odd number u wants in series: "))
list1 = []
for i in range(1,num*2):
    if i%2!=0:
        list1.append(i)
print(f"This is your {num} odd Number list:",list1)    


# In[ ]:


#3. Write a Python script to create a list of first N even natural numbers.
num = int(input("How many even number u wants in series: "))
list1 = []
for i in range(1,num*2+1):
    if i%2==0:
        list1.append(i)
print(f"This is your {num} even Number list:",list1)    


# In[ ]:


#4. Write a Python script to find the greatest number in a given list of numbers.
num = int(input("How many number u wants in series: "))
list1 = []
for i in range(1,num+1):
    number = int(input("enter your fav number: "))
    list1.append(number)
print(f"This is your {num} Number list:",list1) 
print(f"maximum number {max(list1)} ")


# In[ ]:


#5. Write a Python script to find the smallest number in a given list of numbers.
num = int(input("How many number u wants in series: "))
list1 = []
for i in range(1,num+1):
    number = int(input("enter your fav number: "))
    list1.append(number)
print(f"This is your {num} Number list:",list1) 
print(f"minimum number {min(list1)} ")


# In[ ]:


#6. Write a Python script to calculate the sum of elements in a given list of numbers.
num = int(input("How many number u wants in series: "))
sum = 0
list1 = []
for i in range(1,num+1):
    number = int(input("enter your fav number: "))
    list1.append(number)
    sum = sum+number
print(f"This is your {num} Number list:",list1) 
print(f"{sum} is sum of the list.")


# In[ ]:


#7. Write a Python script to remove all non int values from a list.
list1 = [12,34,45,"hello",67,89,"world"]
for i in list1:
    if type(i) != int:
         list1.remove(i)         
print("list after removing all non int values",list1)


# In[5]:


#8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
list1 = [12,"hello",12,12,34,45,67,89,67,34,45,"hello",67,89,"world"]
freq = {}
for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("elements along with their frequencies of occurrence in the list: ",freq)   


# In[3]:


#9. Write a Python script to print indices of all occurrences of a given element in a given list.
list1 = [12,12,12,34,45,67,89,67,34,45]
for i in range(len(list1)):
    if(list1[i] == 1):
        print(i)


# In[4]:


#10. Write a python script to sort a list.
list1 = [12,12,12,34,45,67,89,67,34,45]
list1.sort()
print("after sorting the list:",list1)


# In[ ]:




