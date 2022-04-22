# 打印输出读取的整数符号（跳过0） 

n = int(input('整数：')) 

if n > 0: 
    print('该值为正数。') 
elif n == 0: 
    pass
else: 
    print('该值为负数。')
