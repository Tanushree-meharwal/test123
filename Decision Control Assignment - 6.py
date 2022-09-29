#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q - 1 Write a python script to check whether a given number is positive or non-positive
num = int(input("Enter any Number: "))
if num>0:
    print("Number is Positive")
else:
    print("Number is Non Positive")
#if else comprehension
print("Number is Positive" if num>0 else "Number is Non Positive")   


# In[ ]:


# Q - 2 Write a python script to check whether a given number is divisible by 5 or not.
num = int(input("Enter any Number: "))
if num%5==0:
    print("Number is divisible by 5")
else:
    print("NUmber is not divisible by 5")
# if else comprehension
print("Number is divisible by 5" if num%5==0 else "NUmber is not divisible by 5") 


# In[ ]:


# Q - 3 Write a python script to check whether a given number is even or odd.
num = int(input("Enter any Number: "))
if num%2==0:
    print("given number is even")
else:
    print("given number is odd")
# if else comprehension
print("given number is even" if num%2==0 else "given number is odd")


# In[ ]:


# Q - 4 Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same.
num_1 = int(input("Enter any Number: "))
num_2 = int(input("Enter another number :")) 
if num_1>num_2:
    print(f"{num_1} is greater ")
elif num_1<num_2:
    print(f"{num_1} is small")
else:
    print(f"Both numbers {num_1} are the same")


# In[ ]:


# Q - 5 Write a python script to print two given words in dictionary order.
a = input("enetr first word : ")
b = input("enter second word : ")
if a>b:
    print((a,b))
else:
    print((b,a))   


# In[ ]:


# Q - 6 Write a python script to check whether a given number is a three digit number or not.
num = int(input("enter your number: "))
print("three digit number"if 99<num<1000 else "number is not three digit")


# In[ ]:


# Q - 7 Write a python script to check whether a given number is positive, negative or zero.
num = int(input("enter any number :"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")


# In[ ]:


""" Q - 8 Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
a = int(input("enter  coefficient of x**2 :"))
b = int(input("enter coefficient of x: "))
c = int(input("enter constant value :"))
d = b**2-4*a*c
if d>0:
    print("quadratic equation has two real & distinct roots")
elif d<0:
    print("quadratic equation has two imaginary & distinct roots")
else:
    print("quadratic equation has two real & equal roots")


# In[ ]:


# Q - 9 Write a python script to check whether a given year is a leap year or not.
year = int(input("enetr number of year :"))
if year%400==0:
    print("given year is a leap year")
elif year%100!=0 and year%4==0:
    print("given year is a leap year")
else:
    print("given year is not a leap year")


# In[ ]:


""" Q - 10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
num_3 = int(input("enter third number:"))
if num_1>num_2 and num_1>num_3:
    print(f"first number {num_1} isgreater among three numbers")
elif num_2>num_1 and num_2>num_3:
    print(f"second number {num_2} isgreater among three numbers")
elif num_3>num_1 and num_3>num_2:
    print(f"third number {num_3} is greater among three numbers")
else:
    print(f"all three numbers {num_1} are same")


# In[ ]:


""" Q - 11 Write a python script to take the month value in numeric format and display the
number of days in it."""
month_num = int(input("enter any month number"))
if month_num in (1,3,5,7,8,10,12):
    print("31 days in this month")
elif month_num in (4,6,9,11):
    print("30 days in this month")
elif month_num == 2:
    print("28 or 29 days")
else:
    print("Invalid month number.")    


# In[ ]:


""" Q- 12 Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""
complex_num = complex(input("enter your number : "))
if complex_num.real >complex_num.imag:
    print(complex_num.real)
else:
    print(complex_num.imag)


# In[ ]:




