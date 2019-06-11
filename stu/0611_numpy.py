import numpy as np


print("用numpy生成的二维数组arr1和arr2")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[2, 2, 2], [9, 9, 9]])

print("输出numpy生成的二维数组")
print(arr1, '\n')

# 标量与数组计算
print("输出numpy生成的二维数组与标量计算arr*2结果")
print(arr1 * 2, '\n')

# 数组与数组计算
print("输出numpy生成的二维数组与数组arr1+arr2计算结果")
print(arr1+arr2, '\n')

#数组间比较
print("输出numpy生成的二维数组与数组比较arr1 > arr2结果（布尔值数组）：")
print(arr1 > arr2, '\n')

#数组切片
print("数组切片后是一个降低纬度的数组")
print('arr1[0] = ', arr1[0],'\n')

print("取出某个值")
print('arr1[0][0] = ', arr1[0][0])
print('arr1[0, 0] = ', arr1[0, 0],'\n')

#数组的转置
print("arr1为：", '\n', arr1)
print("数组转置arr1.T")
print(arr1.T)

#数组的换轴
arr = np.arange(15)
arr_shape = arr.reshape((3, 5))

print("数组arr = ", arr, '\n')

print('arr.reshape((3，5) 结果：','\n',arr_shape, '\n')

#一元通用函数
arr3 = np.arange(12).reshape((3, 4))
arr4 = np.square(arr3)
print("原始数组arr3：\n",arr3, '\n\n',"np.square(arr3)：\n",  arr4)

