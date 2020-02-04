#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.0,2.0,0.01)

s= 1 + np.cos(2*np.pi*t)            #In numpy library, there will be all trigonometry function.

plt.plot(t,s,'--')                 #The line will be 'g'=green,'r'=red,'*'=star format
plt.grid()                         #Grid will be showed
plt.xlabel("Time(t)")
plt.ylabel("Voltage(v)")
plt.title("Cosine wave plot(cos(x))")

plt.show()


# In[ ]:




