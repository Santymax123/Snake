# Board.py holds and makes changes to the gamestate
from Square import Square, squareType

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create a 2D array of empty squares
        self.squares = [[0 for x in range(width)] for y in range(height)] # Currently initilizing filled with 0's then setting to squares - has to be a better way to do this
        for x in range(width):
            for y in range(height):
                self.squares[x][y] = Square(x,y)
        self.initialise()



    def initialise(self):
        # TODO Need to place random food
        # TODO need to place snake
        # TODO Chuyangliu also has an else statement to initialise everything else as empty but i believe that unnescesary
        for x in range(self.width):
            for y in range(self.height):
                if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    self.squares[x][y].setType(squareType.WALL)
    
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSquares(self):
        return self.squares

    # Only for debugging so far
    def setSquare(self, x, y, type):
        self.squares[x][y].setType(type)