# Snake.py holds the snake as a dequeSNAKE
from collections import deque

from Square import Square, squareType

class Snake:

    def __init__(self, start_square):
        self.snake_queue = deque([start_square])
        start_square.setType(squareType.SNAKE)
        self.dead = False

    def move_snake(self, next_square):
        # next square is going to be infront, left, or right to the snake
        if (next_square.getType() == squareType.WALL or next_square.getType() == squareType.SNAKE):
            self.dead = True
            return
        if (next_square.getType() == squareType.FOOD):
            self.add_square(next_square)
            # TODO Make sure to add food here
        else:
            self.add_square(next_square)
            self.remove_tail()
        # TODO remove print statement later

            
    def add_square(self, next_square):
        self.snake_queue.appendleft(next_square)
        next_square.setType(squareType.SNAKE)

    def remove_tail(self):
        self.snake_queue[-1].setType(squareType.EMPTY)
        self.snake_queue.pop()

    def get_head(self):
        return self.snake_queue[0]

    def is_dead(self):
        return self.dead

"""
    def opposite_direction(direction):
        if direction
        """

