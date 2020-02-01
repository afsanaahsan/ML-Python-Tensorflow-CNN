#!/usr/bin/env python
# coding: utf-8

# In[3]:


name="Masum"
while True:
    print("Enter your name:")
    name1=input()
    if(name1==name):
        break
print("Thank you so much Jeny!!")


# In[6]:


while True:
    print("Who are you??")
    name=input()
    if(name!="Masum"):
        continue
    print("Hello,{} Enter a valid password!!!".format(name))
    password=input()
    if(password=="Roman_Reigns"):
        break
print("Congrats {}, Access granted - Welcome to the clash of clan!!".format(name))


# In[ ]:




