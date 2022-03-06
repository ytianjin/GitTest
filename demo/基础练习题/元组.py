x = ("apple", "banana", "cherry")
y = list(x)
print(y)
y[1] = "kiwi"
x = tuple(y)
print(x)
# tuple  元组

# 元组方法
# Python 提供两个可以在元组上使用的内建方法
# 方法	        描述
# count()	返回元组中指定值出现的次数。
# index()	在元组中搜索指定的值并返回它被找到的位置。