#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
integers = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
integers *2
integers.ndim


# In[2]:


integers.shape


# In[3]:


for row in integers:
    for column in row:
        print(column, end= ' ')
    print()
for i in integers.flat:
    print(i, end= ' ')


# In[4]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,6])
ypoints = np.array ([5,10])
plt.plot(xpoints, ypoints)
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3,6,9,12])
ypoints = np.array ([2,8,1,10])

plt.plot(xpoints, ypoints, marker = 'o')
plt.show()


# In[6]:


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array ([2,4,6,14,10,12])

plt.plot(ypoints,  's:r', ms = 10, mec = 'g', mfc = 'g')
plt.show()


# In[ ]:




