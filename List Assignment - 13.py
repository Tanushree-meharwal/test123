#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list.
list1 = []
print(type(list1))
i = 0
while(i<4):
    n = input("enter the element of list:")
    list1.append(n)
    i+=1
print(list1)    


# In[ ]:


#2. Write a python script to get the data type of a list.
l1 = ['SQL',"python",1,2,3]
type(l1[3])


# In[ ]:


#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"]).
mylist = ["Java", "C", "Python"]
last_item = mylist.pop()
print(last_item)
print(mylist)


# In[ ]:


"""4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist 
= ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]"""
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist[1] = "NoSQL"
thislist[3] = "Flutter"
print(thislist)


# In[ ]:


#5. Write a python script to add an item to the end of the list (item “Python”. (mylist =["Java", "SQL", "C", "Reactnative"])
mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append("python")
print(mylist)


# In[ ]:


"""6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )"""
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.append(secondlist)
print(firstlist)


# In[ ]:


"""7. Write a python program to Print all items by referring to their index number (thislist =["Java", "SQL", "C","Reactnative"
,"Javascript", "Python"]"""
thislist =["Java", "SQL", "C","Reactnative","Javascript", "Python"]
print("0 element =",thislist[0],"\n1 element =",thislist[1],"\n2 element =",thislist[2],"\n3 element =",thislist[3],"\n4 element =",thislist[4],"\n5 element =",thislist[5])


# In[ ]:


#8. Write a python program to sort the list alphanumerically(thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"])
thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)


# In[3]:


#9. Write a Python script to create a list of city names taken from the user.
l1 = []
n = int(input("how many city you want in the list"))
i = 0 
while i<n:
    name = input("Enter your city name:")
    l1.append(name)
    i+=1
print(l1)


# In[2]:


# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.
l1 = []
n = int(input("how many number you want in the list"))
i = 0 
while i<n:
    name = int(input("Enter your number:"))
    l1.append(name)
    i+=1
print(l1)


# In[ ]:




