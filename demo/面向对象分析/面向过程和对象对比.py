# 面向过程和面向对象的对比
# 面向过程  [一辆汽车,车速60/h, AB的距离100km,求时间.]
speed = 60
distance = 100
time = distance / speed
print(time)

#面向对象  [一辆汽车,车速60/h, AB的距离100km,求时间.]
class Car:  #[创建类]
    speed = 0   #[类的变量]
    def drive(self, distance):  #[类的的方法drive]
        time = distance / self. speed
        print(time)

car = Car()     #[对象]
car.speed = 60      #[改变类的变量]
car.drive(100)      #[调用类的的方法drive,并且给予一个值]
