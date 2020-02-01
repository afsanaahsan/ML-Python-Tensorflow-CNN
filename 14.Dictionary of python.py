#!/usr/bin/env python
# coding: utf-8

# In[2]:


#dictionary is also used to store data and list as well. But for different type of data dictionary is best to use
#because it is a good practice.
#In list we store the data through index but in dictionary we store the data through "KEY".(difference)

dictio= {'size':'fat','color':'gray','disposition':'loud'}  #size=key and fat=value.....
print(dictio['color'])


# In[3]:


spam1 =['cat','dog','rat']
spam2 =['dog','rat','cat']
spam1 == spam2              #output will be false because index didn't match.


# In[5]:


dictio1= {'size':'fat','color':'gray','disposition':'loud'}
dictio2= {'disposition':'loud','color':'gray','size':'fat'}
dictio1 == dictio2         #output will be true because index doesn't use.


# In[7]:


spam = {'name':'jeny','gender':'F','age':'22'}

for v in spam.keys():        #print all keys
    print(v)


# In[10]:


spam = {'name':'jeny','gender':'F','age':'22'}

for w in spam.values():       #print all values
    print(w)


# In[11]:


spam = {'name':'jeny','gender':'F','age':'22'}

for m in spam.items():       #print all items
    print(m)


# In[ ]:




