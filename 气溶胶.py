#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[36]:


# data1=pd.read_csv('C:/Users/Administrator/Desktop/老师/DATA1.csv')
data1_dir=''
data1=pd.read_csv(data1_dir)
data1.head()


# In[44]:


AOT440=data1.ix[:,'AOT440']
AOT500=data1.ix[:,'AOT500']
AOT675=data1.ix[:,'AOT675']
AOT870=data1.ix[:,'AOT870']
AOT936=data1.ix[:,'AOT936']
print(len(AOT440))


# In[38]:


from scipy import interpolate
AOT550=[]
for i in range(len(AOT440)):
    x=[440,500,675,870,936]
    y=[AOT440[i],AOT500[i],AOT675[i],AOT870[i],AOT936[i]]
    f=interpolate.interp1d(x,y,kind='linear')
    AOT550_value=f(550)
#     print(AOT550_value)
    AOT550.append(AOT550_value)


# In[39]:


data1['AOT550']=AOT550


# In[40]:


data1.head()


# In[41]:


import math
ln50=math.log(50)
VIS=[]
for i in range(len(AOT440)):
    VIS_value=ln50/(AOT550[i]+0.01159)
    VIS.append(VIS_value)


# In[42]:


data1['VIS']=VIS
data1.head()


# In[43]:


data1.to_csv('C:\\Users\\Administrator\\Desktop\\data1.csv')


# In[ ]:




