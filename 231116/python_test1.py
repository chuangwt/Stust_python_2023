import math
class MyShape:
    def __init__(self, side, length, witdth, radius):
        self.side = side
        self.length = length
        self.witdth = witdth
        self.radius = radius

    def square(self):
        print (self.side ** 2)

    def rectangle(self):
        print (self.length * self.witdth)

    def circle(self):
        print (self.radius * self.radius * math.pi)

s1 = MyShape (8,4,6,4) 
#lw2 = 8*4
#r3 = 4*4*math.pi

s1.square()
s1.rectangle()
s1.circle()