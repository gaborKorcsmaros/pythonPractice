class car:
    def __init__(self, wheels = 4, doors = 5):
        self.wheels = wheels
        self.doors = doors
        self.engine = "off"
    def start(self):
        self.engine = "on"

class bus(car):
    pass

x = car()
print(x.engine)
x.start()
print(x.engine)

y = bus(8,1)
print(y.engine)
y.start()
print(y.engine)