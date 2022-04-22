# 打印输出长方形

print('长方形') 
h = int(input('宽：')) 
w = int(input('长：'))

for _ in range(h):
    for _ in range(w):
        print('*', end='')
    print()
