class Ball:
    def setname(self, name):
        self.name = name
    def kick(self):
        print("我叫%s, 该死的,谁踢我...." % self.name)


a = Ball()
a.setname('球A')
b = Ball()
b.setname('球B')
c = Ball()
c.setname('土豆')
a.kick()
b.kick()
c.kick()