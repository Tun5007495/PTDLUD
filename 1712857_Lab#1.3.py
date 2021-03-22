#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cau1
import pandas as pd
data={
    "numbers":['#23','#24','#18','#14','#12','#10','#35'],
    "nums":[23,24,18,14,"NA","XYZ",35],
    "colors":["green","red","yellow","orange","purple","blue","pink"],
    "other_column":[0,1,0,2,1,0,2]
}
df=pd.DataFrame(data)
print(df)


# In[2]:


#cau2
df.dtypes


# In[3]:


#cau3
#luu gia tri cua cot numbers vao bien temp
temp=df['numbers']
#tao mot mang y de luu nhung gia tri tinh
y=[]
#loai bo dau '#'
for x in temp:
    #ep kieu
    x=int(x.replace("#",""))
    y.append(x)
#tinh mean
from statistics import mean
mean(y)


# In[8]:


#cau4
for x in df["colors"]:
    x=x.capitalize()
print(df)


# In[17]:


#cau5
#Dua tren df hien co
#Ta thay gia tri cot nums tuong tu voi cot numbers
#Thay doi missing data tu du lieu cot numbers
for x in df.index:
    if type(df.loc[x,"nums"])!=int:
        #Thay the dau '#', ep kieu
        temp=int((df.loc[x,"numbers"]).replace("#",""))
        df.loc[x,"nums"]=temp
print(df)

