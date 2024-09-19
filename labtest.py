#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np
heart_rate_data=np.linspace(80,150,1440)
for i in heart_rate_data:
    print(i)


# In[67]:


from scipy import signal as sg
def avgheart(heart_rate_data):
    hourly_avg=[]
    i=0
    for x in range(24):
        
        sum=0
        for y in range(60) :
            sum=sum+heart_rate_data[i]
            i=i+1
        hourly_avg.append(sum/60)
            
    return hourly_avg
        


# In[68]:


Y=avgheart(heart_rate_data)
for i in Y:
    print(i)


# In[69]:


import matplotlib.pyplot as plt
X=np.linspace(0,100,1440)
plt.plot(X,heart_rate_data)
plt.show()


# In[72]:


EXCEED_100=[]
def exceed100(heart_rate_data):
    for i in range(1440):
        boolean=1
        if(i<1420):
            for j in range(i,i+20):
                if heart_rate_data[j]<100:
                    boolean=0
                    break
            if boolean:
                EXCEED_100.append((i))
                
        
        
    


# In[75]:


exceed100(heart_rate_data)


# In[ ]:





# In[ ]:




