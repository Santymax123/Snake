# Board.py holds and makes changes to the gamestate
from Square import Square, squareType
from Snake import Snake
import random

class Board:

    def __init__(self, width, height):
        # TODO Need to place random food
        # TODO Chuyangliu also has an else statement to initialise everything else as empty but i believe that unnescesary
        self.width = width
        self.height = height

        # Create a 2D array of empty squares
        self.squares = [[0 for x in range(width)] for y in range(height)] # Currently initilizing filled with 0's then setting to squares - has to be a better way to do this
        for x in range(width):
            for y in range(height):
                self.squares[x][y] = Square(x,y)
                if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    self.squares[x][y].setType(squareType.WALL)
        self.snake = Snake(self.squares[self.width//2][self.height//2])
        self.new_food()




    # Takes an int direction
    # 0 NONE
    # 1 UP
    # -1 DOWN
    # 2 RIGHT
    # -3 LEFT
    
    def next_square(self, direction):
        next_square = 0
        # For later
        #if direction == "NONE":
        #    nextsquare = self.squares[self.snake.get_head().getX()][self.snake.get_head().getX()]

        if direction == "UP":
            next_square = self.squares[self.snake.get_head().getX()][self.snake.get_head().getY() - 1]
        elif direction == "DOWN":
            next_square = self.squares[self.snake.get_head().getX()][self.snake.get_head().getY() + 1]
        elif direction == "LEFT":
            next_square = self.squares[self.snake.get_head().getX() - 1][self.snake.get_head().getY()]
        elif direction == "RIGHT":
            next_square = self.squares[self.snake.get_head().getX() + 1][self.snake.get_head().getY()]
        else:
            next_square = self.squares[self.snake.get_head().getX()][self.snake.get_head().getY() - 1]
        
        return next_square
        
            

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

    # Only for debugging so far
    def setSquare(self, x, y, type):
        self.squares[x][y].setType(type)

    def get_snake(self):
        return self.snake
