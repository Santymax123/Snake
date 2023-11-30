# Square objects to populate the board. Each square holds what type it is for game logic and rendering
from enum import Enum, unique

# TODO kinda unsure how Enum works still, but my code works so eh?
@unique
class squareType(Enum):

    EMPTY = 0
    WALL = 1
    FOOD = 2
    # Remove eventually
    SNAKE = 3
    # To be used for head. the OPPOSITE can also be used for tail 
    UP = 4
    DOWN = 5
    LEFT = 6
    RIGHT = 7
    # For anything between head and tail - each multi-direction one can be used for travelling both directions (see Snake Rendering.PNG
    BODY_VERTICAL = 8
    BODY_HORIZONTAL = 9
    BODY_UR = 10
    BODY_DR = 11
    BODY_DL = 12
    BODY_UL = 13
    
    
    

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
