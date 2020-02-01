#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#functions
def hw():
    print("Hello world")
hw()


# In[ ]:


#no argument and no return type
def add():   #argument means give some parameters or conditions into function's bracket
    var1=int(input("Enter 1st num:"))
    var2=int(input("Enter 2nd num:"))
    
    var3=var1+var2
    print("Addition:",var3) #print("Addition:"+str(var3))#if u print like this way then you have to convert this int as a sring.
add()


# In[ ]:


#with argument but no return type
def sub(var1,var2):
    var3=var1-var2
    
    print("Subtract:",var3)
sub(12,10)
    


# In[ ]:


# no argument and return type
def mul():
    var1=int(input("Enter 1st num:"))
    var2=int(input("Enter 2nd num:"))
    
    var3=var1*var2
    return var3

var4= mul()       #as it returns something then after return it keeps the value into var4
print("Multiplication:",var4)


# In[ ]:


#with argument and return type
def div(var1,var2):
    var3=var1/var2
    return var3

var4=div(9,3)
print("Division:",var4)

#we have used same type of variable in every function but it is actually local variable so it doesn't affect in any functions.
    


# In[ ]:




