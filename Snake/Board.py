# Board.py holds and makes changes to the gamestate
from Square import Square, squareType
# import random

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
        # TODO do i need to make a snake here or can i call it in initialise and its still in scope??



    def initialise(self):
        # TODO Need to place random food
        # TODO need to place snake
        # TODO Chuyangliu also has an else statement to initialise everything else as empty but i believe that unnescesary
        for x in range(self.width):
            for y in range(self.height):
                if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    self.squares[x][y].setType(squareType.WALL)
        snake = Snake(self.squares[self.width/2][self.length/2])
        new_food()

    # Takes an int direction
    # 0 NONE
    # 1 UP
    # 2 DOWN
    # 3 LEFT
    # 4 RIGHT
    def next_boardstate(direction):
        '''
        if direction == snake.getHead().oppositedirection: # TODO not implimented, snake cant move opposite to what it was just moving
            reverse direction
        
        if the square the snake head is about to move to is wall or snake:
            lose game
        elif the square the snake head is about to move to is food:
            move snake and dont delete tail # Make sure this overwrites the food
            new_food()
        else
            move snake and delete tail


    def new_food(self):
        empty_squares = []
        for x in range(self.width):
            for y in range(self.height):
                if self.squares[x][y].getType() == squareType.EMPTY:
                    empty_squares.append(self.squares[x][y])
        random.choice(empty_squares).setType(FOOD)
    '''
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSquares(self):
        return self.squares

    # Only for debugging so far
    def setSquare(self, x, y, type):
        self.squares[x][y].setType(type)
