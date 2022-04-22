# 开启驻留机制后判断字符串的同一性

import sys

s1 = input('字符串s1：')
s2 = input('字符串s2：')

str1 = sys.intern(s1)
str2 = sys.intern(s2)

print('str1 is     str2 =', str(str1 is str2))
print('str1 is not str2 =', str(str1 is not str2))
