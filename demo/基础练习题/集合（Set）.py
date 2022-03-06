thisset = {"apple", "banana", "cherry"}     #检查 set 中是否存在 “banana”：存在是: True  不存在是: False
print("banana" in thisset)

# 要将一个项添加到集合，请使用 add() 方法。
# 要向集合中添加多个项目，请使用 update() 方法。

# 使用 add() 方法向 set 添加项目：

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
# print(thisset)

# 使用 update() 方法将多个项添加到集合中：

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])

# union() 方法返回一个新集合，其中包含两个集合中的所有项目：

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

# update() 方法将 set2 中的项目插入 set1 中：注释：union() 和 update() 都将排除任何重复项。

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)

# 使用 set() 构造函数来创建集合：

thisset = set(("apple", "banana", "cherry")) # 请留意这个双括号
print(thisset)