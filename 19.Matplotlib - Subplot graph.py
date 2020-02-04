#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0,2.0)
x2 = np.linspace(0.0,2.0)

y1 = np.cos(2*np.pi*x1)*np.exp(-x1)     #line goes exponentially 
y2 = np.cos(2*np.pi*x2)

plt.subplot(2,1,1)          #2=row,1=col,1=1 no subplot
plt.plot(x1,y1,'o-')
plt.title('Subplot-1')
plt.xlabel('x1')
plt.ylabel('Amp(y1)')

plt.subplot(2,1,2)         #2=row,1=col,2=2 no subplot
plt.plot(x2,y2,'.-')
plt.title('Subplot-2')
plt.xlabel('x2')
plt.ylabel('Amp(y2)')

plt.show()


# In[ ]:




