# GameLoop is currently being used to test that my code works, will eventually be turned into something like Game.py that handles gamestate etc
# Run this file to play snake!

import pygame

from GUI import Display
from Board import Board
from Snake import Snake

GAME_SPEED = 5 # FPS
BOARD_WIDTH = 15
BOARD_HEIGHT = 15


# Loop that runs all game logic and ends when the snake dies
def Game_Loop():

    snake_dead = False

    while (not snake_dead):

        display.update()
        clock.tick(GAME_SPEED)
        input = display.get_input()
        snake.move_snake(input)
        
        if snake.is_dead():
            display.game_over()
            clock.tick(5)
            snake_dead = True



# Create all the objects required for the game
board = Board(BOARD_WIDTH, BOARD_HEIGHT)
snake = Snake(board)
display = Display(board)
clock = pygame.time.Clock()

Game_Loop()

# Close GUI
pygame.quit()
quit()

