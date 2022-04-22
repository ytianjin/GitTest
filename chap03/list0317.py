# 根据读取的月份输出季节（其二：编写多行代码判断该月份是否属于冬天） 

month = int(input('查询季节。\n月份：')) 

if 3 <= month and month <= 5: 
    print('该月份属于春天。')  
elif 6 <= month and month <= 8: 
    print('该月份属于夏天。')  
elif 9 <= month and month <= 11: 
    print('该月份属于秋天。')  
elif (month == 1 or # 1月份属于冬天  
      month == 2 or # 2月份也属于冬天 
      month == 12   # 12月份也属于冬天 
     ): 
    print('该月份属于冬天。')  
else: 
    print('该月份不存在。')