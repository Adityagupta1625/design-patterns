class Movable:
    def getSpeed(self):
        pass

class BMW(Movable):
    def getSpeed(self):
        return 256

class MovableAdapter:
    def __init__(self,luxury_cars):
        self.luxury_cars=luxury_cars

    def getSpeed(self):
        return self.luxury_cars.getSpeed()*1.690

bmw=BMW()
bmwAdapter=MovableAdapter(bmw)
print(bmwAdapter.getSpeed())

# https://medium.com/@akshatsharma0610/adapter-design-pattern-in-java-fa20d6df25b8

# https://medium.com/coding-becomes-easy/adapter-pattern-6174c34ec970