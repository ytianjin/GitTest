# 让列表所有元素的值变为原来的 2 倍（函数）

def double(n):
    return 2 * n

x = [1, 2, 3, 4]
y = map(double, x)

print(list(y))
