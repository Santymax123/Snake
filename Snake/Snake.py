# Snake.py holds the snake as a deque
from collections import deque

from Square import Square
from Board import Board

class Snake:

    def __init__(self, start_square):
        self.snake_queue = deque([start_square])

    def move_snake(self, next_square, ate_food):
        if ate_food:
            add_square(next_square)
        else:
            add_square(next_square)
            remove_square()
            
    def add_square(self, next_square):
        self.snake_queue.appendleft(next_square)
        next_square.setType(SNAKE)

    def remove_square(self):
        self.snake_queue[-1].setType(EMPTY)
        self.snake_queue.pop()


    def get_gead():
        return self.snake_queue[0]

