# 强制使用关键字参数

def puts(*, n, s): 
    """连续打印输出n个s""" 
    for _ in range(n):
        print(s, end='')

puts(n = 3, s = '*')
print()
puts(s = '+', n = 7)
print()
puts(3, '*')    # 程序错误
