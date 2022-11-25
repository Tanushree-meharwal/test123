#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q - 1 Write a python script to display the number of days in a given month number.
month = int(input("enter month number :"))
match month:
    case month if month in (1,3,5,7,8,10,12) :
        print("31 days ")
    case month if month in (4,6,9,11) :
        print("30 days")
    case 2 :
        print("28 or 29 days")    
    case _ :
        print("invalid month number")    


# In[ ]:


"""Q - 2 Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your choice: "))
match choice:
    case 1:    
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second numberaa; "))
        c = a+b
        print(f"sum of two number is {c}.")
    case 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second numberaa; "))
        c = a-b
        print(f"subtraction of two number is {c}.")
    case 3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second numberaa; "))
        c = a*b
        print(f"multipication of two number is {c}.")
    case 4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second numberaa; "))
        c = a/b
        print(f"Division of two number is {c}.")   
    case _:
        print("Invalid choice")   


# In[ ]:


"""Q - 3 Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""
print("1.Check whether a given set of three numbers are lengths of an isosceles triangle or not.")
print("2.Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("3.Check whether a given set of three numbers are equilateral triangle or not.")
print("4.Exit")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        f_side = float(input("Enter the first side of triangle: "))
        s_side = float(input("Enter the second side of triangle: "))
        t_side = float(input("Enter the third side of triangle: "))
        if (t_side == f_side or s_side == f_side or s_side == t_side):
            print("This triangle is isosceles.\n")
        else :
            print("This is not isosceles triangle.\n")
    case 2:  
        f_side = float(input("Enter the first side of triangle: "))
        s_side = float(input("Enter the second side of triangle: "))
        t_side = float(input("Enter the third side of triangle: ")) 
        if ((f_side*f_side + s_side*s_side == t_side*t_side)or(s_side*s_side + t_side*t_side == f_side*f_side)or(t_side*t_side + f_side*f_side == s_side*s_side)):
            print("This is right triangle.\n")
        else:
            print("This is not right triangle.\n")        
    case 3:
        f_side = float(input("Enter the first side of triangle: "))
        s_side = float(input("Enter the second side of triangle: "))
        t_side = float(input("Enter the third side of triangle: "))
        if (f_side == s_side and s_side == t_side):
            print("This is equilateral triangle.\n")
        else:
            print("This id not equilateral triangle.\n")
    case 4:
        print("Exit")
    case __:
        print("invalid choice")            
    


# In[ ]:


"""Q - 4 Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
age = int(input("enter your age: "))
match age:
    case age if (age<10):
        print("kid")
    case age if age<20:
        print("Teen") 
    case age if age<40:
        print("young")
    case age if age<60:
        print("Experienced")
    case age if(age==60 or age>60) :
        print("senior citizen")
    case __:
        print("invalid syntax")                  


# In[ ]:


"""Q - 5 Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""
a = int(input("Enter the number: "))
match a:
    case a if a%2==0:
        print("Saurabh shukla")
    case a if a>0 and a%2!=0:
        print("Aditya choudhry") 
    case a if a<0 and a%2!=0:
        print("Prateek jain") 
    case _:
        print("invalid output")          


# In[ ]:


"""Q - 6 Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""
s = input(" Enter a string: ")
match s:
    case s if ' ' in s:
        print("Multiword String")
    case s if ' ' in s:
        print("Single word string")


# In[ ]:


"""Q - 7 Write a python program to check whether a given number is positive, negative or
zero using match case statement"""
num = int(input("enter the number: "))
match num:
    case num if num>0:
        print(f"Given number {num} is Positive.")
    case num if num<0:
        print(f"Given number {num} is Negative.")
    case num if num == 0:
        print(f"Given number {num} is zero.") 


# In[ ]:


"""Q - 8 Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""
s1 = input("enter the first string: ")
s2 = input("enter the second string: ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical Strings")
    case (s1,s2) if s1>s2:
        print(f"{s1} comes after {s2}.")
    case (s1,s2) if s1<s2:
        print(f"{s2} comes after {s1}.")     


# In[ ]:


"""Q - 9 Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""
year = int(input("Enter the year number: "))
match year:
    case year if year%400==0:
        print(f"Given year {year} is century leap year.") 
    case year if (year%400!=0 and year%4==0) :
        print(f"Given year {year} is non century leap year.") 
    case year if  (year%400!=0 and year%4!=0):
        print(f"Given year {year} is non century non leap year.") 
    case year if (year%100!=0 and year%4!=0):
        print(f"Given year {year} is century non leap year.")  


# In[ ]:


"""Q - 10 Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""
s1 = input("Enter your favourite colour: ")
l1 = ["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in s1:
        c = colour
        break
else:
    c = "other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday") 
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")    

