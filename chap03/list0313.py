# 判断读取的整数是否为多位数（其二） 

n = int(input('整数：')) 

if not (n <= -10 or n >= 10):             # 非多位数  
    print('该值不是多位数。') 
else:                                     # 多位数 
    print('该值为多位数。') 
