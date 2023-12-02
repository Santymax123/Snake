# Board.py holds the board as a 2D array of squares
from Square import Square, square_type
import random

class Board:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        # Create a 2D array of empty squares
        self.squares = []
        for x in range(width):
            row = []
            for y in range(height):
                square = Square(x,y)
                if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    square.set_type(square_type.WALL)
                row.append(square)
            self.squares.append(row)
                
        #self.squares = [[0 for y in range(width)] for x in range(height)]
        #for x in range(width):
            #for y in range(height):
                #self.squares[x][y] = Square(x,y)

                # Make walls around arena - also prevents snake from ever going out of bound and exiting the array
                #if (x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1):
                    #self.squares[x][y].set_type(square_type.WALL)
                    
        self.new_food()
        

    def new_food(self):
        empty_squares = []
        for x in range(self.width):
            for y in range(self.height):
                if self.squares[x][y].get_type() == square_type.EMPTY:
                    empty_squares.append(self.squares[x][y])
        food_square = random.choice(empty_squares)
        food_square.set_type(square_type.FOOD)
    

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_squares(self):
        return self.squares