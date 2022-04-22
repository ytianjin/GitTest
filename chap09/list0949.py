# 让列表所有元素的值变为原来的 2 倍（lambda 表达式）

x = [1, 2, 3, 4]
y = map(lambda n: 2 * n, x)

print(list(y))
