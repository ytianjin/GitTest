# j = 1
# while j<=9:
#     i =1
#     while i<=j:
#         print(f'{i} * {j} = {i*j}', end='\t')
#         i +=1
#     print()
#     j +=1
# 使用 extend() 方法将 list2 添加到 list1 的末尾：



from itertools import count


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)

# clear() 方法清空列表：

thislist = ["apple", "banana", "cherry"]
thislist.clear()

# del 关键字删除指定的索引：

thislist = ["apple", "banana", "cherry"]
del thislist[0]

# pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：

thislist = ["apple", "banana", "cherry"]
thislist.pop()

# 要在指定的索引处添加项目，请使用 insert() 方法：插入项目作为第二个位置：

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")


# 使用 list() 构造函数创建列表：

thislist = list(("apple", "banana", "cherry")) # 请注意双括号       
# print(thislist)


# 方法	描述
# append()	在列表的末尾添加一个元素
# clear()	删除列表中的所有元素
# copy()	返回列表的副本
# count()	返回具有指定值的元素数量。
# extend()	将列表元素（或任何可迭代的元素）添加到当前列表的末尾
# index()	返回具有指定值的第一个元素的索引
# insert()	在指定位置添加元素
# pop()	删除指定位置的元素
# remove()	删除具有指定值的项目
# reverse()	颠倒列表的顺序
# sort()	对列表进行排序