#!/usr/bin/env python
# coding: utf-8

# In[5]:


string='1234567890'
var=iter(string)
print(var)        #Location print
print(next(var))  #by using next function() the string could be printed.
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))


# In[6]:


string='1234567890'
for char in iter(string):    # iter means iterator function
    print(char)


# In[8]:


list=['sat','sun','mon','tues','wed','thurs','fri']
iterator=iter(list)
for chart in range(0,len(list)):
    iterator2=next(iterator)
    print(iterator2)


# In[9]:


list=['sat','sun','mon','tues','wed','thurs','fri']
for char in iter(list):    # iter means iterator function
    print(char)


# In[ ]:




