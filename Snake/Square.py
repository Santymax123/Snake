# Square objects to populate the board. Each square holds what type it is for game logic and rendering
from enum import Enum, unique

# TODO kinda unsure how Enum works still, but my code works so eh?
@unique
class squareType(Enum):

    EMPTY = 0
    WALL = 1
    FOOD = 2
    SNAKE = 3
    
    

class snake_type(Enum):
    NONE = 0
    END_UP = 1
    END_DOWN = 2
    END_RIGHT = 3
    END_LEFT = 4
    BODY_VERTICAL = 5
    BODY_HORIZONTAL = 6
    BODY_UR = 7
    BODY_DR = 8
    BODY_DL = 9
    BODY_UL = 10
    
    

class Square:
    def __init__(self, x, y):
        self.type = squareType.EMPTY
        self.snake_type = snake_type.NONE
        self.x = x
        self.y=y

    def setType(self, square_type):
        self.type = square_type

    def set_snake_type(self, snake_type):
        self.snake_type = snake_type

    def getType(self):
        return self.type

    def get_snake_type(self):
        return self.snake_type

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
