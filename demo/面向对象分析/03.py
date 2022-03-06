class Bass:

    def __init__(self):
        self.func()

    def func(self):
        print('in base')

class Son(Bass):
    def __init__(self):
        super().__init__()
        self.func = 200

    func = 100
    def func(self):
        print('in son')

s = Son()