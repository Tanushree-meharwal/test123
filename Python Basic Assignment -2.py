#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q - 1 Write a python script to add comments and print “Learning Python” on screen.
# This is a single line comment.
print("Learning Python")


# In[1]:


""" Q - 2 Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values."""
a = int(input("Enter any number: "))
b = input("Enter value: ")
c = float(input("Enter any number:"))
d = bool(input("Enter value:"))
""" a is a integer value.
b is a string .
c is a float value 
d is a boolen .
"""
print(a,b,c,d,sep="\n")
print(str(a) + '\n' + b +'\n' + str(c) + '\n' + str(d) )


# In[ ]:


""" Q - 3 Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)"""
a = 35 
b = False 
c = "MySirG"
d = 5.46
e = 3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# In[ ]:


# Q - 4 Write a python script to print the id of two variables containing the same integer values.
a = 3
b = 3
c = 3
#print(id(c))
print(id(a))
print(id(b))


# In[ ]:


""" Q - 5 Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable."""
a = 345
b = "LEARN SOMETHING NEW"
c = 45.5
d = 4+5j
print(a,type(a),id(a))
print(b,type(b),id(b))
print(c,type(c),id(c))
print(d,type(d),id(d))


# In[ ]:


# Q - 6 Write a python script to print all the keywords
#import keyword as k
"""jb bi print krwana ho to (module name.module element)  """
#print(k.kwlist)
"""iska mtlb h ki aap pura keyword module ko import nhi kr ry 
ho sirf aap kwlist ko import kr ry ho """
from keyword import kwlist
print(kwlist)


# In[4]:


# Q - 7 On Python shell use help() function and display the list of keywords.
help('keywords')


# In[ ]:


""" Q - 8 Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py"""


# In[8]:


# Q - 9 Name the keywords, used as data in the Python script.
"""here is 3 keywords which is used as data like (False,True,None)"""
a = True 
b = False
c = None
print(a,b,c)
print(type(a),type(b),type(c))


# In[8]:


""" Q - 10 Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)"""
#import time

import datetime
dt = datetime.date.today()
d1 = dt.strftime("%d-%m-%Y and %I:%M %p")
print(d1)
    
#d1 = dt.strftime("%B %d %Y")
#d1 = dt.strftime("%d/%b/%y")
#d1 = dt.strftime("%H:%M:%S")
#d1 = dt.strftime("%d-%m-%y")
#print("Current date and time: " , datetime.datetime.now())
#print("Current year: ", datetime.date.today().strftime("%Y"))
#print("Month of year: ", datetime.date.today().strftime("%B"))
#print("Week number of the year: ", datetime.date.today().strftime("%W"))
#print("Weekday of the week: ", datetime.date.today().strftime("%w"))
#print("Day of year: ", datetime.date.today().strftime("%j"))
#print("Day of the month : ", datetime.date.today().strftime("%d"))
#print("Day of week: ", datetime.date.today().strftime("%A"))


# In[ ]:




