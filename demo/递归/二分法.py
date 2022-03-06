# 二分法是一个查找算法
# 要求:数据必须是有序序列
# 核心思想:掐头结尾取中间

#      left           mid               right
#       0  1   2   3   4   5   6    7   8 
lst = [12, 13, 14, 15, 16, 17, 18, 19, 20, ]
n = int(input("请输入您要找的数据"))
# 最low的查找算法
# for item in lst:
#     if n == item:
#         print("找到了")
#         break

# 高级的算法:二分法查找
left = 0
right = len(lst) - 1

while left <= right:
    mid = (left + right) // 2

    if n > lst[mid]:
        left = mid + 1
    elif n < lst[mid]:
        right = mid - 1
    else:
        print("我找到了这个数,它就在%s位置" % mid)
        break

else:
    print("没有这个数")