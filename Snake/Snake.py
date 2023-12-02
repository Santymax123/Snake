# Snake.py holds the snake as a dequeSNAKE
from collections import deque

from Square import Square, squareType
import Board
from Direction import Direction

class Snake:

    def __init__(self, board):
        
        self.dead = False
        self.board = board

        start_square = board.getSquares()[board.getWidth() // 2][board.getHeight() // 2]

        self.snake_queue = deque([start_square])
        start_square.setType(squareType.SNAKE)
        self.current_direction = Direction.NONE
        self.head = self.snake_queue[0]



    def move_snake(self, new_direction):
        next_square = self.get_next_square(new_direction)
        # next square is going to be infront, left, or right to the snake
        if (next_square.getType() == squareType.WALL or next_square.getType() == squareType.SNAKE):
            # Snake will kill itself at game start if user doesnt move without this - basically prevents itself from colliding with the head, which isnt possible when moving
            if next_square != self.head:
                self.dead = True
                return
        if (next_square.getType() == squareType.FOOD):
            self.add_square(next_square)
            self.board.new_food()
        # TODO is this the same as the previous ask at current line 28 (6 lines above)
        #elif next_square != self.head:
            #return
        else:
            # Remove tail first because otherwise at game start snake will be invisible
            self.remove_tail()
            self.add_square(next_square)
            
        

    # TODO this is a clone of boards next_square since i decided to move the function into snake
    def get_next_square(self, new_direction):
        next_square = 0 # TODO should i initialize it as none???
        if self.current_direction == Direction.opposite(new_direction):
            new_direction = new_direction.opposite()
        elif new_direction == Direction.NONE:
            new_direction = self.current_direction
        
        if new_direction == Direction.UP:
            next_square = self.board.getSquares()[self.head.getX()][self.head.getY() - 1]
        elif new_direction == Direction.DOWN:
            next_square = self.board.getSquares()[self.head.getX()][self.head.getY() + 1]
        elif new_direction == Direction.LEFT:
            next_square = self.board.getSquares()[self.head.getX() - 1][self.head.getY()]
        elif new_direction == Direction.RIGHT:
            next_square = self.board.getSquares()[self.head.getX() + 1][self.head.getY()]
        # At the game start the snake doesnt move till key press
        else:
            next_square = self.board.getSquares()[self.head.getX()][self.head.getY()]
        
        self.current_direction = new_direction

        return next_square
        

    def add_square(self, next_square):
        self.snake_queue.appendleft(next_square)
        next_square.setType(squareType.SNAKE)
        self.head = next_square

    def remove_tail(self):
        self.snake_queue[-1].setType(squareType.EMPTY)
        self.snake_queue.pop()

    def is_dead(self):
        return self.dead
