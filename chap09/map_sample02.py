# map的应用实例（其二：将所有元素的计量单位从厘米转换为英寸）

x = [1, 2, 3, 4]

print(list(map(lambda n: 2.54 * n , x)))
