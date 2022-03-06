def outer(func):  #(1)
    def inner():    #(4)
        # a = '1,2,3'   
        print('0,0,0')  #（6）
        r = func()      #（8）
        print('4,5,6')  #（10 ）
        return r        #（9）
    return inner()  #(5)

@outer              # (2)
def f1():           #(3)
    print('1,2,3')  #（7）