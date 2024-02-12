#!/usr/bin/env python
# coding: utf-8

# # Merge

# In[1]:


import pandas as pd


# In[18]:


var1 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4,5] , "C":[21,22,23,24,25]})
pd.merge(var1,var2,)


# In[19]:


pd.merge(var1,var2,on = "A")


# In[28]:


var3 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
var4 = pd.DataFrame({"A":[1,2,3,4,6] , "C":[21,22,23,24,25]})
pd.merge(var3,var4)


# In[29]:


pd.merge(var3,var4,on = "A")


# In[30]:


pd.merge(var3,var4, how = "left")


# In[31]:


pd.merge(var3,var4, how = "right")


# In[32]:


pd.merge(var3,var4, how = "outer")


# In[33]:


pd.merge(var3,var4, how = "outer" , indicator = True)


# In[35]:


var5 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
var6 = pd.DataFrame({"A":[1,2,3,4,6] , "B":[21,22,23,24,25]})
pd.merge(var5,var6 , left_index = True , right_index = True)


# In[39]:


#To change a name of COLUMN then we use "suffixes"


# In[41]:


pd.merge(var5,var6 , left_index = True , right_index = True , suffixes = ("_ID" , "_NAME"))


# # Concat

# In[45]:


import pandas as pd


# In[47]:


Series1 = pd.Series([1,2,3,4,5])
Series2 = pd.Series([6,7,8,9,10])
pd.concat([Series1,Series2])


# In[49]:


df1 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
df2 = pd.DataFrame({"A":[1,2,3,4,6] , "B":[21,22,23,24,25]})
pd.concat([df1,df2])


# In[51]:


pd.concat([df1,df2],axis = 1)


# In[60]:


df3 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
df4 = pd.DataFrame({"A":[1,2,3,4,6] , "B":[21,22,23,24,25]})
pd.concat([df3,df4], axis =1)


# In[ ]:





# In[ ]:





# # 08.02.2024 

# In[4]:


import pandas as pd
import numpy as np


# In[6]:


def add(num1,num2):
    sum = num1  * num2
    print(sum)
    
add(5,6)


# In[13]:


range(5)[3]


# In[16]:


Starvalue = range(5)[3]
print("The frst element in range is = " , Starvalue)


# In[22]:


for i in range(3,10,2):
    print(i)


# In[35]:


for i in range(3,10,2):
    print(type(i))


# In[40]:


for i in range(3,10,2):
    print(list(range(5)))


# In[42]:


#Range works for "String" only


# In[47]:


print(ord('A'))


# In[56]:


#generator function
def get_alphabets(Startletter,Stopletter,Step):
    for c in range(ord(Startletter.lower()),ord(Stopletter.lower()),Step):
        yield chr(c)
    
print(list(get_alphabets("A" , "H" , 1)))


# In[57]:


#user defined function
def alphabets(letter1,letter2):
    print(letter1)
    print(letter2)
    
alphabets("a","b")


# In[ ]:




