#!/usr/bin/env python
# coding: utf-8

# In[3]:


name=input("Please enter your name:")
age=int(input("Enter your age:"))
if age>18:
    print("You have been given permission for vote!")
else:
    print("You haven\'t been given permission for vote!")
    print("Come plz after {} years!!!".format(18-age))   #most importnat to print different numbers in one line


# In[7]:


print("Guess a number among 1-10")
number=int(input("Enter a number:"))
if number<5:
    print("Guess higher!!")
    number=int(input("Again enter a number:"))
    if number==5:
        print("You are correct :-)")
    else:
        print("Still you are wrong but sorry you don\'t get a chance again :-(")
elif number>5:
    print("Guess lower!!")
    number=int(input("Again enter a number:"))
    if number==5:
        print("You are correct :-)")
    else:
        print("Still you are wrong but sorry you don\'t get a chance again :-(")
else:
    print("Wow!!!! You got it first time :-D")


# In[ ]:




