# 基于format方法进指定各种格式

print('{:5d}'.format(1234567))
print('{:7d}'.format(1234567))
print('{:9d}'.format(1234567))
print('{:,}'.format(1234567))
print()
print('{:b}'.format(1234567))
print('{0:o} {0:#o}'.format(1234567))
print('{0:x} {0:#X}'.format(1234567))
print()
print('{:%}'.format(35 / 100))
print()
print('{:e}'.format(3.14))
print('{:f}'.format(3.14))
print('{:g}'.format(3.14))
print()
print('{:.7f}'.format(3.14))
print('{:12f}'.format(3.14))
print('{:12.7f}'.format(3.14))
print()
print('{:.0f}'.format(3.0))
print('{:#.0f}'.format(3.0))