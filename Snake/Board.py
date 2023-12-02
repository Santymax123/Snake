# Board.py holds and makes changes to the gamestate
from Square import Square, squareType
import random

class Board:

    def __init__(self, width, height):
        # TODO Chuyangliu also has an else statement to initialise everything else as empty but i believe that unnescesary
        self.width = width
        self.height = height

        # Create a 2D array of empty squares
        self.squares = [[0 for x in range(width)] for y in range(height)] # TODO Currently initilizing filled with 0's then setting to squares - has to be a better way to do this
        for x in range(width):
            for y in range(height):
                self.squares[y][x] = Square(x,y)
                # Make walls around arena - also prevents snake from ever going out of bound and exiting the array
                if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    self.squares[x][y].setType(squareType.WALL)
        self.new_food()
        

    def new_food(self):
        empty_squares = []
        for x in range(self.width):
            for y in range(self.height):
                if self.squares[x][y].getType() == squareType.EMPTY:
                    empty_squares.append(self.squares[x][y])
        food_square = random.choice(empty_squares)
        food_square.setType(squareType.FOOD)
    

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSquares(self):
        return self.squares