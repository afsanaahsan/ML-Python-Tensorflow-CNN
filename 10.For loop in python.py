#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(20):     #Range function automatically consider the starting point from 0 . 
    print("The value of i is {}".format(i))


# In[2]:


for i in range(1,20):     #If you want to start from 1 then start simply from 1 . 
    print("The value of i is {}".format(i))


# In[6]:


for i in range(1,20,3):     #If you want to increment(2 or 3) in the loop then add the third position of range function . 
    print("The value of i is {}".format(i))


# In[8]:


for i in range(20,1,-3):     #If you want to decrement(2 or 3) in the loop then add the third position of range function . 
    print("The value of i is {}".format(i))


# In[10]:


for i in range(0,20,5): 
    print(i,end="")     #python automatically takes new line. To close this, you can give end="" ,then it prints side by side.


# In[ ]:




