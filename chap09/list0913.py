# 反转列表中元素的排列顺序

def reverse_list(lst): 
    """反转lst的元素排列顺序""" 
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

x = [22, 57, 11, 32, 91, 68, 77]
print('x =', x)

reverse_list(x)
print('x =', x)
