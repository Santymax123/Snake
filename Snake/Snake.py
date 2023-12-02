# Snake.py holds the snake as a deque

from collections import deque

from Square import Square, square_type
import Board
from Direction import Direction

class Snake:

    def __init__(self, board):
        
        self.dead = False
        self.board = board

        start_square = board.get_squares()[board.get_width() // 2][board.get_height() // 2]

        self.snake_queue = deque([start_square])
        start_square.set_type(square_type.SNAKE)
        self.current_direction = Direction.NONE
        self.head = self.snake_queue[0]



    def move_snake(self, new_direction):

        next_square = self.get_next_square(new_direction)

        if (next_square.get_type() == square_type.WALL or next_square.get_type() == square_type.SNAKE):
            # Snake will kill itself at game start if user doesnt move without this - prevents itself from colliding with the head, which isnt possible when moving anyway
            if next_square != self.head:
                self.dead = True
                return
        if (next_square.get_type() == square_type.FOOD):
            self.add_square(next_square)
            self.board.new_food()
        else:
            self.remove_tail()
            self.add_square(next_square)
            
        

    # Takes input as a Direction and returns the next square the snake is to move to
    # Will not return a square behind the snake (snake cant write over itself)
    def get_next_square(self, new_direction):

        next_square = 0 # TODO should i initialize it as none???

        # TODO should i combine these 2 if statements?
        if self.current_direction == Direction.opposite(new_direction): # TODO is this good practise? 
            new_direction = self.current_direction
        elif new_direction == Direction.NONE:
            new_direction = self.current_direction
        
        if new_direction == Direction.UP:
            next_square = self.board.get_squares()[self.head.get_x()][self.head.get_y() - 1]
        elif new_direction == Direction.DOWN:
            next_square = self.board.get_squares()[self.head.get_x()][self.head.get_y() + 1]
        elif new_direction == Direction.LEFT:
            next_square = self.board.get_squares()[self.head.get_x() - 1][self.head.get_y()]
        elif new_direction == Direction.RIGHT:
            next_square = self.board.get_squares()[self.head.get_x() + 1][self.head.get_y()]
        # At the game start the snake doesnt move till key press
        else:
            next_square = self.board.get_squares()[self.head.get_x()][self.head.get_y()]
        
        self.current_direction = new_direction

        return next_square
        


    def add_square(self, next_square):
        self.snake_queue.appendleft(next_square)
        next_square.set_type(square_type.SNAKE)
        self.head = next_square

    def remove_tail(self):
        self.snake_queue[-1].set_type(square_type.EMPTY)
        self.snake_queue.pop()

    def is_dead(self):
        return self.dead
