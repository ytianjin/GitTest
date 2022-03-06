import random

naes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
offsic = [[], [], []]
for nae in naes:
    name = random.randint(0, 2)
    offsic[name].append(nae)
print(offsic)