#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[1]:


a = 1
b = 2
a+b


# $ a + (b)^2 $

# In[2]:


a+b**2


# $ (a \times 2) + b^2 $

# In[3]:


a*2+b**2


# In[5]:


print("a is equal to", a)


# In[6]:


print("b is equal to", b)


# In[7]:


def add_number(x, y):
    return x+y

add_number(1,2)


# In[8]:


def add_number(a, b):
    return ((a)**2 + b)*2

add_number(1,2)


# In[9]:


def add_number(a, b):
    return ((a)**2 + b)*2

add_number(81,27)


# In[11]:


def add_number(x, y, z = None):
    if (z == None):
        return x+y
    else:
        return x+y+z
    
print(add_number(1,2))
print(add_number(1,2,3))


# In[12]:


def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))


# In[13]:


def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)


# I played a bit more than what those videos were showing!!! :)

# # Types and Sequences

# In[14]:


type('This is a string')


# In[15]:


type(None)


# In[16]:


type(1)


# In[17]:


type(1.0)


# In[18]:


type(add_numbers)


# In[19]:


x = (1, 'a', 2, 'b')
type(x)


# In[20]:


x = [1, 'a', 2, 'b']
type(x)


# In[21]:


x.append(3.3)
print(x)


# In[22]:


for item in x:
    print(item)


# In[23]:


i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1


# In[24]:


[1,2] + [3,4]


# In[25]:


[1]*3


# In[26]:


x = 'This is a string'
print(x[0]) 
print(x[0:1]) 
print(x[0:2]) 


# In[27]:


x[-7]


# In[28]:


x[-8]


# In[30]:


x[-8:-2]


# In[31]:


x[-4:-2]


# In[33]:


x[6:]


# In[34]:


firstname = 'Aru'
lastname = 'Bhardwaj'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Aru' in firstname)


# In[35]:


firstname = 'Aru Bhardwaj'.split(' ')[0] 
lastname = 'Aru Bhardwaj'.split(' ')[-1] 
print(firstname)
print(lastname)


# In[39]:


x = {'Aru Bhardwaj': 'arubhardwaj@hotmail.com', 'Bill Gates': 'billg@microsoft.com'}
x['Aru Bhardwaj'] 


# # More on Strings

# In[40]:


print('Aru' + str(2))


# In[41]:


print('Aru', 2)


# # Reading CSV Files

# In[62]:


import pandas as pd
import csv


# In[63]:


csvfile = pd.read_csv("E:\mpg.csv")


# In[68]:


mpg = list(csv.DictReader(csvfile))

mpg[:3]


# In[69]:


len(mpg)


# # Dates and Times

# In[70]:


import datetime as dt
import time as tm


# In[71]:


tm.time()


# In[72]:


dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow


# In[73]:


dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second 


# In[74]:


dtnow.day, dtnow.month, dtnow.year, dtnow.hour, dtnow.minute, dtnow.second 


# In[79]:


print("Today's date is", dtnow.day, dtnow.month, dtnow.year)


# In[80]:


print("Today's date is", dtnow.day, "/", dtnow.month, "/", dtnow.year)


# # Objects and map()

# In[81]:


class Person:
    department = 'School of Economics'
    
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location


# In[83]:


person = Person()
person.set_name('Aru Bhardwaj')
person.set_location('India')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))


# In[86]:


store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest


# In[88]:


for item in cheapest:
    print(item)


# In Video question

# In[89]:


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))


# # Lambda and List Comprehensions

# In[96]:


my_function = lambda a,b,c:a+b


# In[97]:


my_function(1,2,3)


# In[98]:


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


# # Working with Numpy

# In[99]:


import numpy as np


# In[100]:


mylist = [1, 2, 3]
x = np.array(mylist)
x


# In[101]:


y = np.array([4, 5, 6])
y


# In[104]:


m = np.array([[7, 8, 9], [10, 11, 12]])
m


# In[105]:


m.shape


# In[109]:


n = np.arange(0,30,2)
n


# In[111]:


o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
o


# In[112]:



o.resize(3, 3)
o


# In[113]:


np.ones((3, 2))


# In[116]:


np.zeros((2, 3))


# In[117]:


np.eye(3)


# In[118]:



p = np.ones([2, 3], int)
p


# In[119]:


np.vstack([p, 2*p])


# In[120]:


np.hstack([p, 2*p])


# ## Operations

# In[121]:


print(x+y)
print(x-y)


# In[122]:


z = np.array([y, y**2])
print(np.shape(z))
print(len(z))


# In[123]:


z = np.array([y, y**2])
z


# In[124]:


a = np.array([-4, -2, 1, 3, 5])


# In[125]:


a.sum()


# In[126]:


a.max()


# In[127]:


r[0:6,::-7]


# In[ ]:




