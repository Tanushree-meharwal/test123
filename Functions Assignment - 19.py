#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. Write a python program to create a simple function which prints “MySirG” .
def printN1(n):
    for i in range(n):
        print("MySirG")
def printN():
    print("MySirG")   
printN1(2) # function calling
printN()


# In[5]:


#2. Write a python program to create a function which expects two arguments and print them in the function body.
def exp(a,b):
    print(a)
    print(b)
exp(2,3)   # function calling 


# In[6]:


#3. Write a python program to create a function which expects an unknown number of arguments.
def unknown(*n):
    average = sum(n)/len(n)
    print(average)
unknown(2,3,4,5) # function calling   


# In[7]:


#4. Write a python program to create a function which expects kwargs arguments.
def arg(a,b):
    print(a)
    print(b)
arg(b=2,a=5)   # function calling


# In[2]:


#5. Write a python program to create a function which expects a list as an argument.
def list1(l):
    list_1= []
    for i in l:
        list_1.append(i)
    print(list_1)
l2 = [1,2,3,4,'hello',45,55]
list1(l2)        # function calling
        


# In[8]:


#6. Write a python program to create a function that finds a maximum of four numbers.
def max(a,b=0,c=0,d=0):
    if a>b and a>c and a>d:
        print(f"maximum number is {a}")
    elif b>a and b>c and b>d:
        print(f"maximum number is {b}")
    elif c>a and c>d and c>b:
        print(f"maximum number is {c}")
    elif d>a and d>b and d>c:
        print(f"maximum number is {d}")
    else:
        print(f"all number is same" )
max(2,3,4,5)# function calling
max(34,45)        


# In[3]:


#7. Write a python program to sum all the numbers in a list.
def sum(l):
    s = 0
    for i in l:
        if type(i)== int or type(i)== float:
            s = s+i
    return s 
listr = [2,6,4,5,8.9,'hello']
sum(listr) # function calling


# In[9]:


#8. Write a python program to multiply all the numbers in a list.
def mul(l):
    m = 1
    for i in l:
        if type(i)== int or type(i)== float:
            m = m*i
    return m 
listm = [2,6,4,5,8.9,'hello'] 
mul(listm)# function calling


# In[10]:


#9. Write a python program to create a function to check whether a number falls in a given range.
def check(n):
    for i in range(1,1001):
        if i == n:
            print(f"yes,given number {n} in range.")
            break;
        elif n>1000:
            print("no,given number {n} is not in range.")
            break;
check(34)   


# In[11]:


#10. Write a python program to create a function to check whether a given number is even or odd.
def check(a):    
    if a%2==0:
        print(f"given number {a} is even.")
    else :
        print(f"given number {a} is odd.")
check(35)        # function calling    

