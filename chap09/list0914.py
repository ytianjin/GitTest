# 使用敬称打招呼的函数（带默认值的形参）

def hello(name, honorific = '老师'): 
    """使用敬称打招呼""" 
    print('你好，{}{}。'.format(name, honorific)) 
    
hello('田中') 
hello('关根', '先生') 
hello('西田', '女士') 