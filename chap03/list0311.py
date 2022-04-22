# 判断整数的位数（0、一位数或多位数） 

n = int(input('整数：')) 

if n == 0:                   # 0
    print('该值为零。')  
elif n >= -9 and n <= 9:     # 一位数 
    print('该值为一位数。')  
else:                        # 多位数 
    print('该值为多位数。') 
