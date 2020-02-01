#!/usr/bin/env python
# coding: utf-8

# In[5]:


#One way (Notice:keep module file and "calling file" together---calling file means in which file u can call all functions)
import Functions   #Functions has been created as a module in (c/users/(pcname) 
                   #(keep Functions.py file in this path without calling the function name))
Functions.hw()


# In[6]:


Functions.add()


# In[7]:


Functions.sub(12,10)


# In[8]:


#Another way
from Functions import mul
var4= mul()       
print("Multiplication:",var4)
#But this process is too lenthy because you hvae to import all functions one by one that's why follow the next cell 


# In[10]:


from Functions import *
var4=div(9,3)
print("Division:",var4)
hw()
#by using * u can call any functions of Functions module


# In[ ]:




