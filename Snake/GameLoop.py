# Main.py is currently being used to test that my code works, will eventually be turned into something like Game.py that handles gamestate etc

from GUI import Display
from Board import Board

import pygame
from Square import Square, squareType
from Snake import Snake

GAME_SPEED = 5 # FPS

# Test to make sure GUI is updating
def runGame():
    # loop to try get some display updates
    snake_dead = False
    while (not snake_dead):
        # Updates display
        display.update()
        # Waits one second
        clock.tick(GAME_SPEED)
        # 
        input = display.get_input()
        snake.move_snake(input)
        if snake.is_dead():
            display.game_over()
            clock.tick(GAME_SPEED / 2)
            snake_dead = True

            

board = Board(10, 10)
snake = Snake(board)
display = Display(board)
clock = pygame.time.Clock()
runGame()
pygame.quit()
quit()

