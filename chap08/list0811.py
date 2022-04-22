# 取出字典的所有键、所有值以及所有元素

rgb = {'red': '赤', 'green': '绿', 'blue': '蓝'} 

print('键：', list(rgb.keys()))    # 将键的视图转换为列表
print('值 ：', list(rgb.values())) # 将值的视图转换为列表
print('元素：', list(rgb.items())) # 将(键, 值)的视图转换为列表