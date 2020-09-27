#!/usr/bin/env python
# coding: utf-8

# 1. Write a function to compute 5/0 and use try/except to catch the exceptions. 
# 

# In[1]:


def div_by_zero():
 return 5 / 0

try:
 div_by_zero()
except ZeroDivisionError as e:
 print("This is ' div by 0'error:",e)


# 2. Implement a Python program to generate all sentences where subject is in  ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in  ["Baseball","cricket"]. 
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
# subjects=["Americans ","Indians"] 
# verbs=["play","watch"] 
# objects=["Baseball","Cricket"] 
# Output should come as below: 
# Americans play Baseball. 
# Americans play Cricket. 
# Americans watch Baseball. 
# Americans watch Cricket. 
# Indians play Baseball. 
# Indians play Cricket. 
# Indians watch Baseball. 
# Indians watch Cricket.

# In[4]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates

sentence_list =[(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print(sentence)


# In[ ]:




