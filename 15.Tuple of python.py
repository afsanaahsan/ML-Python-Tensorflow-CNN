#!/usr/bin/env python
# coding: utf-8

# In[1]:


tuple=()
print(tuple)


# In[2]:


tuple1=(33, 3.3, 3+3j)
print(tuple)


# In[3]:


tuple2=(33, "33", [3, 3])
print(tuple)


# In[4]:


tuple3=(('x', 'y', 'z'), ('X', 'Y', 'Z'))
print(tuple)


# In[11]:


tuple3=(('x', 'y', 'z'), ('X', 'Y', 'Z'))
print(tuple3[0])
print(len(tuple3[0]))


# In[15]:


weekdays = ('mon', 'tue', 'wed' ,'thu', 'fri', 'sat', 'sun')
print(weekdays[1:])
print(weekdays[5:])
print(weekdays[-5])
print(weekdays[:])


# In[17]:


py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
for item in py_tuple:
        print("Item:", item)


# In[20]:


#tuple is immutable and list is mutable means you can add,delete,insert in list but not tuple

py_tuple = ['p', 'y', 't', 'h', 'o', 'n']
py_tuple[0] = 'a'         #In the ouput the new data will be added
print(py_tuple)
py_tuple2 = ('p', 'y', 't', 'h', 'o', 'n')
py_tuple2[0] = 'a'
print(py_tuple2)        #The output will produce an error.


# In[ ]:




