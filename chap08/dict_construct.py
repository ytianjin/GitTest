# 字典的生成

dict01 = {}                     # {}    空字典
dict02 = {'China': 156, 'Japan': 392, 'France': 250}

dict03 = dict()                 # {}    空字典

lst = [('China', 156), ('Japan', 392), ('France', 250)]
dict04 = dict(lst)

key = ['China', 'Japan', 'France']
value = [156, 392, 250]
dict05 = dict(zip(key, value))

print('dict01 =', dict01)
print('dict02 =', dict02)
print('dict03 =', dict03)
print('dict04 =', dict04)
print('dict05 =', dict05)
