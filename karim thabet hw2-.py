#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = 0
while n < 10:
    if n == 5:
        break
    print(n)    
    n = n + 1
    


# In[3]:


n = 0
while n < 5:
    print(n)
    n = n +1
else:
    print(n, "is not less than 5")


# In[14]:


fruitlist = ["orange", "banana", "kiwi", "apple"]
i = len(fruitlist)
for A in range(0,i):
    if fruitlist[A] == "apple":
        print("Is apple really a fruit?")
        break
    print("I like", fruitlist[A])
    
    
    


# In[63]:


weather = {
    "sunny":"play",
    "rainy": "watch tv",
    "cloudy": "walk" 
}

print("when sunny", "let us",weather["sunny"])
print("when rainy", "let us",weather["rainy"])
print("when cloudy", "let us",weather["cloudy"])


# In[86]:


weather = {
    "sunny":"play",
    "rainy": "watch tv",
    "cloudy": "walk", 
    
}

print("when sunny", "let us",weather["sunny"])
print("when rainy", "let us",weather["rainy"])
print("when cloudy", "let us",weather["cloudy"])

weather["snowy"]="ski"


# In[107]:


weather =	{
  "sunny": "run",
  "rainy": "watch tv",
  "cloudy": "walk"
}

for key in weather:
    if [key]=="sunny":
        print("when", key, "lets" ,  weather[key])
    elif [key]=="rainy":
        print("when", key, "lets" , weather[key])
    else:
        print("when", key, "lets" , weather[key])


# In[93]:


grade = 92
if grade >= 90:
  grade = 'A'
elif grade >= 80:
  grade = 'B'
elif grade >= 70:
  grade = 'C'
elif grade >= 60:
  grade = 'D'
else:
  grade = 'F'
print(grade)


# In[95]:





# In[ ]:




