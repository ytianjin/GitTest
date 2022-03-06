import random as r

class Fish:
        def move(self):
            self.x = r.randint(0, 10)
            self.y = r.randint(0, 10)
            self.x -= 1
            print('我的位置是:', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def _init_(self):
        super()._init_()
    

    def eat(self):
        self.hungry = True
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")

        else:
            self.hungry = False
            print("太饱了吃不了")

shark = Shark()
shark.eat()
fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move() 