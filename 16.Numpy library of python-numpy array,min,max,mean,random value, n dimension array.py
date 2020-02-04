#!/usr/bin/env python
# coding: utf-8

# In[2]:


#In numpy, everything will be happening by form of array.
import numpy as np
array=[1,2,3,4,5]
arr=np.array(array)
print(arr)


# In[13]:


np.arange(0,10)


# In[14]:


np.arange(0,10,2)


# In[15]:


np.zeros(5)


# In[16]:


np.zeros((3,5))


# In[19]:


np.ones((3,5))


# In[27]:


np.random.randint(0,10)         #Take random variable from 0 to 9


# In[30]:


np.random.randint(0,1000,(4,4))     # 4 dimension random array generate 


# In[33]:


np.random.seed(101)
np.random.randint(0,1000,(4,4))     # 4 dimension stable array generate using seed function.


# In[48]:


array = np.random.randint(0,1000,(4,4)) 
print(array)
array.max()                        # Max number determine 
array.min()                        # Min number determine 
array.mean()                       # Average calculate
array.argmax()                     # Provide the index of maximum value
array.argmin()                     # Provide the index of minimum value


# In[47]:


np.random.seed(101)
array1=np.random.randint(0,100,10)
print(array1)
array1.reshape(2,5)              #Array split


# In[49]:


mat=np.arange(0,100).reshape(10,10)
mat


# In[51]:


mat[0,1]       #print value by index
mat[2,2]


# In[57]:


mat[0,:]    #All value of 0 no row


# In[60]:


mat[:,0]    #All value of 0 no column


# In[61]:


mat[0:3,0:3]       


# In[ ]:




