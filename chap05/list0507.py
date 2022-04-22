# 打印输出位的逻辑与运算的结果、逻辑或运算的结果、逻辑异或运算的结果以及取反的结果

a = int(input('正整数a：')) 
b = int(input('正整数b：')) 
w = int(input('表示位数：')) 

f = '{{:0{}b}}'.format(w) 
m = 2 ** w - 1       # w位都相当于二进制数的1

print('a = ' + f.format(a)) 
print('b = ' + f.format(b)) 
print('a & b = ' + f.format(a & b)) 
print('a | b = ' + f.format(a | b)) 
print('a ^ b = ' + f.format(a ^ b)) 
print('~a = ' + f.format(~a & m)) 
print('~b = ' + f.format(~b & m))