# 按照升序排列四个数值（sroted函数）

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
d = int(input('整数d：'))

a, b, c, d = sorted([a, b, c, d])     # 按照升序排列四个数值

print('按照a≦b≦c≦d进行排序。')
print('变量a的值是', a, '。') 
print('变量b的值是', b, '。')
print('变量c的值是', c, '。')
print('变量d的值是', d, '。')
