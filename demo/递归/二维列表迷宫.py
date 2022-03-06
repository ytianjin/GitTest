import random
# 创建迷宫
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,0,1,1,1],
    [1,0,1,1,1,1,0,0,1,1],
    [1,0,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,1,1,1],
    [1,0,0,0,1,1,1,1,1,1],
    [1,1,1,0,0,0,0,1,1,1],
    [1,1,1,0,0,1,0,1,1,1],
    [1,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

# 设置起点
start = (1, 1)
# 设置终点
end = (8, 8)

# 判断当前这个数,上下左右是0还是1,如果是0就可以
lst = [start]
while lst:
    now = lst[-1]
    if now == end:
        print("终于走出来了")
        print(lst)
        break
    row, col = now
    maze[row][col] = 2
    if maze[row-1][col] == 0: # 上
        lst.append((row-1, col))
        continue
    elif maze[row][col+1] == 0:  # 右
        lst.append((row, col+1))
        continue
    elif maze[row+1][col] == 0:  # 左
        lst.append((row+1, col))
        continue
    elif maze[row][col-1] == 0:
        lst.append((row+1, col-1))        
    else:
        lst.pop()

else:
    print("此路不通")