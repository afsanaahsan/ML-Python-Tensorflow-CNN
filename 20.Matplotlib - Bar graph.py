#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [10,24,36,40,50]

label = ['Maldeep','Srilanka','Nepal','Bangladesh','India']

plt.bar(x,y,tick_label=label,width = 0.7,color=['green','blue'])    #1st bar will be green,2nd bar will be blue,3rd green...

plt.xlabel('x-axis')

plt.ylabel('y-axis')

plt.title('Bar Graph(Population)')

plt.show()


# In[ ]:





# In[ ]:




