#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Write a python script to create a String in 3 different possible ways.
str1 = "using double quote, this is the way of create string"
str2 = 'using singl quote , this is another way to create string'
str3 = str("using str keyword , we create string.")
print(str1)
print(str2)
print(str3)


# In[ ]:


#2. Write a python script to Get the characters from the start to position 5 (Given String“iNeuron” using the slice syntax)
st1 = "iNeuron"
print(st1[5])


# In[ ]:


#3.Write a python script to Get the characters from position 2 to position 5(Given String“Hello Learners” using the slice syntax)
st1 = "Hello Learner"
print(st1[2:5:1])


# In[ ]:


#4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a = "Learning"
b = "Python"
c = a+" "+b
print(c)


# In[ ]:


#5. Write a python script to get the count of total number of characters in String a=“iNeuron”
a = "iNeuron"
print("Total number of character present in string is",len(a))


# In[ ]:


#6. Write a python script to reverse a String. (“iNeuron”)
a = "iNeuron"
print("This is the reverse of the string:",a[-1::-1])


# In[6]:


#7. Write a python script to determine whether a string contains a specific substring.
st1 = "this is my first string program."
st2 = "string"
if st2 in st1:
    print("Yes,string contains a specific substring")
else:
    print("No,string not contains a specific substring")


# In[8]:


#8. Write a python script to check if a string contains only numbers.
st1 = "1234567843534"
st2 = "abcdjhgeh"
if st1.isdigit():
    print("St1 contain digits only.")
else:
    print("St1 not contain digits only.")
if st2.isdigit():
    print("St2 contain digits only.")
else:
    print("St2 not contain digits only.")


# In[9]:


#9. Write a python script to check if a string contains only characters of the alphabet.
st1 = "1234567843534"
st2 = "abcdjhgeh"
if st1.isalpha():
    print("St1 contain characters only.")
else:
    print("St1 not contain characters only.")
if st2.isalpha():
    print("St2 contain characters only.")
else:
    print("St2 not contain characters only.")


# In[17]:


#10. Write a python script to convert an integer to a string.
inte = 2345
inte = str(inte)
print("integer to string:",inte)
type(inte)

