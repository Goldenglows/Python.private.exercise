import pandas as pd
import numpy as np

var = {'one':[1,4,7],'two':[2,5,8],'three':[3,6,9]}

var1 = pd.DataFrame(var,index = ['a','b','c'])

var1['two']
var1['three']

var1.iloc[0]
var1.iloc[2]
var1.iloc[:,0]
var1[0]
var1.iloc[:,2]
var1[2]

#筛选
data1 = var1.loc[var1['one']>2,['one']]

#添加列
data1['four']=[10,10,10]

for x in data1.index:
    if data1.loc[x]>9:
        data1.loc[x]=8.


#删除
data1.drop(labels=[0,1],axis= 'a')