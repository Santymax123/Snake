# Square objects to populate the board. Each square holds what type it is for game logic and rendering
from enum import Enum, unique

# TODO kinda unsure how Enum works still, but my code works so eh?
@unique
class squareType(Enum):

    EMPTY = 0
    WALL = 1
    FOOD = 2
    SNAKE = 3

class Square:
    def __init__(self, x, y):
        # Nothing in square on initial creation TODO is this the best way to do this?
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

'''
methods that chuyangliu implimented - I dont need these i think
str
eq
neg
add
sub
hash
manhattan distance
direction to
adjacent
all adj
'''
