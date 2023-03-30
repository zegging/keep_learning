# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: pandas_test
@file: quick_start.py
@time: 2023/3/29 21:06
"""
import numpy as np
import pandas as pd

r = [1, 2, 3, 4, 5, 6, 7]
ser = pd.Series(r)
print(r)
print(ser)
ser.iloc[0] = 999
print(r)
print(ser)

print('----------------------------------------------------')

r = [1, 2, 3, 4, 5, 6, 7]
ser = pd.Series(r)
print(r)
print(ser)
ser.iloc[0] = 999
print(r)
print(ser)

print('----------------------------------------------------')

r = [0, 1, 2, 3, 4, 5, 6, 7]
ser = pd.Series(r)
print(ser.iloc[[0,3]])
print(ser.iloc[:3])
print(ser.iloc[lambda x: x.index % 2 == 0])

print('----------------------------------------------------')

r = [0, 1, 2, 3, 4, 5, 6, 7]
ser = pd.Series(r, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# 注意Series对象只有一列数据，因此无法选择列。.iloc方法用于选择Series对象中的某些行。
# 使用ser.loc时，可以指定一个标签或一组标签来选择数据。
print(ser.loc[['a', 'b', 'c']])

print('----------------------------------------------------')

mydict = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 100, 'b': 200, 'c': 300, 'd': 400},
    {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000},
]
df = pd.DataFrame(mydict)
# print(df)
#       a     b     c     d
# 0     1     2     3     4
# 1   100   200   300   400
# 2  1000  2000  3000  4000
print(df.iloc[1,2])
print(type(df.iloc[1]))

print('----------------------------------------------------')

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})

print(df1)
print(df2)

df3 = df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right'))
print(df3)
#   lkey  value_x rkey  value_y
# 0  foo        1  foo        5
# 1  foo        1  foo        8
# 2  foo        5  foo        5
# 3  foo        5  foo        8
# 4  bar        2  bar        6
# 5  baz        3  baz        7
# df4 = df1.merge(df2, right_on='rkey')
# print(df4)

print('----------------------------------------------------')

df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['foo', 'bar', 'qux'], 'value': [5, 6, 7]})
# 交集
merged_inner = pd.merge(df1, df2, on='key')
print(merged_inner)
# 左DataFtame的基础上并，补Nan
merged_left = pd.merge(df1, df2, on='key', how='left')
print(merged_left)

print('----------------------------------------------------')

ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])

print(pd.concat([ser1, ser2]))
print(pd.concat([ser1, ser2], axis=1))

print(pd.concat([ser1, ser2]).__class__)
print(pd.concat([ser1, ser2], axis=1).__class__)
# <class 'pandas.core.series.Series'>
# <class 'pandas.core.frame.DataFrame'>

print('----------------------------------------------------')

df = pd.concat([ser1, ser2], axis=1)
print(df)
print('--------')
print(pd.concat([ser1, df], axis=1, join='inner'))
print('--------')
print(pd.concat([ser1, ser2], axis=1, keys=[1,2]))

print('----------------------------------------------------')

dframe = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white', 'black', 'red'],
                      columns=['ball', 'pen', 'pencil'])
print(dframe)
print('------------')
ser = dframe.stack()
print(ser)
dframe_after = ser.unstack()
print(dframe_after)

