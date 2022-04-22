# 进行乘法运算和除法运算的程序（异常处理：其一）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b 等于', a * b, '。')
    print('a / b 等于', a / b, '。')

except ValueError:
    print('无法识别为整数！')
    
except ZeroDivisionError:
    print('除数为0的运算！')
    
else:
    print('正常结束！')

finally:
    print('您辛苦了。')