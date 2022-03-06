a = eval(input('请输入成绩:'))
if a <0 or a>100 or a%1!=0:
    print('你输入的成绩不合理,请检查后重新输入')
elif 90<=a<=100:
    print('成绩等级:A')
elif 80<=a<=89:
    print('成绩等级:B')
elif 70<=a<=79:
    print('成绩等级:C')
elif 60<=a<=69:
    print('成绩等级:D')
else:
    print('成绩等级:E')
