"""
设计一个猜数游戏,首先由计算机产生一个[1,100]之间的随机整数,然后由用户猜测所产生的随机数。根据用户猜测的情况给出不同提示,
如猜测的数大于产生的数,则显示“High”,小于则显示LoW”,等于则显示“ You won!”,游戏结束。用户最多可以猜7次,如果7次均未猜中,
则显示“ You lost!”,并给出正确答案,游戏结束。游戏结束后,询问用户是否继续游戏,选择“Y”则开始轮新的猜数游戏;选择“N”则退出游戏
"""
chose = 'y'
while chose == 'y':
    import random
    num = random.randint(1, 100)
    def judge(b):
        if b == num:
            return 1
        else:
            return 0
    for i in range(1, 8):
        b = eval(input('请输入您第{}次猜的整数: '.format(i)))
        if judge(b) == 1:
            print("You won!")
        elif b > num:
            print("high")
        elif b < num:
            print("low")
        if judge(b) == 0:
            print("You lost")
            chose = input('请输入Y(y)继续进行游戏, N(n)出游戏:')
            while chose != 'Y' and chose != 'y' and chose !='N' and chose != 'n':
                print('输入有误,请新输入Y(y)继续进行游戏, N(n)退出游戏:',end = '')
                chose = input()