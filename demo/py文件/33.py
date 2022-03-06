listt1 = []
list5 = []
with open('01.txt') as f:
    listt2 = f.read()
    list1 = listt2.split()
    # for list in list1:
        # listt1.append(float(list))
    listt1 = list(map(float, list1))
    # for list in listt1:
    #     if list >1 and list <2:
    #         print(list)
   # print(listt1)
    list2 = listt1[0:41:3]
    print(list2)
    list3 = listt1[1:41:3]
    print(list3)
    list4 = listt1[2:42:3]
    print(list4)
    result = 0
    for i in range(len(list2)):
        rest = list2[i] * list3[i] * list4[i]
        result +=rest
    print(result)
# [1.375, 0.55, 96.0, 1.375, 0.04, 96.0, 0.55, 0.04, 96.0, 1.375, 0.035, 96.0, 0.55, 0.035, 96.0, 1.375, 0.55, 80.0, 1.375, 0.04, 80.0, 0.55, 0.04, 80.0, 1.375, 0.035, 80.0, 0.55, 0.035, 80.0, 1.225, 0.55, 48.0, 1.225, 0.04, 48.0, 0.55, 0.04, 48.0, 1.225, 0.035, 48.0]