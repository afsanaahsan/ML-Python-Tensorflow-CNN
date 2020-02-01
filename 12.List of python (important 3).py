#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(["cat","bat","rat"]) #direct print


# In[2]:


print(["cat","bat","rat",123,12.4,True,None]) 
#difference between array and list
#In list you can use any type of data together like (int,string,float,boolian...) 
#But in array you have to use or store same type of data in a variable


# In[10]:


animals = ['cat','bat','rat',123,12.4,True,None] #cat=0,bat=1,rat=3......
print(animals)
len(animals)


# In[5]:


#Index means the position of the data of a list
print(animals[0])   #index print of list


# In[8]:


print(animals[-5])     #None=-1,True=-2,.....cat=-7,bat=-6,rat=-5......


# In[4]:


print(animals[0:3])


# In[6]:


print("Hello "+animals[0])   #you can use anything of a list


# In[16]:


#this list like: [[1,2,3,4,5],
                #["cat","bat","rat"]] 

var2=[[1,2,3,4,5],["cat","bat","rat"]]   # multiple list
print(var2)
print(var2[1][2])               #[row][column] that means 1 no row er 2 no data (row and column start from 0)


# In[21]:


#Append function
var3=['jeny','masum','roman','john']
var3.append('seth')    #value add function but by append, whatever we awnt to add it will be added the last of the list
print(var3)


# In[22]:


#Insert function
var3.insert(2,'michle')    #by insert, we chave to add the data with index.
print(var3)


# In[23]:


#Remove function
var3.remove('michle')
print(var3)


# In[25]:


#Sort function
var4=[-7,-5,45,3,67]
var4.sort()            #First of all u have to call seperatley then print.
print(var4)


# In[ ]:




