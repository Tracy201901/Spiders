
import pandas as pd

# 生成一个数组
arr1d = pd.Series([1, 2, 3])  # 默认索引
arr2d = pd.Series([[1, 2, 3],[4, 5, 6]], index=['first', 'second'])  #自定义索引


print('******arr1d*********')
print( arr1d,'\n')

print('******arr2d*********')
print(arr2d,'\n')

#数组的切片
print(arr1d[0])
print(arr2d[0])
print(arr2d[0][0])
print(arr2d['first'])

print('\n将字典转化成Series')
dict = {'apple':5, 'banana':3.5, 'watermelon':6}
obj3 = pd.Series(dict)
print(obj3)


