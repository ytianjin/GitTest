# 第４章 总结

while True: 
    n = int(input('0～100的整数：')) 
    if 0 <= n <= 100: 
        break 

c = n 

# 打印输出c个'*'
while n > 0: 
    print('*', end='') 
    n -= 1 
print() 

# 循环输出'1234567890'（总共c个字符） 
for i in range(1, c + 1): 
    print(i % 10, end='') 
print('\n') 

# 列举面积为s且长和宽度都是整数的长方形边长
s = int(input('面积：')) 
print('面积为{}且长和宽度都是整数的' 
        '长方形边长'.format(s)) 
for i in range(1, s + 1): 
    if i * i > s: break 
    if s % i: continue 
    print('{}×{}'.format(i, s // i)) 
print() 

# 每输出w个'*'换一次行，总共输出n个'*'
n = int(input('一共输出多少个：')) 
w = int(input('每输出多少个换一次行：')) 
for i in range(1, n + 1): 
    print('*', end='') 
    if i % w == 0: 
        print() 
if n % w != 1: 
    print() 
print() 

# 数字长方形 
h = int(input('宽：')) 
w = int(input('长：')) 
for i in range(1, h + 1): 
    for j in range(1, w + 1): 
        print((i + j - 1) % 10, end='') 
    print() 
