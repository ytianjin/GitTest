# with open('01.txt') as f:
#     listt2 = f.readlines()
#     # list1 = listt2.split()
#     # listt1 = list(map(float,list1))
#     # print(listt2)
def func():
    print('我是func函数')   # 等二步打印:我是func函数
    value = (11,22,33,44)   # 等三步打印:11,22,33,44
    return value

def outer(fun):       # 这里给予一个a的形参也是:func = outer(func)传递func的函数进去
    # print("before")     # 等一步打印:before
    def inner():
        print("before") 
        res = fun()   # 这里相当于是调用了func的函数
        print("after")
        return res
        
    return inner

func = outer(func)

result = func()
print(result)

# def func():
#     print("before")
#     print('我是func函数')
#     value = (11,22,33,44)
#     print('after')
#     return value