#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np
y1 = np.array ([1,2,3,4,5])
y2 = np.array ([5,6,7,8,9])
y3 = np.array ([9,10,11,12,13])

plt.plot(y1, linewidth = 5)
plt.plot(y2, linewidth = 5)
plt.plot(y3, linewidth = 5)


# In[2]:


import matplotlib.pyplot as plt

import numpy as np

 

x = np.random.normal(0, 0.2, 800)

plt.hist(x)

plt.show()


# In[1]:


import  matplotlib.pyplot as plt

fruits=['Apples', 'Bananas', 'Cherries', 'Dates']
Counts=[45, 25, 15, 20]

print(fruits)
print(Counts)


plt.bar(fruits, Counts)
plt.show()
plt.pie(Counts, labels= fruits)
plt.show()


# In[4]:


import numpy as np

import matplotlib.pyplot as plt

x=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

y=np.array([75, 59, 69, 48, 65, 56, 32, 45, 20, 30])

plt.scatter(x, y, c='lightblue', label='maths marks')

x=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

y=np.array([88, 92, 80, 89, 90, 80, 60, 88, 80, 84])

plt.scatter(x, y, c='coral', label='science marks')

plt.title('My chart')

plt.xlabel('Subject')

plt.ylabel('Marks')

plt.show()

 


# In[5]:


import  matplotlib.pyplot as plt

import numpy as np

#plot 1

x=np.array([1,1,2,3,5,6,6,7,8,9,10,12,17])

y=np.array([103, 111, 94, 99, 86, 86, 88, 87, 87, 85, 83, 82, 86])

plt.subplot(1,4,1)

plt.scatter(x,y)

plt.title('Chart 1')

#plot 2

x=np.array([0, 1, 2, 3])

y=np.array([3,8,0.5, 10])

plt.subplot(1,4,2)

plt.plot(x,y)

x=np.array([0, 2, 4, 3])

y=np.array([6,2, 7, 12])

plt.plot(x,y, c='red')

plt.title('Chart 2')

#plot 3

x=np.array(['A', 'B', 'C', 'D'])

y=np.array([3,7,8, 10])

plt.subplot(1,4,3)

plt.bar(x,y)

plt.title('Chart 3')

#plot 4

x=np.array([50, 90, 95,100, 105, 110, 112,115, 120, 125])

y=np.array([240, 253, 261, 270, 280,295, 305, 310, 322, 340])

plt.subplot(1,4,4)

plt.plot(x,y)

plt.title('Chart 4')

 

plt.show()


# In[ ]:




