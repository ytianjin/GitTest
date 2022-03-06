def sum_number(num):                    # 3 +2 +1 =6
    #2: 出口
    if num == 1:
        return 1
   #1: 当前数字 +  当前数字 -1的累加        递归的特点:当前数字-1的累加和,必须要有出口
    return num + sum_number(num-1)        # 函数内部自己调用自己

result = sum_number(6)
print(result)

"""
基本的路程就是:6 = 3+2以内数字累加      等一步num(3) + sum_number(num3-1)2
2以内数字累加:2+1以内数字累加           等二步函数内部自己调用自己,num(sum_number(num3-1)2) + sum_number(2-1)1
1以内数字累加:1=出口                    等三步函数内部自己调用自己,sum_number(2-1),if num == 1:return 1.结果1=出口 
"""