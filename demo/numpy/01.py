import numpy as np

arr = np.array(61)

arr = np.array([1, 2, 3, 4, 5, 6])

arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim) # 检查数组有多少维：ndim            on=true&page=1&pageSize=15&productName=&conditionType=1&applyname=&applysn=
# print(b.ndim)         c6fe0e0c374448128149352fc8aca2a3
# print(c.ndim) 
# print(d.ndim)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print(arr[1, 0, 2])
print(arr[1, 1, 2])