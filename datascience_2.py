# -*- coding: utf-8 -*-
"""Datascience_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nKXPsvFB64p2dqixAsbwEaDqEYPqahXa
"""

#Series Object attribute:
import pandas as pd
x = pd.Series([1,2,3, None],index = ['a','b','c','d'])
# It returns a tuple of shape of the data.
print("Shape:",x.shape)
# It returns the size of the data.
print("Size:",x.size)
# Defines the index of the Series.
print("Index:",x.index)
# It returns the number of dimensions in the data.
print("Dimension:",x.ndim)
# It returns the values of series as list
print("values:",x.values)

#Series Object attribute (cont.)
# It returns the data type of the data.
print("Data Type:",x.dtype)
# It returns the number of bytes in the data
print("Bytes:",x.nbytes)
# It returns True if Series object is empty, otherwise returns false.
print("is empty:",x.empty)
#It returns True if there are any NaN values, otherwise returns false.
print("is empty:",x.hasnans)

#Pandas Operations
#map()
import pandas as pd
import numpy as np
a = pd.Series(['Java', 'C', 'C++', np.nan])
b = a.map({'Java':'Core',"C++":'Python'})
print(a)
print(b)

#std()
import numpy as np
x = pd.Series([1,2,3,4,5,None])
print("Std=",np.std(x))
#print("Series:",np.std([1,2,3,4,5]))

#count()
import pandas as pd
import numpy as np
x = pd.Series([2, 1, 1, np.nan, 3,4,5,5])
print(x.count())

#Pandas Operations
#filter()
import numpy as np
import pandas as pd
arr=np.array(([20,30,40],[50,70,80]))
df=pd.DataFrame(arr,index=["V","X"],columns= ["Physics","Chemistry","Maths"])
print(df)
#print(df.filter(items=["Physics"]))

print(df.filter(items=["Maths"]))

#Creating DataFrame
# importing the pandas library
import pandas as pd
#empty DataFrame
df = pd.DataFrame()
print (df)

# Using List
list=["Rays","Tech","Os"]
print(list)
df = pd.DataFrame(list)
df_1 = pd.DataFrame(list,index=["V","X",'Y'],columns= ["subject"])
print(df)
print(df_1)

# using Dict
info = {'ID' :[101, 102, 103],'Department':['B.Sc','B.Tech','M.sc',]}
#df_2 = pd.DataFrame(info)
df_3 = pd.DataFrame(info, index=["student1","student2",'student3'],columns= ["Grade", "Course"])
#print(info)
#print('df_2=',df_2)
print('df_3=',df_3)

#Creating DataFrame
#Using Dict of series
info = {'one' : pd.Series([1, 2, 3, 4, 5, 6],
                          index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two' : pd.Series([1, 2, 3, 4, 5, 6, 7, 8],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g','h'])}
d1 = pd.DataFrame(info)
print(d1)

#Column Selection from a DataFrame:
from pandas import DataFrame,Series
x={'Id':Series([1,2,3,4,5]), "Name":Series(["A","B","C","D","E"])}
df=DataFrame(x)
print(df)

print('id=', df['Id'])
print('Name=', df["Name"])

#Column Addition and Deletion to DataFrame
from pandas import DataFrame,Series
x={'Id':Series([1,2,3,4,5]),
   "Name":Series(["A","B","C","D","E"])}
df=DataFrame(x)
print(df)

# ADD a Column from DataFrame
df['Subject']=pd.Series(["C","C++","Java","python","Java"])
print(df)

# Delete a Column from DataFrame
del df["Id"] #Using del function
print(df)

df.pop("Name") # Delete a Column from DataFrame Using pop function
print(df)