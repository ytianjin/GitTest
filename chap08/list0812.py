# 获取的视图被转换为列表后，我们可使用整数型索引访问其中的元素

item = list({'red': '赤', 'green': '绿', 'blue': '蓝'}.items()) 

print('item[0]    = ', item[0])
print('item[1]    = ', item[1])
print('item[2]    = ', item[2])

print('item[0][0] = ', item[0][0])
print('item[0][1] = ', item[0][1])
print('item[1][0] = ', item[1][0])
print('item[1][1] = ', item[1][1])
print('item[2][0] = ', item[2][0])
print('item[2][1] = ', item[2][1])
