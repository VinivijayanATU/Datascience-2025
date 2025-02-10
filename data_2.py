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
