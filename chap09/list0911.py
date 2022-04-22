# 程序接收实参时形参就是实参本身。请通过该程序对此进行确认。

def func(n): 
    """输出形参的值和标识值""" 
    print('n：', n, id(n))
    n = 0
    print('n：', n, id(n))

x = 5
print('x：', x, id(x))
func(x)
print('x：', x, id(x))
