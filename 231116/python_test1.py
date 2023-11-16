import math
class MyShape:
    def __init__(self, side, length, witdth, radius):
        self.side = side
        self.length = length
        self.witdth = witdth
        self.radius = radius

    def getSquareArea(self):
        print (self.side ** 2)

    def gteRectangleArea(self):
        print (self.length * self.witdth)

    def getCircleArea(self):
        print (self.radius * self.radius * math.pi)

s1 = MyShape (8,4,6,4) 

s1.getSquareArea()
s1.gteRectangleArea()
s1.getCircleArea()