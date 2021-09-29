#!/usr/bin/env python
# coding: utf-8

# In[4]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'jules':55, 'Arthur':77}


# In[5]:


for key in marks:
        print(key, marks[key])  


# In[25]:


import statistics 
Markslist = marks.values()
max_value = max(Markslist)
min_value= min(Markslist)

Mean_value = statistics.mean(Markslist)

print(Mean_value)
print(max_value)
print(min_value)


# In[19]:


for key in marks:
    name=key
    if name[0] == 'J':
        break
    print(key)


# In[26]:


for key in marks:
    name=key
    if name[0] == 'J':
       continue
    print(key)


# In[45]:


def student_grade(name):
    for key in marks:
        if key == name:
            print(marks[key])
            break
    else: print('can not find this students name')

            
student_grade('Amy')

            

        


# In[58]:


def less_than(num):
    n = 0
    while n < num:
        print(n,n**n)
        n = n + 1
    print("greater than", num)
less_than(8)

        


# In[68]:


def addint(num):
    n = 1
    sum = 0 
    while n in range(num + 1):
        sum = sum + n 
        n = n + 1
    print(sum)
addint(3)


# In[79]:


def addint(num):
    
    sum = 0 

    for n in range(1, num + 1):
        sum = sum + n 
        print(sum)
        n = n + 1
    
addint(3)


# In[89]:


def minimal(v1, v2, v3, v4):
    min_value = v1
    if v2 < min_value:
        min_value = v2
    if v3 < min_value:
        min_value = v3
    if v4 < min_value:
        min_value = v4
    return min_value
    
        
        
minimal(10,8,13,3)    


# In[ ]:





# In[ ]:




