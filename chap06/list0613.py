# 搜索字符串中包含的字符串

txt = input('字符串txt：') 
ptn = input('字符串ptn：') 

try: 
    print('ptn包含于txt[{}]。'.format(txt.index(ptn))) 
except ValueError: 
    print('ptn不在txt内。') 
