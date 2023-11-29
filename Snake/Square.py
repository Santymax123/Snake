from enum import Enum, unique

@unique
class squareType(Enum):

    EMPTY = 0
    WALL = 1
    FOOD = 2

class Square:

    def __init__(self, x, y):
        self.type = squareType.EMPTY
        self.x = x
        self.y=y

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getX(self):
        return self.x

    def getY(self):
        return self.y


#str
#eq
#neg
#add
#sub
#hash
#manhattan distance
#direction to
#adjacent
#all adj
