
class Component:
    def showPrice():
        pass

class Leaf(Component):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def showPrice(self):
        return f'This item {self.name} has price {self.price}'

class Composite(Component):
    def __init__(self,name):
        self.name=name
        self.components=[]
    
    def showPrice(self):
        for c in self.components:
            if c is None or c.showPrice() is None:
                continue
            else:
                print(c.showPrice())
    
    def add(self,component):
        self.components.append(component)

hdd = Leaf("hdd", 4000)
keyboard = Leaf("keyboard", 1000)
mouse = Leaf("mouse", 500)
ram = Leaf("ram", 3000)
processor = Leaf("Processor", 10000)

computer = Composite("computer")

motherboard = Composite("motherboard")
motherboard.add(ram)
motherboard.add(processor)

cabinet = Composite("cabinet")
cabinet.add(hdd)
cabinet.add(motherboard)

peripherals = Composite("peripherals")
peripherals.add(keyboard)
peripherals.add(mouse)

computer.add(cabinet)
computer.add(peripherals)

print(computer.showPrice())


# Link:
# https://medium.com/@akshatsharma0610/composite-design-pattern-b1ebd0756aa9