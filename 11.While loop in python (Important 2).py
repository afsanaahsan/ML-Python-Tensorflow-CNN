#!/usr/bin/env python
# coding: utf-8

# In[2]:


var=0   #In "while loop", variable must be initialized first but in "for loop" there is no need to initialize the variable 
while var<=10:
    print("Value of var = ",var)
    var=var+1 # var += 1


# In[3]:


list= ["south","west","east"]
input_var=""                      # "not in" means not equal to
while input_var not in list:      # "not in" mane jei porjonto list er variable input akare na pabe ei loop choltei thakbe
    input_var=input("Enter the value of list=")   #User input
print("You are out of the loop and got your valid input!!")


# In[5]:


list= ["south","west","east"]
input_var=""                      
while input_var not in list:      
    input_var=input("Enter the value of list=")   
    if input_var=="quit":                          # how can you match with string
        print("Your game is over!!")
        break
print("You are out of the loop and got your valid input!!")


# In[ ]:





# In[ ]:




