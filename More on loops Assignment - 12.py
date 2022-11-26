#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python script to reverse a number.
num = int(input("Enter your number"))
r_num = 0
while num!=0:
    digit = num%10
    r_num = r_num*10+digit
    num//=10
print(r_num)


# In[ ]:


#2. Write a python script to check whether a given number is Prime or not.
num = int(input("enter the number: "))
for i in range(2,num):
    if num%i==0:
        print(f"Given number {num} is not prime.")
        break
    else:
        print(f"Given number {num} is prime.")
        break


# In[ ]:


#3. Write a python script to print all Prime numbers under 100.
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)


# In[ ]:


#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
a = int(input("Enter the first limit: "))
b = int(input("Enter the second limit: "))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)


# In[2]:


#5.Write a python script to find next prime number of a given number.
n = int(input("enter the number: "))
while True:
    n+=1
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print(n)
        break


# In[ ]:


#6. Write a python script to print first N prime numbers.
b = int(input("Enter the number: "))
for i in range(2,b+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)


# In[ ]:


#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
f_num = int(input("enter the first number: "))
s_num = int(input("enter the second number:  "))
i = 1
while(i<=f_num*s_num):
    if ((i%f_num==0)and(i%s_num==0)):
        H = f_num*s_num/i;
        if (H == 1):
            print("given number is co-prime.")
        else:
            print("Given number is not co-prime.")
            break
    i+=1 


# In[ ]:


#8. Write a python script to print first N terms of a Fibonacci series.
a = 0 
b = 1
n = int(input("enter the number: "))
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c,end=' ')
    


# In[ ]:


#9. Write a python script to calculate LCM of two numbers.
f_num = int(input("enter the first number: "))
s_num = int(input("enter the second number:  "))
i = 1
while(i<=f_num*s_num):
    if ((i%f_num==0)and(i%s_num==0)):
        print(f"LCM {i} of first number {f_num} and second number {s_num}.")
        break
    i+=1    


# In[ ]:


#10. Write a python script to calculate HCF of two numbers.
f_num = int(input("enter the first number: "))
s_num = int(input("enter the second number:  "))
i = 1
while(i<=f_num*s_num):
    if ((i%f_num==0)and(i%s_num==0)):
        H = f_num*s_num/i;
        print(f" HCF {H} of first number {f_num} and second number {s_num}.")
        break
    i+=1 


# In[ ]:




