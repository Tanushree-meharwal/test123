#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python script to calculate sum of first N natural numbers.
num = int(input("Enter the number: "))
sum = 0
for i in range(num+1):
    sum = sum+i
print(f"Sum of first {num} Natural numbers is {sum}.")


# In[ ]:


#2. Write a python script to calculate sum of squares of first N natural numbers.
num = int(input("Enter the number: "))
sum = 0
for i in range(num+1):
    sum = sum+i**2
print(f"Sum of squares of first {num} Natural numbers is {sum}.")


# In[ ]:


#3. Write a python script to calculate sum of cubes of first N natural numbers.
num = int(input("Enter the number: "))
sum = 0
for i in range(num+1):
    sum = sum+i**3
print(f"Sum of cubes of first {num} Natural numbers is {sum}.")


# In[ ]:


#4. Write a python script to calculate sum of first N odd natural numbers.
num = int(input("enter the number:"))
sum = 0
for i in range(num*2):
    if i%2!= 0:
        sum = sum+i
print(f"sum of first {num} odd natural numbers is {sum}.")


# In[ ]:


#5. Write a python script to calculate sum of first N even natural numbers.
num = int(input("enter the number:"))
sum = 0
for i in range(num*2):
    if i%2== 0:
        sum = sum+i
print(f"sum of first {num} even natural numbers is {sum}.")


# In[ ]:


#6. Write a python script to calculate factorial of a given number.
num = int(input("enter the number:"))
fact = 1
for i in range(num):
    fact = fact*(num-i)
print( f"factorial of a given number {num} is {fact}.")


# In[ ]:


#7. Write a python script to count digits in a given number.
count = 0
num = int(input("enter the number: "))
while(num!=0):
    num = num//10
    count+=1
print(f"Given Number have {count} digit.")    


# In[ ]:


#8. Write a python script to calculate sum of digits of a given number.
count = 0
sum = 0
num = int(input("enter the number: "))
while(num!=0):
    num = num//10
    count+=1
    sum = sum+count 
print(f"sum of digits of a given number is {sum}.") 


# In[25]:


#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method).
num = list(input(" Enter the binary number: "))
result = 0
for i in range(len(num)):
    digit = num.pop()
    if digit =='1':
        result = result+pow(2,i)
print(f"binary equivalent of decimal number is {result}.")    


# In[26]:


#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
num = list(input("Enter the octal number: "))
result = 0
for i in range(len(num)):
    digit = num.pop()
    result = int(digit)*pow(8,i)+result
print(f"octal equivalent of decimal number is {result}.")


# In[ ]:




