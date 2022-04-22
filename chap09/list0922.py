# 打印输出字典化的关键字参数的信息

def print_kwargs(s, **kwargs): 
    """将字典化的关键字参数传递给kwargs后，程序打印输出kwargs的信息""" 
    print(s) 
    print('type(kwargs) =', type(kwargs)) 
    print('len(kwargs) =', len(kwargs)) 
    print('kwqrgs =', kwargs) 

print_kwargs('第一次调用', spring='春', summer='夏') 
print() 
print_kwargs('第二次调用', spring='春')