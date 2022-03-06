def tine(name):
    with open(name) as f:
        f = f.read()
        file = f.split()
        list1 = list(map(float, file))
        list2 = list1[0:117:3]
        list3 = list1[1:117:3]
        list4 = list1[2:118:3]
        result = 0
        for i in range(len(list2)):
            rea = list2[i] * list3[i] * list4[i]
            result +=rea
        print(result)

tine('01.txt')
tine('02.txt')