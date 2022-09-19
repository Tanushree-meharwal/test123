#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q - 1 Write a python script to take your name as input from the user and then print it.
Name = input("Enter your Name: ")
print(Name)


# In[ ]:


# Q - 2 Write a python script to take input from the user. Input must be a number.
Number = float(input("Enter your Number: "))
print(Number)


# In[3]:


""" Q -3 Write a python script which takes two numbers from the user, then calculate their sum
and display the result."""
first_num = float(input("Enter your First Number: "))
second_num = float(input("Enter your Second Number: "))
total = first_num + second_num
print(total)
#print(a+b)


# In[2]:


# Q - 4 Write a python script which takes the radius from the user and display area of a circle.
radius = float(input("Enter Radius: "))
area = (22/7)*radius**2
#d = 3.14*radius**2
#print(d)
print("Area of circle is ",area)


# In[3]:


# Q - 5 Write a python script to calculate the square of a number. Number is entered by the user.
num = float(input("Enter your Number: "))
square = num**2
print(f"Square of {num} is ",square)


# In[4]:


# Q - 6 Write a python script to calculate the area of Triangle. Number is entered by the user.
base = float(input("Enter Base of Triangle: "))
height = float(input("Enter Height of Triangle: "))
area = (1/2)*base*height
print("Area of Triangle is ",area)


# In[5]:


# Q - 7 Write a python script to calculate average of three numbers, entered by the user
num_1 = float(input("Enter your First Number: "))
num_2 = float(input("Enter your Second Number: "))
num_3 = float(input("Enter your Third Number: "))
ave = (num_1 + num_2 + num_3)/3
print("Average of Three Number is ",ave)


# In[14]:


# Q - 8 Write a python script to calculate simple interest
amount = float(input("Enter your principal amount: "))
rate = float(input("Enter your rate of interest: "))
time = float(input("Enter period of time(in month): "))
SI = (amount*rate*time)/100
print("Simple Interest is ",SI)


# In[15]:


# Q - 9 Write a python script to calculate the volume of a cuboid.
length = float(input("Enter the length of cuboid: "))
breadth = float(input("Enter the breadth of cuboid: "))
height = float(input("Enter the height of cuboid: "))
vol = length*breadth*height
print("Volume of cuboid is ",vol)


# In[16]:


# Q - 10 Write a python script to calculate area of a rectangle.
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
area = length*breadth
print("Area of Rectangle is ",area)


# In[ ]:




